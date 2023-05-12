# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:42:50 2023

@author: mokuneva
"""

def umlauts_correct_sz(text):
    
    '''Replaces incorrectly encoded German umlaut characters with their correct versions in the given text.'''
    
    replacements = {
        "&auml;": "ä",
        "&uuml;": "ü",
        "&ouml;": "ö",
        "&Auml;": "Ä",
        "&Uuml;": "Ü",
        "&Ouml;": "Ö"
    }
    
    for entity, replacement in replacements.items():
        text = text.replace(entity, replacement)
    
    return text