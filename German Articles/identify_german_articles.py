# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 18:23:06 2022

@author: jbaer
"""

def identify_german_articles(lemmas, german_list, country_and_capital_list):
    
    idx_non_german = [idx for idx, article in enumerate(lemmas) if (any(word in article for word in country_and_capital_list) and not any(word in article for word in german_list))]
    
    return(idx_non_german)