# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 10:51:35 2022

@author: mOkuneva
"""

def unicode_correct(text):
    
    """This function corrects the unicode errors present in the database."""
    
    # Correct the unicode errors.
    correct_unicode_dic = {
        "Å¾": "ž",
        "Åˆ": "ň",
        "Å‚": "ł",
        "Å¯": "ů",
        "oÅ": "ō",
        "Å¼": "ż",
        "Å„": "ń",
        "Å™": "ř",
        "SinÅ iju": "Sinŭiju",
        "ShinzÅ": "Shinzō"
        }
    
    for mistake, correction in correct_unicode_dic.items():
        text = text.replace(mistake, correction)                  
    
    return(text)