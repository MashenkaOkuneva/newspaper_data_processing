# -*- coding: utf-8 -*-
"""
Created on Wed Nov  2 15:37:21 2022

@author: mokuneva
"""
import pandas as pd

def Berichtigung_pairs(inputs):
    """ 
    This function returns the dataframe with the titles of the corrected
    and original articles along with their publication date.
    
    Inputs are:
        1. Publication year of the corrected article.
        2. Publication month of the corrected article.
        3. Publication day of the corrected article.
        4. The title of the corrected article.
        5. Titles of all the articles published on the same day as the corrected article.
    """ 
    # Publication day
    column1 = []
    # Publication month
    column2 = []
    # Publication year
    column3 = []
    # The title of the corrected article
    column4 = []
    # The title of the original article
    column5 = []
    for title in inputs[4]:
        # If the title of the corrected article contains the title we consider
        if title in inputs[3] and title != inputs[3] and title != '':
            column1.append(inputs[2])
            column2.append(inputs[1])
            column3.append(inputs[0])
            column4.append(inputs[3])
            column5.append(title)
    test_df = pd.DataFrame({'day': column1,
                             'month': column2,
                             'year': column3,
                             'title_Berichtigung': column4,
                             'title_main': column5})
    return test_df