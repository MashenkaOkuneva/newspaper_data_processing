# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:27 2021

@author: jbaer
"""

import re

def clean_dpa_articles(text):
    """
    This function removes information that is unlikely to be relevant for sentiment and topic
    analysis.
    """

    # Remove unnecessary strings from the text with the method replace
    to_replace = ['ROUNDUP:', 
                  'Der Beitrag lag dpa in redaktioneller Fassung vor.',
                  'Bei   Rückfragen  steht  Ihnen',
                  'Weitere Informationen erhalten Sie unter:',
                  '(Der Beitrag wurde dpa vorab in redaktioneller Fassung übermittelt.)',
                  'dpa vs ot', 'dpa ds is', 'dpa as is', 'dpa cb ot', 'dpa cb ak','(...)', 
                  'dpa-AFX Broker - die Trader News im dpa-AFX ProFeed',
                  'dpa-AFX Broker - die Trader s von dpa-AFX',
                  '(Der Beitrag wurde dpa in redaktioneller Fassung übermittelt. )',
                  'NEW', 'New']

    for string in to_replace:
    
        text = text.replace(string, '')

    # Remove unnecessary strings from the text with regular expressions
    text = re.sub('''<.{1,15}?>|<[A-Z]{2}[0-9]+>|# dpa-Notizblock.{20,}|
    |Diese Meldung finden Sie auch unter.{10,}|Die englische Originalmeldung finden Sie unter.{10,}|
    |Bitte beachten Sie die englische Originalmeldung.{10,}|
    |Originaltext:.{100,}|.{100,}Die gesamte korrigierte Mitteilung lautet:|Rückfragehinweis:.{10,}|
    |dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.{10,}|
    |dpa-AFX Broker - die Trader News von dpa-AFX.{10,}|
    |dpa-AFX Broker - die Trader News von dpa-AFX.*|
    |Datum der Analyse.{5,}|
    |Für weitere Informationen wenden Sie sich bitte an:.{10,}|
    |OTS:.{5,}|Debitos GmbH newsroom:.{5,}|
    |.{20,}Inhalt der Mitteilung ist der Emittent verantwortlich.|
    |/[a-zA-Z]{2,3}|Von \w{1,20} \w{1,20}, (dpa-AFX|dpa)|
    |Achtung:Zusammenfassung bis.{5,}|
    |[-]{2,}|
    |[=]{2,}|
    |Ende der Mitteilung.{1,}|
    |(Telefon|Tel\.):[^a-zA-Z]+|
    |Fax:[^a-zA-ZÜÄÖüäö]+|
    |\+\d{2}\s[^a-zA-Z]+|
    |This announcement is distributed by.{1,}|
    |Diese Mitteilung enthält bestimmte in die Zukunft gerichtete Aussagen.{1,}|
    |Kontakt:.{2,}|
    |\(Achtung: Neue Zusammenfassung.{2,}|
    |\(Achtung: Zusammenfassung bis.{2,}|
    |\(Achtung: Folgt Zusammenfassung.{2,}|
    |\(Achtung: Folgt weitere Zusammenfassung.{2,}|''', '', text)
    
    ### List with explanation for each removed string: ###
    # Stock symbols:                                       <.{1,15}?>
    #                                                      <[A-Z]{2}[0-9]+>  
    # Additional information meant for the author:         # dpa-Notizblock.{20,}    
    # Reference to article with same text:                 Diese Meldung finden Sie auch unter.{10,}   
    # Link to the original article in English:             Bitte beachten Sie die englische Originalmeldung.{10,}
    #                                                      Die englische Originalmeldung finden Sie unter.{10,}                  
    # Uncorrected original article:                        Originaltext:.{100,}
    #                                                      .{100,}Die gesamte korrigierte Mitteilung lautet:'  
    # Inquiry note:                                        Rückfragehinweis:.{10,}  
    # Reference to other stock related articles:           dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.{10,}
    #                                                      dpa-AFX Broker - die Trader News von dpa-AFX.{10,}
    #                                                      Die englische Originalmeldung finden Sie unter folgendem Link:.{10,}  
    # Date and place of study related cited in article:    Datum der Analyse.{5,}    
    # Reference for aditional information:                 Für weitere Informationen wenden Sie sich bitte an:.{10,}  
    # Reference to sender:                                 OTS:.{5,}    
    # Reference to Debitos:                                Debitos GmbH newsroom:.{5,}    
    # Reference to issuer:                                 .{20,}Inhalt der Mitteilung ist der Emittent verantwortlich.   
    # Reference to author(s):                              /[a-zA-Z]{2,3}|Von \w{1,20} \w{1,20}, (dpa-AFX|dpa)    
    # Reference to summary:                                Achtung:Zusammenfassung bis.{5,}    
    # Unnecessary hyphens and equation signs:              [-]{2,}
    #                                                      [=]{2,}    
    # Reference to additional information:                 Ende der Mitteilung.{1,}   
    # Telefon and fax numbers:                             (Telefon|Tel\.):[^a-zA-Z]+
    #                                                      Fax:[^a-zA-ZÜÄÖüäö]+
    #                                                      \+\d{2}\s[^a-zA-Z]+   
    # Reference to distributer:                            This announcement is distributed by.{1,}  
    # Reference to additional information:                 Diese Mitteilung enthält bestimmte in die Zukunft gerichtete Aussagen.{1,}   
    # Reference to contact(s):                             Kontakt:.{2,}   
    # Reference to summary of article:                     \(Achtung: Neue Zusammenfassung.{2,}
    #                                                      \(Achtung: Zusammenfassung bis.{2,}
    #                                                      \(Achtung: Folgt Zusammenfassung.{2,}
    #                                                      \(Achtung: Folgt weitere Zusammenfassung.{2,}

    return(text)