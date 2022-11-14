# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 23:30:07 2022

@author: jbaer
"""

##############################################################################

import re
#import pandas as pd

def delete_aktualisierung_index(data):
    '''
    This function identifies "Aktualisierung" articles and returns a list of indices
    with outdated "Aktualisierung" articles to delete them later.
    '''

    delete_index = []
    #keep_index = []
    
    for idx, title in enumerate(data['title']):
        
        # remove the "Aktualisierung" note from the title
        title = re.sub('\((.*?)Aktualisierung(.*?)\)', '', title,1).strip()
      
        # check if title exists and is not part of "dpa-Vorausmeldungen"
        if (len(title) > 1 and all(s not in title for s in ['dpa-Vorausmeldungen kompakt: Das bringt der Tag.', 'dpa-Vorausmeldung kompakt: Das bringt der Tag.'])):
            
            # select all articles with same title
            akt_title = data[data['title'].str.contains(title, na = False, regex = False)]
            
            # if only one article with the given title was found, use the first
            # sentence from the main text instead to select articles
            if len(akt_title) == 1:
                
                text = data.iloc[idx]['texts']
                text = re.sub('\((.*?)Aktualisierung(.*?)\)(\.?)', '', text,1).strip()
                
                # select the first sentence from the main text
                try:
                
                    first_sent = re.findall('(^.*?[a-z]{2,}[.!?])\s+\W*[A-Z]', text)[0]
                    
                except:
                    
                    first_sent = ''
                    
                if  first_sent != '':
                
                    # select all articles with same starting sentence
                    akt_sent = data[data['texts'].str.contains(first_sent, na = False, regex = False)]
                    
                    # if multiple article were found, save all indices except the last one
                    # to delete the corresponding articles later
                    if len(akt_sent) > 1:
                        
                        akt_ind = akt_sent.sort_values(by=['file']).index.tolist()
                        delete_index.extend(akt_ind[:-1])
                        
                        #keep_index.extend(akt_ind[-1:]) 
           
            # if multiple article were found, save all indices except the last one
            # to delete the corresponding articles later
            elif len(akt_title) > 1:
                
                akt_ind = akt_title.sort_values(by=['file']).index.tolist()
    
                delete_index.extend(akt_ind[:-1])
                #keep_index.extend(akt_ind[-1:])
                
    delete_index = list(set(delete_index))
    #keep_index = list(set(delete_index))
    
    return(delete_index)