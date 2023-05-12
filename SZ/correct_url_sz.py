# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 14:07:31 2023

@author: mokuneva
"""

import re

def correct_url_sz(text):
    
    """  
    This is a function that removes URLs, html file references, and e-mails.
    """
    
    # Define a list of patterns and their replacements
    # 1: Change "Händler.der" to "Händler. der"
    # 2: Change "{any_word}....de" to "{any_word} de"
    # 3: Change "...de" to " de"
    patterns = [
        (r'(Händler|hätten)\.(der)', r'\1. \2'),
        (r'(\w+)\.{2,}de', r'\1. de'),
        (r'\.{2,}de', r' de')
    ]

    # Apply all the patterns and their replacements to the text
    for pattern, replacement in patterns:
        text = re.sub(pattern, replacement, text)
          
    exceptions = {'tagesschau.de', 'Web.de', 'web.de', 'freenet.de', 'Booking.com', 'Siegelklarheit.de',
                  'handwerk.de', 'Handwerk.de', 'downdetector.com', 'allestörungen.de', 'Netzpolitik.org',
                  'pey.de', 'scheidung.de', 'gekündigt.de', 'flightright.de', 'Aerobuzz.de',
                  'mobile.de', 'autoscout24.de', 'buch.de', 'amazon.com', 'libri.de', 'MP3.com',
                  'manager-magazin.de', 'Liveleak.com', 'stern.de', 'faz.net', 'wikileaks.org',
                  'Bild.de', 'icasualties.org', 'Neckermann.de', 'neckermann.de',
                  'bild.de', 'Salesforce.com', 'Hotel.de', 'fluege.de', 'Check24.de',
                  'Bitcoin.de', 'bitcoin.de', 'Boo.com', 'Alibaba.com', 'Lastminute.com', 
                  'Monster.com', 'Relentless.com'}

    def replace_url(match):
        url = match.group(0)
        clean_url = url.rstrip(')').rstrip("»").lstrip("«")
        return ' ' if clean_url not in exceptions else url
        
    regex = r'''\([Ii]nternet\: [^)]+\)|
    |\(Spenden\: [^)]+\)|
    |(?:\(Adresse\: |\(Internet-Adresse\: )(?:\S+\.com)(?:[^)]*?\))|
    |\S+\.html|
    |\S+\.de[^. ]*(?:\.pdf)?|
    |\S+\.org[^. ]*|
    |\S+\.com[ ]\)|
    |\S+\.com[^. ]*|
    |\S+\.eu\.int[^. ]*|
    |\S+\.net[^. ]*|
    |\S+\.heim\.at[^. ]*'''
    
    text = re.sub(regex, replace_url, text)

    # Make sure that there are no extra white spaces
    text = ' '.join(text.split()) 
    
    return text