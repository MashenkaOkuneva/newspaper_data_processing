# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 11:23:20 2022

@author: mOkuneva
"""

import re

def find_umlaut(text):
    
    """This function finds the words like '}ber' and 'gel|st'.
    We use the output to drop the texts with broken umlauts and
    too many mistakes."""
    
    pat1 = r'[a-zA-Z\u00C0-\u017F]*[{}][a-z\u00C0-\u017F]+'
    pat2 = r'[a-zA-Z\u00C0-\u017F]+[|][a-z\u00C0-\u017F]+\b'  
            
    return re.findall(pat1, text) + re.findall(pat2, text)