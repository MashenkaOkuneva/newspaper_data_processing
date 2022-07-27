# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 16:12:20 2021

@author: jbaer
"""

import re
import pandas as pd

def continue_articles(full_data):
    """  
    This function returns joined continuations and the indices of seperate 
    condinuations. 
    """
    
    data = full_data[0]
    meta_data = full_data[1]
    
    data.reset_index(inplace = True, drop = True)
    meta_data.reset_index(inplace = True, drop = True)
 
    drop_ind = []
    cont_articles = pd.DataFrame()
    
    # Subsequent parts of articles are usually marked by titles with a double
    # dash followed by a number. The number is either 2,3 or 4 indicating
    # the position of the article
    for ind, title in enumerate(data['title']): 
        
        # Check of index belongs to an article that was already processed
        if ind not in drop_ind:
        
            # Check if title is not NAN
            if title == title:
                
                # Check if pattern '--[digit]' occurs in text
                if bool(re.search(r'(--[0-9])|(--\s[0-9])', title)):
                    
                    # Get title without '--[digit]' to identify the article on 
                    # which the continuation is based on
                    clean_title = re.split(r'(--[0-9])|(--\s[0-9])', title)[0].replace('\n', '').strip()
                    articles = data[data['title'].map(str).replace('\n', ' ', regex = True).str.contains(re.escape(clean_title), regex = True, na = False)].copy()
                    
                    # Save indices to delete articles later
                    drop_ind += list(articles.index)
                        
                    if len(articles) > 1:
                        
                        # Bring articles in the correct order
                        orders = []
                
                        for indx, article in articles.iterrows():
                            
                            order = re.search(r'(--[0-9])|(--\s[0-9])', article['title'])
                            if order != None:
                                orders.append(int(order[0][-1:]))
                            else:
                                orders.append(1)
                        
                        # The full articles is sometimes published after its
                        # single parts. To identify these cases, check if the 
                        # last entry of articles is longer than all other parts
                        # combined                   
                        full_art = False
                    
                        if len(orders) > 2 and orders[-1] == 1:
                            
                            max_length = max(articles['length'])
                            max_length_pos = list(articles['length']).index(max(articles['length']))
                            
                            if max_length >= sum([l for i,l in enumerate(articles['length']) if i!=max_length_pos]):
                                
                                full_art = True
                                full_text = articles.iloc[max_length_pos]['texts']
                                
                        if full_art == False:
                            
                            # Bring sperate parts in correct order
                            articles['order'] = orders
                            articles = articles.sort_values(['order'])
                
                            # Join the start of article and its continuation(s)
                            full_text = ' '.join(articles['texts'])
                        
                        # Select meta data for new article
                        cont_article = meta_data[list(meta_data.index == meta_data.index[0]+ind)].copy().iloc[0,:]
                        cont_article['title'] = clean_title
                        
                        # Filter out '(Fortseztung)' (continuation) from the 
                        # full text
                        full_text = full_text.replace('(Fortsetzung) -', '')
                        
                        # Set text of new article to full text
                        cont_article.loc['texts'] = full_text
                        cont_articles = cont_articles.append(cont_article)
                                      
    return drop_ind, cont_articles