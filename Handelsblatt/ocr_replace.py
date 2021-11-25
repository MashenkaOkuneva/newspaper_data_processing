# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 15:55:08 2021

@author: mokuneva
"""

import re

def ocr_replace(text):
    
    # empty dictionary for tokens I want to change
    replace_dic = dict()
    
    # example: ' 1OO'
    pat1 = r"(\s[1-9]+)([O]+\b)"
    to_replace = re.findall(pat1, text, re.I)
    
    # example: ' OOO '
    pat2 = r"(\s)(O{3,}\s)"
    to_replace += re.findall(pat2, text, re.I)
    
    # create a dictionary with confused tokens as keys and corrected tokens as items
    for rep in to_replace:
        rep_before = rep[0]+rep[1]
        replace_dic[rep_before] = rep[0] + rep[1].replace('o', '0').replace('O', '0')
    
    # replace ocr mistakes with the correct tokens
    for mistake, repl in sorted(replace_dic.items(), reverse = True):
        text = text.replace(mistake, repl)
        
    return(text)    
    
    
    