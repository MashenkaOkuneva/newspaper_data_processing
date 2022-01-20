# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:27 2021

@author: jbaer
"""

import re

def clean_dpa_articles(text):
    """
    Returns articles cleaned from unnecessary strings
    """

    # Remove unnecessary terms from the text
    to_replace = ['Ende der Mitteilung', 'ROUNDUP:', 
                  'Der Beitrag lag dpa in redaktioneller Fassung vor.',
                  'Bei   Rückfragen  steht  Ihnen',
                  'Weitere Informationen erhalten Sie unter:',
                  '(Der Beitrag wurde dpa vorab in redaktioneller Fassung übermittelt.)',
                  'dpa vs ot', 'dpa ds is', 'dpa as is']

    for string in to_replace:
    
        text = text.replace(string, '')

    # Remove unnecessary terms from the text with regular expressions
    text = re.sub('''<.{1,7}?>|# dpa-Notizblock.{20,}|Diese Meldung finden Sie auch unter.{10,}
    |Originaltext:.{100,}|
    |.{100,}Die gesamte korrigierte Mitteilung lautet:|Rückfragehinweis:.{10,}|
    |dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.{10,}|
    |Die englische Originalmeldung finden Sie unter.{10}|
    |Datum der Analyse.{5,}|
    |Für weitere Informationen wenden Sie sich bitte an:.{10,}|
    |dpa-AFX Broker - die Trader News von dpa-AFX.*|
    |OTS:.{5,}|Debitos GmbH newsroom:.{5,}|
    |.{20,}Inhalt der Mitteilung ist der Emittent verantwortlich.|
    |/[a-zA-Z]{2,3}|Von \w{1,20} \w{1,20}, dpa-AFX|
    |Achtung:Zusammenfassung bis.{5,}''', '', text)
    
    # stock symbols: - '<.{1,7}?>'
    # additional information meant for the author: - '# dpa-Notizblock.*'
    # previous article: - '.*(FORTSETZUNG) - '
    # reference to dpa webpage: - 'Diese Meldung finden Sie auch unter.*'
    # uncorrected original article: - 'Originaltext:.*|.*Die gesamte korrigierte Mitteilung lautet:'
    # inquiry note: - ' Rückfragehinweis:.*'
    # reference to dpa-AFX webpage: - 'dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.*'
    # reference to article in english: Die englische Originalmeldung finden Sie unter.*
    # date of the article: Datum der Analyse.*
    # reference for aditional information: Für weitere Informationen wenden Sie sich bitte an:.*
    # reference to afx webpage: Bei   Rückfragen  steht  Ihnen|dpa-AFX Broker - die Trader News von dpa-AFX.*
    # reference to sender: OTS:.*
    # reference to Debitos: Debitos GmbH newsroom:.*
    # reference to issuer :.*Inhalt der Mitteilung ist der Emittent verantwortlich.
    # reference to authors: /[a-zA-Z]{2,3}|Von \w+ \w+, dpa-AFX
    # links and Emails: www\..*?\.com|http:.*?\.png|Email:.*?\.com
    # reference to summary: Achtung:Zusammenfassung bis.*
    # (Der Beitrag wurde dpa vorab in redaktioneller Fassung übermittelt.): 'The editorial version of the article was sent to dpa in advance.'

    return(text)