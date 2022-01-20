# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:12:20 2021

@author: jbaer
"""

import re
import itertools
import pandas as pd

def continue_articles(full_data):
    """  
    Returns joined continuations and the indices of seperate contination articles
    """
    
    data = full_data[0]
    drop_ind = []
    cont_articles = pd.DataFrame()
    meta_data = full_data[1]
    
    for ind, title in enumerate(data['title']): 
        
        if title == title:
            
            # Check if pattern '--[digit]' occurs in text
            if bool(re.search(r'(--[0-9])|(--\s[0-9])', title)):
                
                # Get title without '--[digit]' to identify the article on which the 
                # continuation is based on
                clean_title = re.split(r'(--[0-9])|(--\s[0-9])', title)[0]  
                articles = data[data['title'].str.contains(re.escape(clean_title.strip()), regex = True, na = False)].copy()
                
                # Save indices to delete articles
                drop_ind.append(ind)
                
                try:
                    
                    if len(articles) > 1:
                        
                        # Bring articles in the correct order
                        orders = []
                
                        for ind, article in articles.iterrows():
                            
                            order = re.search(r'(--[0-9])|(--\s[0-9])', article['title'])
                            if order != None:
                                orders.append(int(order[0][2]))
                            else:
                                orders.append(1)
                        
                        articles['order'] = orders
                        articles = articles.sort_values(['order'])
                        
                        # Select meta data
                        cont_article = meta_data[list(meta_data.index == meta_data.index[0]+ind)].copy().iloc[0,:]
                        cont_article['title'] = clean_title
                        
                        # Drop articles 
                        data = data.drop(articles.index)
                            
                        # Join the start of article and its continuation(s)
                        full_text = ' '.join(articles['texts'])
                        
                        # Filter out '(Fortseztung)' (continuation)
                        full_text = full_text.replace('(Fortsetzung)', '')
                        
                        # Get index of start article and its continuation
                        ind = list(article.index)
                        
                        cont_article.loc['texts'] = full_text
                        cont_articles = cont_articles.append(cont_article)
                                  
                except:
                
                    continue
            
    # drop_ind = sorted(set(map(tuple, drop_ind))) 
    # drop_ind = list(itertools.chain(*drop_ind))
    
    return drop_ind, cont_articles