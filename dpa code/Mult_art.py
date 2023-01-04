# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:30:55 2022

@author: jbaer
"""

import pandas as pd
from tqdm import tqdm
import re

data = pd.read_csv('D:\Studium\PhD\Media Tenor\Results\Code neu\dpa_step1_testing.csv')
mult_art = data[data['title'].str.contains('(?:zwei|drei|drei|vier|fünf|sechs) Teile', na = False)]

def multi_part_art(mult_art, data):
    '''
    This function identifies texts which are split over multiple articles and 
    merges them together to single articles.

    '''
    
    def cont_art(title_fol, mult_art, delete_index, data, ty):    
        
        '''
        This function searches for follow-up articles based on a given title
        and returns text of the follow-up articles for further use.
        
        Parameters
        ----------
        title_fol : string or None
            Title which is used to identify the following article
        mult_art : DataFrame
            Dataframe of articles which are potentially split up into smaller articles
        delete_index : list
            Indices of articles which can be deleted from main corpus. The function
            adds the indices of the selected start and follow up articles.
        data : DataFrame
            Main Corpus
        ty : string
            Either "Type 1" or "Type 2". "Type 1" are articles where the last sentence is the 
            beginning of the next article. "Type 2" are articles with the same main headline.

        Returns
        -------
        text_fol : string
            Text from the following article. The text
            can be added to the text of the starting article.
        delete_index : list
            Indices of articles which can be deleted from the main corpus. 
        title_fol : string or None
            Title which can can be used to identify the next follow-up article in line.
            
        '''
          
        if len(title_fol) > 1:
            
            # Select all potential follow-up articles based on the title.
            article_fol = data[data['title'].str.contains(title_fol, na = False, regex = False)]
            
            if not article_fol.empty:
                
                if len(article_fol) > 1:
                
                    # Get dates of all potential follow-up articles.
                    date_fol = article_fol[['year', 'month', 'day']]
                    
                    # Get indices of all follow-up articles with the same date
                    # as the first article.
                    idx_fol = date_fol[(date_fol == date).all(1)]
                    
                    if not date_fol[(date_fol == date).all(1)].empty:
                        
                        if ty == "Type 1":
                            
                            idx_fol = idx_fol.index[0]
                    
                            text_fol = article_fol['texts'].iloc[0].replace(title_fol, '')
                                
                            # Get title for the next following article from the last sentence
                            # of the article currently selected. 
                            title_fol = re.search('Folgt (.{,75}?)$',text_fol)
                            
                            if title_fol is not None:
  
                                title_fol = title_fol.groups(1)[0]
                            
                        elif ty == "Type 2":
                            
                            idx_fol = list(idx_fol.index)
                            
                            article_fol = article_fol.loc[idx_fol]
                            
                            text_fol = ' '.join(article_fol['texts'])
                            
                            title_fol = None
                        
                    else:
                        
                        title_fol = None
                        text_fol = ''
                                            
                else:
                    
                    text_fol = article_fol['texts'].iloc[0].replace(title_fol, '')
                                  
                    title_fol = re.search('Folgt (.{,75}?)$',text_fol)
                    
                    if title_fol is not None:
  
                        title_fol = title_fol.groups(1)[0]
                
                if ty == "Type 1":
                    
                    delete_index.append(article_fol.index[0])
                    
                elif ty == "Type 2":
                    
                    delete_index.extend(list(article_fol.index))
                
            else:
                
                title_fol = None
                text_fol = '' 
            
        return(text_fol, delete_index, title_fol)

    delete_index = []
    articles_final = pd.DataFrame()
    
    for idx, title in tqdm(enumerate(mult_art['title'])):   
        
        if not mult_art.index[idx] in delete_index:
        
            article = mult_art.iloc[idx].copy()
            text = article['texts']            
            date = list(article[['year', 'month', 'day']])
            
            delete_index.append(mult_art.index[idx])
            
            # If the last sentence of the article begins with "Folgt", it can be 
            # used as a title to identify the following article.
            title_fol = re.search('[Ff]olgt (.{,75}?)(?:\)|$|(?: # dpa-Notizblock)|(?:\())',text)
            
            if title_fol is not None:
                
                title_fol = title_fol.groups(1)[0]
                text = re.sub('Folgt ' + title_fol, '', text)
                
                ty = "Type 1"
                
            elif title_fol is None:
                
                # If the title of the articles includes "Teil (number) - (number) Teile"
                # (part (number) - (number) parts) the title can be used to identify 
                # all articles which belong together.
                
                ty = "Type 2"
                
                try:
                    
                    title_fol = re.search('(- \w+ Teile)(.*)', title).groups(0)[1]
                                   
                except:
                    
                    continue
            
            if ty == "Type 1":
            
                # Identfiy the followign article and add its text to the text of the starting article.
                # Repeat this step until the last article is reached.
                while title_fol is not None:
                    
                    text_fol, delete_index, title_fol = cont_art(title_fol, mult_art, delete_index, data, ty)
                        
                    text += text_fol
                    
            elif ty == "Type 2":
                
                text, delete_index, title_fol = cont_art(title_fol, mult_art, delete_index, data, ty)
                
            article.loc['texts'] = text
            
            articles_final = articles_final.append(article)
         
    delete_index = list(set(delete_index))    
    
    return(delete_index, articles_final)