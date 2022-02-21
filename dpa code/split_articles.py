# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:21:11 2021

@author: jbaer
"""

import re
import pandas as pd

# Define a function that splits up collections of articles into single articles
def split_articles(multiple_articles):
    """
    Returns split up articles
    """
    
    split_art =[]
    
    multiple_articles.reset_index(inplace = True, drop = True)
    
    for index, row in multiple_articles.iterrows():
        
        mult_art = []

        # check if capitlaizeted words exist in text.
        capital_words = re.findall(r'\b[A-ZÄÖÜß:\-]{10,}\b', row["texts"])
             
        if len(capital_words) > 1:
            # split articles based on paragraphs and the occurence of uppercase
            # words (a.k.a titles)
            mult_art = re.findall(r'[A-ZÄÖÜß:-]{2,}(?:\s+[A-ZÄÖÜß:\-]+)+.{15,}?(?:\s{2,}|$)', row["texts"])    

        else:
            
            # search for dpa references
            dpa_ref = re.findall(r'\(dpa.*?\)', row["texts"])

            # if there is a dpa reference search for mutliple articles
            if len(dpa_ref) >= 1:
                  
                # split articles based on paragraphs
                mult_art = re.findall(r'(?:^.+?(?:\s{2,})|(?:\s{2,})).+?(?:\s{2,}|$)', row["texts"])     
                
                # the existence of more dpa references than number of articles indicates that we need
                # a different pattern for splitting the articles
                if len(mult_art) < len(dpa_ref):
                
                    headlines = re.findall(r'((?:^|(?<=\.))[^.]+?(?=\(dpa.+?))', row["texts"])
                    txt = row["texts"]
                    for headline in headlines:
                        txt = txt.replace(headline, 'SEP')
                    mult_art = [i.strip() for i in txt.split('SEP')][1:]
                    mult_art = [headline + art for headline, art in zip(headlines, mult_art)]

            else:
                
                # split articles based on paragraphs (can sometimes lead to false positives)
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