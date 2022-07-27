# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:27 2021

@author: jbaer
"""

import re

def clean_dpa_articles(text):
    """
    This function removes all unnecessary terms like internal notes from a string.
    """

    # Remove unnecessary terms from the text
    to_replace = ['Ende der Mitteilung', 'ROUNDUP:', 
                  'Der Beitrag lag dpa in redaktioneller Fassung vor.',
                  'Bei   Rückfragen  steht  Ihnen',
                  'Weitere Informationen erhalten Sie unter:',
                  '(Der Beitrag wurde dpa vorab in redaktioneller Fassung übermittelt.)',
                  'dpa vs ot', 'dpa ds is', 'dpa as is', '(...)']

    for string in to_replace:
    
        text = text.replace(string, '')

    # Remove unnecessary terms from the text with regular expressions
    text = re.sub('''<.{1,8}?>|# dpa-Notizblock.{20,}|Diese Meldung finden Sie auch unter.{10,}
    |Originaltext:.{100,}|
    |.{100,}Die gesamte korrigierte Mitteilung lautet:|Rückfragehinweis:.{10,}|
    |dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.{10,}|
    |Die englische Originalmeldung finden Sie unter.{10,}|
    |Datum der Analyse.{5,}|
    |Für weitere Informationen wenden Sie sich bitte an:.{10,}|
    |dpa-AFX Broker - die Trader News von dpa-AFX.*|
    |OTS:.{5,}|Debitos GmbH newsroom:.{5,}|
    |.{20,}Inhalt der Mitteilung ist der Emittent verantwortlich.|
    |/[a-zA-Z]{2,3}|Von \w{1,20} \w{1,20}, dpa-AFX|
    |Achtung:Zusammenfassung bis.{5,}|
    |Bitte beachten Sie die englische Originalmeldung.{10,}|
    |[---]+''', '', text)
    
    ### List with explanation for each removed string: ###
    # Stock symbols: - '<.{1,8}?>'
    # Additional information meant for the author: - '# dpa-Notizblock.*'
    # Previous article: - '.*(FORTSETZUNG) - '
    # Reference to dpa webpage: - 'Diese Meldung finden Sie auch unter.*'
    # Uncorrected original article: - 'Originaltext:.*|.*Die gesamte korrigierte Mitteilung lautet:'
    # Inquiry note: - ' Rückfragehinweis:.*'
    # Reference to dpa-AFX webpage: - 'dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.*'
    # Reference to article in english: Die englische Originalmeldung finden Sie unter.*
    # Date of the article: Datum der Analyse.*
    # Reference for aditional information: Für weitere Informationen wenden Sie sich bitte an:.*
    # Reference to afx webpage: Bei   Rückfragen  steht  Ihnen|dpa-AFX Broker - die Trader News von dpa-AFX.*
    # Reference to sender: OTS:.*
    # Reference to Debitos: Debitos GmbH newsroom:.*
    # Reference to issuer :.*Inhalt der Mitteilung ist der Emittent verantwortlich.
    # Reference to authors: /[a-zA-Z]{2,3}|Von \w+ \w+, dpa-AFX
    # Links and Emails: www\..*?\.com|http:.*?\.png|Email:.*?\.com
    # Reference to summary: Achtung:Zusammenfassung bis.*
    # 'The editorial version of the article was sent to dpa in advance.':(Der Beitrag wurde dpa vorab in redaktioneller Fassung übermittelt.)
    # Link to the original article in English: Bitte beachten Sie die englische Originalmeldung.{10,}
    # Link to the original article in English: Die englische Originalmeldung finden Sie unter folgendem Link:.{10,}
    # Unnecessary strings: [---]+ 

    return(text)