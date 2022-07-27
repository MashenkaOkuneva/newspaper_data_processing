# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:21:11 2021

@author: jbaer
"""

import re
import pandas as pd

def split_articles(multiple_articles):
    """
    This function splits up collections of articles into single articles.
    """
    
    split_art =[]
    
    multiple_articles.reset_index(inplace = True, drop = True)
    
    for index, row in multiple_articles.iterrows():
        
        mult_art = []

        # Check if fully capitalized words exist in article.
        capital_words = re.findall(r'\b[A-ZÄÖÜß:\-]{5,}\b', row["texts"])
          
        # If there is more than one fully capitalized word (a.k.a titles) in 
        # the article, check if fully capitalized words are at the beginning 
        # of paragraphs. A fully capitalized at the beginning of a paragraph
        # indicates the beginning of a new article
        if len(capital_words) > 1:
            # Split articles based on paragraphs and the occurence of fully 
            # capitalized words 
            mult_art = re.findall(r'[A-ZÄÖÜß:-]{2,}(?:\s+[A-ZÄÖÜß:\-]+)+.{30,}?(?:\s{2,}|$)', row["texts"])    

        # A second indication for multiple articles is the occurence of 
        # multiple dpa references. 
        else: 
            # Search for dpa references
            dpa_ref = re.findall(r'\(dpa.*?\)', row["texts"])
            # If there is a dpa reference search for mutliple articles
            if len(dpa_ref) >= 1:
                  
                # Split articles based on paragraphs
                mult_art = re.findall(r'(?:^.+?(?:\s{2,})|(?:\s{2,})).+?(?:\s{2,}|$)', row["texts"])     
                
                # The existence of more DPA references than paragraphs
                # indicates that we need a different pattern for splitting the
                # articles
                if len(mult_art) < len(dpa_ref):
                    print(index)
                    # Search for headline preceding the DPA references
                    headlines = re.findall(r'((?:^|(?<=\.))[^.]+?(?=\(dpa.+?))', row["texts"])
                    txt = row["texts"]
                    
                    # Repleace headline with 'SEP'
                    for headline in headlines:
                        txt = txt.replace(headline, 'SEP')
                    
                   # Split text by 'SEP' tokens
                    mult_art = [i.strip() for i in txt.split('SEP')][1:]
                    
                    # Store headline and splitted articles for metadata
                    mult_art = [headline + art for headline, art in zip(headlines, mult_art)]

            else:
                
                # If neither capitalized words nor multiple DPA references can
                # be found in the text split articles based on paragraphs
                # This method can sometimes lead to false positives, hence the 
                # two previous approaches
                mult_art = re.findall(r'(?:^.+?(?:\s{2,})|(?:\s{2,})).+?(?:\s{2,}|$)', row["texts"])    
         
        if mult_art != []:
            
            for art in mult_art:
                # Store meta data for the article
                seperated_articles = multiple_articles.iloc[index][multiple_articles.iloc[index] != 'texts']
                # Assign the new text to the matching meta data
                seperated_articles['texts'] = art
                split_art.append(seperated_articles)
                    
        else:
            split_art.append(row) 

    return(pd.concat(split_art, axis=1).transpose())