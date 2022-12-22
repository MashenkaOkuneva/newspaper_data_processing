# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:30:55 2022

@author: jbaer
"""

import pandas as pd
from tqdm import tqdm
import re

#mult_art = data[data['title'].str.contains('(?:zwei|drei|drei|vier|fünf|sechs) Teile', na = False)]

def multi_part_art(mult_art, data):

    delete_index = []
    articles_final = pd.DataFrame()
    
    for idx, title in tqdm(enumerate(mult_art['title'])):   
        
        article = mult_art.iloc[idx].copy()
        text = article['texts']
        date = list(article[['year', 'month', 'day']])
        
        # If the last sentence of the article begins with "Folgt", it can be 
        # used as a title to identify the following article
        
        title_fol = re.search('Folgt (.{,75}?)$',text)
        
        if title_fol is not None:
            
            title_fol = title_fol.groups(1)[0]
        
        def cont_art(title_fol, mult_art, delete_index, data):
            
            
            if len(title_fol) > 1:
                
                # Select all potential follow-up articles based on the title
                article_fol = data[data['title'].str.contains(title_fol, na = False, regex = False)]
                
                if not article_fol.empty:
                
                    # If multiple potential follow-up articles where found, select
                    # only the article with the same date as the first article
                    if not (isinstance(article_fol, pd.Series)):
                        
                        article_fol.reset_index(inplace = True, drop = True)
                    
                        date_fol = article_fol[['year', 'month', 'day']]
                        
                        idx_fol = date_fol[(date_fol == date).all(1)]
                        
                        if not date_fol[(date_fol == date).all(1)].empty:
                        
                            idx_fol = idx_fol.index[0]
                        
                            article_fol = article_fol.iloc[idx_fol]
                    
                            text_fol = re.sub(title_fol, '', article_fol['texts'])
                                      
                            title_fol = re.search('Folgt (.{,75}?)$',text_fol)
                            
                        else:
                            
                            title_fol = None
                            text_fol = ''
                    
                    if title_fol is not None:
                    
                        title_fol = title_fol.groups(1)[0]
                        
                    delete_index.append(article_fol.index[0])
                    
                else:
                    
                    title_fol = None
                    text_fol = '' 
                
            return(text_fol, delete_index, title_fol)
    
        # Use the last sentence from each article to search for the following article. 
        while title_fol is not None:
            
            text_fol, delete_index, title_fol = cont_art(title_fol, mult_art, delete_index, data)
                
            text += text_fol
                
        article.loc['texts'] = text
        
        articles_final = articles_final.append(article)
        
    return(delete_index)
        
multi_part_art(mult_art)          


# Examples:
# 5739309.xml
# 5739311.xml


# 5739731.xml

# keyword:  Abendvorschau   
# title: Die 603 Abgeordneten des Bundestages in der 15. Wahlperiode.   