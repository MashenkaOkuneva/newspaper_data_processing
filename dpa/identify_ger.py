# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 11:02:45 2021

@author: mokuneva
"""

import re
from langdetect import detect_langs

def identify_ger(text):
    '''
    This function identifies if a given text is written in German and returns 
    either 1 for a German text or 0 for a non-German text. The language detection
    is based on the langdetect library, which uses a non-deterministic approach
    to assign one or multiple languages to a text and their corresponding
    probabilities.
    
    Due to the probabilistic nature of the algorithm, determine the language three times
    and calculate the average probability that the language is German. If the 
    probability is above the threshold value, the text is classified as German.
    '''

    tr = 0.9
    
    # We remove '# dpa-Notizblock' from the text before the language identification
    # because 'Notizblock' may contain infromation in English that will
    # be deleted in the last pre-processing step.
    text = re.sub('# dpa-Notizblock.{20,}','',text)
    
    prob_ger = 0
    n = 0
    
    # Identify the language three times
    for i in range(3):
        ident = detect_langs(text)
        # Save probability of the language being German
        ger_found = [lang for lang in ident if lang.lang == 'de']
        if len(ger_found) != 0:
            prob_ger += ger_found[0].prob
            n += 1
            
    # If German was detected at least once, calculate the average probability that
    # the language is German        
    if n!=0:
        prob_ger = prob_ger/n
    
    # If the probability is above the threshold value, the text is classified as German
    if prob_ger < tr:
        ger = 0
    else:
        ger = 1
    
    
    return ger
        