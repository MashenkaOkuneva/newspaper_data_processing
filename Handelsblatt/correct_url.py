# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:53:18 2021

@author: mokuneva
"""

# This is a function that removes URLs and html file references.

import re

def correct_url(text):
    
    # example: 'Services.html'
    text = re.sub(r'\S+\.html', ' ', text)
    
    # example: '(comdirect.de)'
    text = re.sub(r'\S+\.de\)', ' ', text)
    
    # example: 'Telefonbuch.de'
    text = re.sub(r'\S+\.de', ' ', text)
    
    # example: 'oecd.org'
    text = re.sub(r'\S+\.org', ' ', text)
    
    # example: 'bnpparibas.com/de'
    text = re.sub(r'\S+\.com\/de', ' ', text)
    
    # example: '(amazon.com )'
    text = re.sub(r'\S+\.com[ ]\)', ' ', text)    
      
    # example: '(Amazon.com)'
    text = re.sub(r'\S+\.com\)', ' ', text)
    
    # example: '"skype.com"'
    text = re.sub(r'\S+\.com\"', ' ', text)    
    
    # example: 'E-Bookers.com'
    text = re.sub(r'\S+\.com', ' ', text)
     
    # make sure that there are no extra white spaces
    text = ' '.join(text.split()) 
    
    return(text)