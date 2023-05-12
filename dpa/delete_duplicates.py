# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:37:21 2022

@author: mokuneva
"""

##############################################################################

import re

def delete_duplicates(data):
    '''
    This function returns the indices of the duplicate articles.
    
    First, we identify articles that have the same title as one of the summaries, 
    overviews, repeated articles, or advance notifications and are published on the
    same day. If we find such articles, among all articles with the same title 
    (including summaries, overviews, repeated articles, and advance notifications),
    we keep the one with the highest words count (column 'word_count'). 
    The other articles are considered as duplicates.
    '''

    delete_index = []
    ignore = []
    
    # A dataframe with all the summaries, overviews, repeated articles, or advance 
    # notifications published on the same day.
    # We do not consider articles that contain the string 'dpa-Vorausmeldungen kompakt'
    # in the title because these articles contain multiple articles.
    dup_types = data[(data.title.str.contains('Zusammenfassung|zusammenfassung|Überblick|Wiederholung|Vorausmeldung'))  & \
                 (~data.title.str.contains('dpa-Vorausmeldungen kompakt'))]
    # Remove the "Aktualisierung" note from the titles of summaries,
    # overviews, repeated articles, or advance notifications
    # (in the previous step of our analysis we might have deleted
    # the original articles)
    dup_types.loc[:,'title'] = [re.sub('\((?:.*?)Aktualisierung(?:.*?)\)', '', dup_title,1).strip() for dup_title in dup_types.title]
    # Remove the "Aktualisierung" note from the titles of all articles
    # published on the same day.
    data.loc[:,'title'] = [re.sub('\((?:.*?)Aktualisierung(?:.*?)\)', '', tit,1).strip() for tit in data.title]
    # Titles of all the articles published on the same day as one of the 
    # summaries, overviews, repeated articles, or advance notifications.
    for title in data.title:
        # If the title of the summary, overview, repeated article, or advance 
        # notification article contains the title we consider, the title is not empty,
        # and was not considered before
        if len(dup_types[dup_types['title'].str.contains(title, na = False, regex = False)])>0 and \
            len(title) > 1 and title not in ignore:
                                        
            # Select all articles with this title from the full dataset
            dup_titles = data[data['title'].str.contains(title, na = False, regex = False)]
            
            # Remove the "Zusammenfassung" note from the title
            title_zus_clean = title.replace('Zusammenfassung ', '')
            # This condition takes into account the case where the summary ('Zusammenfassung title') 
            # and overview ('Überblick title') have the same title
            # Check if we can find more articles with the title stripped of the
            # "Zusammenfassung" note
            if len(data[data['title'].str.contains(title_zus_clean, na = False, regex = False)]) > \
                len(dup_titles):
                    dup_titles = data[data['title'].str.contains(title_zus_clean, na = False, regex = False)]
                    
            # If multiple articles were found, keep only one article with
            # the highest word count. Add indices of other articles to list
            # delete_index. These are duplicates.
            if len(dup_titles) > 1:                
                delete_index.extend(dup_titles.sort_values(by=['word_count']).index.tolist()[:-1])
            
            # Add titles of all the articles we've just considered to the ignore list    
            ignore.extend(dup_titles.title)
        else:
            # If the article does not share the title with one of the summaries,
            # overviews, repeated articles, or advance notifications, add its title
            # to the ignore list.
            ignore.append(title)
            
    # Output indices of all duplicates
    delete_index = list(set(delete_index))
    
    return(delete_index)