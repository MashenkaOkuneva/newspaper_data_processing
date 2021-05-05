# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 22:06:27 2021

@author: Nutzer
"""

from langdetect import detect

def identify_eng(data):
    index_eng = []
    for article in data['texts']:
        if detect(article) == 'en':
            index_eng.extend(data['texts'][data['texts'] == article].index)
    return(index_eng)