# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:26:31 2021

@author: jbaer
"""
import re

def numeric_articles(text, word_count, tr = 0.75):
    
    # count numbers in text
    
    count_n = len(re.findall(r'[0-9]+\.[0-9]+|[0-9]+\,[0-9]+|[0-9]+', text))
                  
    # check if share of numbers is above threshold
    if count_n/word_count > tr:
        numeric_article = True
    else:
        numeric_article = False
    
    return numeric_article