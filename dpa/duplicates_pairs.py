# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:37:21 2022

@author: mokuneva
"""
import pandas as pd
import re

def duplicates_pairs(data):
    """ 
    This function returns the dataframe with the titles of duplicates and 
    original articles along with their publication date. By duplicate we mean 
    a summary (Zusammenfassung, Gesamtzusammenfassung, Morgenfassung), 
    overview (Überblick), repeated article (Wiederholung), or advance notification 
    (Vorausmeldung, articles about future events) that 
    has a common title with another (original) article published the same day.
    
    data is the dataframe with all the articles published on the same day as
    one of the summaries, overviews, repeated articles, or advance notifications.
    """ 
    # Publication day of the duplicate article.
    column1 = []
    # Publication month of the duplicate article.
    column2 = []
    # Publication year of the duplicate article.
    column3 = []
    # The title of the duplicate article.
    column4 = []
    # The title of the original article
    column5 = []
    
    # A dataframe with all the summaries, overviews, repeated articles, or advance 
    # notifications published on the same day.
    # We do not consider articles that contain the string 'dpa-Vorausmeldungen kompakt'
    # in the title because these articles contain multiple articles.
    types_df = data[(data.title.str.contains('Zusammenfassung|zusammenfassung|Überblick|Wiederholung|Vorausmeldung'))  & \
                 (~data.title.str.contains('dpa-Vorausmeldungen kompakt'))]
    for idx, type_title in enumerate(types_df.title):
        # Titles of all the articles published on the same day as one of the 
        # summaries, overviews, repeated articles, or advance notifications.
        for title in data.title:
            # remove the "Aktualisierung" note from the title we consider
            # (in the previous step of our analysis we might have deleted
            # the original article)
            title = re.sub('\((?:.*?)Aktualisierung(?:.*?)\)', '', title,1).strip()
            # remove the "Aktualisierung" note from the title of a summary,
            # overview, repeated article, or advance notification
            type_title  = re.sub('\((?:.*?)Aktualisierung(?:.*?)\)', '', type_title,1).strip()
            # If the title of the summary, overview, repeated article, or advance 
            # notification article contains the title we consider
            if title in type_title and title != type_title and title != '':
                column1.append(types_df.iloc[idx]['day'])
                column2.append(types_df.iloc[idx]['month'])
                column3.append(types_df.iloc[idx]['year'])
                column4.append(types_df.iloc[idx]['title'])
                column5.append(title)
            # This condition takes into account the case where the summary and overview
            # have the same title
            elif title.replace('Zusammenfassung ', '') in type_title and title != type_title and title != '':
                column1.append(types_df.iloc[idx]['day'])
                column2.append(types_df.iloc[idx]['month'])
                column3.append(types_df.iloc[idx]['year'])
                column4.append(types_df.iloc[idx]['title'])
                column5.append(title)    
    dup_df = pd.DataFrame({'day': column1,
                             'month': column2,
                             'year': column3,
                             'title_duplicate': column4,
                             'title_original': column5})
    return dup_df