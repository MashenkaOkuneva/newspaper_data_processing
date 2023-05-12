# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 23:30:07 2022

@author: jbaer
"""

##############################################################################

import re

def delete_aktualisierung_index(data):
    '''
    This function identifies the updated news text/s with the keyword 'Aktualisierung'
    in the title and its/their original version.
    
    If the original article and its update are published on the same day,
    this function returns the index of the original article. Later, we use the index
    to delete the original article. If multiple updates are published on the
    same day, we only keep the one that was created last. To identify an update created
    later than others, we use the file name.
    
    If the original article and its last update are published on different days,
    both news reports are kept. However, if there is more than one update, we keep 
    only the most recent one with the highest number in the file name. This function 
    returns the indices of all intermediate updates that we later delete.
    '''

    delete_index = []
    ignore = []
    
    # select all "Aktualisierung" articles
    data_aktualisierung = data[data['title'].str.contains('\((?:.*?)Aktualisierung(?:.*?)\)', na = False)]
    
    for idx, title in enumerate(data_aktualisierung['title']):   

        akt_ind = []        

        # remove the "Aktualisierung" note from the title
        title = re.sub('\((?:.*?)Aktualisierung(?:.*?)\)', '', title,1).strip()
      
        # check if a title exists, is not on the ignore list and is not part of "dpa-Vorausmeldungen"
        if (len(title) > 1 and title not in ignore and all(s not in title for s in ['dpa-Vorausmeldungen kompakt: Das bringt der Tag.', 'dpa-Vorausmeldung kompakt: Das bringt der Tag.'])):
            
            # add title to ignore list to ignore all articles with same title in the next iteration
            ignore.append(title)
            
            # select all articles with same title from the full dataset
            akt_title = data[data['title'].str.contains(title, na = False, regex = False)]
            
            # If only one article with the given title was found, use the first
            # sentence from the main text instead to select articles.
            # In most cases, the title and first sentence are the same, but
            # sometimes the first sentence helps identify the original article.
            if len(akt_title) == 1:
                
                text = data_aktualisierung.iloc[idx]['texts']
                text = re.sub('\((?:.*?)Aktualisierung(?:.*?)\)(\.?)', '', text,1).strip()
                
                # select the first sentence from the main text
                try:
                
                    first_sent = re.findall('(^.*?[a-z]{2,}[.!?])\s+\W*[A-Z]', text)[0]
                    
                except:
                    
                    first_sent = ''
                    
                if  first_sent != '':
                
                    # select all articles with same starting sentence from the full dataset
                    akt_sent = data[data['texts'].str.contains(first_sent, na = False, regex = False)]
                    
                    # if multiple articles were found, save indices of all the articles
                    if len(akt_sent) > 1:
                        
                        akt_ind = akt_sent.sort_values(by=['file']).index.tolist()                      
           
            # if multiple articles were found, save indices of all the articles
            elif len(akt_title) > 1:
                
                akt_ind = akt_title.sort_values(by=['file']).index.tolist()            
                
            if akt_ind != []:
                 
                # check if the first article is the original article
                if akt_ind[0] not in data_aktualisierung.index:
                
                    data_first_art = data[data.index == akt_ind[0]][['day', 'month', 'year']].values.tolist()[0]
                    data_last_art = data[data.index == akt_ind[-1]][['day', 'month', 'year']].values.tolist()[0]
                    
                    # Check if the date of the original article is the same as the date
                    # of the latest "Aktualisierung" article.
                    # Add the index of the original article and the indices of all 
                    # the intermediate updates to the delete_index list if that is the case.
                    # If that is not the case, keep the original article,
                    # but delete all the intermediate updates.
                    if data_first_art == data_last_art:
                        
                        delete_index.extend(akt_ind[:-1])
                    
                    else:

                        delete_index.extend(akt_ind[1:-1])
                        
                else:
                    
                    delete_index.extend(akt_ind[:-1])
                
    delete_index = list(set(delete_index))
    
    return(delete_index)