# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:02:45 2021

@author: mokuneva
"""

from langdetect import detect

eng = None

def identify_eng_2(text):
    try:
        detect(text)
        if detect(text) == 'en':
            eng = 1
        else:
            eng = 0
    except:
        eng = 2
    return eng