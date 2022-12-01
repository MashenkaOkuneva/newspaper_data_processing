# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:02:45 2021

@author: mokuneva
"""

from langdetect import detect_langs

def identify_ger(text):
    '''
    This function identifies if a given text is written in German and returns 
    either 1 for a German text or 0 for a non-German text. The language detection
    is based on the langdetect library, which uses a non-deterministic approach
    to assign one or multiple languages to a text and their corresponding
    probabilities.
    
    If more than one language is detected, check if the language with the
    highest probability is German and if the probability is above the threshold value.
    Otherwise, the text is classified as non-German.
    '''

    tr = 0.9
    
    ident = detect_langs(text)
    
    if len(ident) > 1:     
        
        unclear_ger = [lang for lang in ident if lang.lang == 'de']
        
        if len(unclear_ger) == 0:
            
            ger = 0
            
        else:
            
            if unclear_ger[0].prob < tr:
                
                ger = 0
                
            else:
                
                ger = 1
                
    else:
        
        if ident[0].lang == 'de':
            
            ger = 1
            
        else:
            
            ger = 0
            
    return ger
        