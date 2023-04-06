# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 11:30:55 2022

@author: jbaer
"""

import pandas as pd
from tqdm import tqdm
import re


def multi_part_art(mult_art, data):
    
    '''
    This function identifies texts that are split across multiple articles and 
    merges them together into single articles.

    '''
    def cont_art(title_fol, mult_art, delete_index, data, ty):    
        
        '''
        This function searches for follow-up articles based on a given title
        and returns the text of the follow-up article for further use.
        
        Parameters
        ----------
        title_fol : string or None
            Title used to identify the following article.
        mult_art : DataFrame
            Dataframe of articles, where each article is potentially a part of a larger article,
            and its continuation is in another article.
        delete_index : list
            Indices of articles that can be deleted from the main corpus. The function
            adds the indices of the selected starting and follow-up articles.
        data : DataFrame
            Main corpus.
        ty : string
            Either "Type 1" or "Type 2". "Type 1" refers to articles where the last sentence is the 
            beginning of the next article. "Type 2" refers to articles with the same main headline.

        Returns
        -------
        text_fol : string
            Text from the following article. This text
            can be added to the text of the starting article.
        delete_index : list
            Indices of articles that can be deleted from the main corpus. 
        title_fol : string or None
            Title that can be used to identify the next follow-up article in line.
            
        '''
        
        if len(title_fol) > 1:
            
            # Select all potential follow-up articles based on the title.
            article_fol = data[data['title'].str.contains(title_fol, na = False, regex = False)]
            
            if not article_fol.empty:
                
                if len(article_fol) > 1:
                
                    # Obtain the dates of all potential follow-up articles.
                    date_fol = article_fol[['year', 'month', 'day']]
                    
                    # Retrieve the indices of all follow-up articles having the same date
                    # as the first article.
                    idx_fol = date_fol[(date_fol == date).all(1)]
                    
                    if not date_fol[(date_fol == date).all(1)].empty:
                        
                        if ty == "Type 1":
                                                        
                            idx_fol = idx_fol.index[0]
                            
                            article_fol = article_fol.loc[idx_fol].to_frame().T
                    
                            text_fol = article_fol['texts'].iloc[0].replace(title_fol, '')
                                
                            # Obtain the title for the subsequent article from the last sentence
                            # of the currently selected article. 
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
                    
                    if ty == "Type 1":
                        
                        text_fol = article_fol['texts'].iloc[0].replace(title_fol, '')
                        
                    elif ty == "Type 2":
                        
                        text_fol = article_fol['texts'].iloc[0]
                                  
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
            
            # If the last sentence of an article begins with "Folgt", it can be 
            # used as the title to identify the subsequent article, which is the
            # continuation of the current article.
            title_fol = re.search('[Ff]olgt (.{,75}?)(?:\)|$|(?: # dpa-Notizblock)|(?:\())',text)
            
            if title_fol is not None:
                
                title_fol = title_fol.groups(1)[0]
                text = re.sub('Folgt ' + title_fol, '', text)
                
                ty = "Type 1"
                
            elif title_fol is None:
                
                # If the title of the article contains "... - number Teile",
                # the title can be used to identify all articles that belong together.
                
                ty = "Type 2"
                
                try:
                    
                    title_fol = re.search('(- \w+ Teile\){0,1})(.*)', title).groups(0)[1]
                                   
                except:
                    
                    continue
            
            if ty == "Type 1":
            
                # Identfiy the subsequent article and add its text to the text of the starting article.
                # Repeat this step until the last article is reached.
                while title_fol is not None:
                    
                    text_fol, delete_index, title_fol = cont_art(title_fol, mult_art, delete_index, data, ty)
                        
                    text += text_fol
                    
            elif ty == "Type 2":
                
                text, delete_index, title_fol = cont_art(title_fol, mult_art, delete_index, data, ty)
                
            article.loc['texts'] = text
            
            articles_final = pd.concat([articles_final, article.to_frame().T])
            
                 
    delete_index = list(set(delete_index))    
    
    return(delete_index, articles_final)