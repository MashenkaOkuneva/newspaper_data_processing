# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:58:56 2022

@author: mOkuneva
"""

import re

def find_strings_re(text):
    #pat = """[A-ZÄÖÜß:-]{2,}(?:\s+[A-ZÄÖÜß:\-]+)+.{30,}?(?:\s{2,}|$)"""
    #pat = """[A-ZÄÖÜß]{5,}"""
    pat = r'\(dpa.*?\)'
    #return re.findall(pat, text)
    if len(re.findall(pat, text))>1:
        return('yes')
    else:
        return('no')