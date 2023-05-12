# -*- coding: utf-8 -*-
"""
Created on Wed Apr 12 19:03:01 2023

@author: mokuneva
"""

import nltk

def text_tok(text):
    '''This function tokenizes text after replacing umlauts.'''
    
    def replace_umlauts(text):
        """This function replaces German umlauts with their respective substitutes."""
        replacements = {
            u'ä': u'ae',
            u'ö': u'oe',
            u'ü': u'ue',
            u'Ä': u'AE',
            u'Ö': u'OE',
            u'Ü': u'UE',
            u'ß': u'ss'
        }
        for umlaut, substitute in replacements.items():
            text = text.replace(umlaut, substitute)
        return text
    
    text = replace_umlauts(text)
    
    return(nltk.word_tokenize(text))

    