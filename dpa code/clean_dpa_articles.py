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
    |(?:#{0,2}\s{0,2}(?:dpa){0,1}-{0,1}\s{0,1}[Nn]otizblock ){0,1}(?:## Internet.{0,})|
    |# Notizblock.{0,}|
    |# dpa-notizblock.{0,}|              
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
    |\(Achtung: Zusammenfassung (?:mit|bis).{2,}|
    |\(Achtung: Sie erhalten eine Zusammenfassung\).{0,}|   
    |\(Achtung: Folgt Zusammenfassung.{2,}|
    |\(Achtung: Folgt weitere Zusammenfassung.{2,}|
    |VWD/ap-dj.{0,}|
    |VWD/\d{2}.{0,}|
    |vwd/dj.{0,}|
    |vwd/\d{2}.{0,}|
    |vwd//.{0,}|
    |vwd/ap-dj.{0,}|
    |(?:\(Az\:)(?:[^)]{1,})(?:(?<!Bundeskriminalamts \(BKA)\))|
    |(?:\(Az\: 1 BvR 370/07)(?=\. Das Gericht erklärte)|
    |(?:\(Az\.\:)(?:[^)]{1,})(?:\))|
    |dpa hb.{0,}|
    |(?:dpa eh)(?!er)(?:.{0,})|
    |dpa bg.{0,}|
    |(?:\(A c h t u n g\:)(?:.{0,})(?:Januar 2230\))|
    |(?:A c h t u n g\:)(?:.{0,})(?:28\.4\. 2130)|
    |(?:A c h t u n g\:)(?:.{0,})(?:zu \«Mehmet\»\.|zu Koalition\.)|
    |(?:A c h t u n g\:)(?:.{0,})(?:Neufassung\:)|
    |\({0,1}A c h t u n g\:.{0,}|
    |dpa hh.{0,}|
    |(?:\(Wiederholung[^)]+?)(?:[^)]{1,})(?:Aktenzeichen\:[^)]+?\))|
    |(?:\(OLG Koblenz)(?:[^)]{1,})(?:\))|
    |(?:\(LG München)(?:[^)]{1,})(?:\))|
    |(?:\(Beschluss vom[^)]+?)(?:[^)]{1,})(?:Aktenzeichen:[^)]+?\)\.)|
    |(?:Das Urteil vom)(?:[^)]{1,})(?:Aktenzeichen:.+?\.)|
    |(?:\: \(Aktenzeichen\:)(?:[^)]+?)(?:\.\.\.)|
    |(?:\(\s{0,1}Aktenzeichen\:)(?:[^)]{1,})(?:\))|
    |(?:Aktenzeichen\:)(?:.{0,})(?=Nach dem Zivilrecht)|
    |(?:- Aktenzeichen\:)(?:.{0,})(?:\d{4}\.)|
    |(?<!«)(?<!ZDF-Magazin )Aktenzeichen\:.{0,}|
    |(?:\(\s{0,1}Achtung\:)(?:[^)]{1,})(?:\))|
    |(?:\(\s{0,1}URL\:)(?:[^)]{1,})(?:\))|
    |(?:\(\s{0,1}Internet\:)(?:[^)]{1,})(?:\))|  
    |dpa wj.{0,}|
    |dpa pf.{0,}|
    |dpa dk.{0,}|
    |(?:dpa rt kb)(?:.{0,})(?:Debatte sechs)|
    |(?:dpa ke kb)(?:.{0,})(?:Debatte zwei)|
    |(?: [Ff]olgt [Dd]ebatte )(?:zwei |drei |vier |fünf |sechs |sieben |acht |neun |zehn |elf |zwölf |13 |14 |15 |16 |17 |18 )(?:und Schluß ){0,1}(?:\(Solms\) ){0,1}(?:dpa ku|dpa ke|dpa dr|dpa js|dpa rf|dpa rt|dpa he|dpa hö|dpa rx|dpa hs|dpa wb|dpa li|dpa sm|dpa ta|dpa ct)(?:.+?)(?<!\(Berichtigung - )(?:Debatte |Deabtte )(?:zwei |drei |vier |fünf |sechs |sieben |acht |neun |zehn |elf |zwölf |13 |14 |15 |16 |17 |18 )(?:und Schluß){0,1}|
    |dpa ku(?!rz|rsiert).{0,}|
    |(?:\(\s{0,1}Rechtssachen)(?:[^)]{1,})(?:\))|
    |dpa bb.{0,}|
    |(?:\(\s{0,1}Der Beitrag)(?:[^)]{1,})(?:\))''', '', text)
    
    ### List with explanation for each removed string: ###
    # Stock symbols:                                       <.{1,15}?>
    #                                                      <[A-Z]{2}[0-9]+>  
    # Additional information meant for the author:         # dpa-Notizblock.{20,} 
    #                                                      (?:#{0,2}\s{0,2}(?:dpa){0,1}-{0,1}\s{0,1}[Nn]otizblock ){0,1}(?:## Internet.{0,})
    #                                                      # Notizblock.{0,}
    #                                                      # dpa-notizblock.{0,}
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
    #                                                      \(Achtung: Zusammenfassung (?:mit|bis).{2,}
    #                                                      \(Achtung: Folgt weitere Zusammenfassung.{2,}
    #                                                      \(Achtung: Sie erhalten eine Zusammenfassung\).{0,}
    # Reference to a news agency:                          VWD/ap-dj.{0,}
    #                                                      VWD/\d{2}.{0,}
    #                                                      vwd/dj.{0,}
    #                                                      vwd/\d{2}.{0,}
    #                                                      vwd//.{0,}
    #                                                      vwd/ap-dj.{0,}
    #                                                      dpa hb.{0,}
    #                                                      (?:dpa eh)(?!er)(?:.{0,})
    #                                                      dpa bg.{0,}
    #                                                      dpa hh.{0,}
    #                                                      dpa wj.{0,}
    #                                                      dpa pf.{0,}
    #                                                      dpa dk.{0,}
    #                                                      dpa ku(?!rz|rsiert).{0,}
    #                                                      dpa bb.{0,}
    # Reference to the case number at the court:           (?:\(Az\:)(?:[^)]{1,})(?:(?<!Bundeskriminalamts \(BKA)\))
    #                                                      (?:\(Az\: 1 BvR 370/07)(?=\. Das Gericht erklärte)
    #                                                      (?:\(Wiederholung[^)]+?)(?:[^)]{1,})(?:Aktenzeichen\:[^)]+?\))
    #                                                      (?:\(OLG Koblenz)(?:[^)]{1,})(?:\))
    #                                                      (?:\(LG München)(?:[^)]{1,})(?:\))
    #                                                      (?:\(Beschluss vom[^)]+?)(?:[^)]{1,})(?:Aktenzeichen:[^)]+?\)\.)
    #                                                      (?:Das Urteil vom)(?:[^)]{1,})(?:Aktenzeichen:.+?\.)
    #                                                      (?:\: \(Aktenzeichen\:)(?:[^)]+?)(?:\.\.\.) 
    #                                                      (?:\(\s{0,1}Aktenzeichen\:)(?:[^)]{1,})(?:\))
    #                                                      (?:Aktenzeichen\:)(?:.{0,})(?=Nach dem Zivilrecht)
    #                                                      (?:- Aktenzeichen\:)(?:.{0,})(?:\d{4}\.)
    #                                                      (?<!«)(?<!ZDF-Magazin )Aktenzeichen\:.{0,}
    #                                                      (?:\(Az\.\:)(?:[^)]{1,})(?:\))
    # Reference to additional information:                 (?:\(A c h t u n g\:)(?:.{0,})(?:Januar 2230\))
    #                                                      (?:A c h t u n g\:)(?:.{0,})(?:28\.4\. 2130)
    #                                                      (?:A c h t u n g\:)(?:.{0,})(?:zu \«Mehmet\»\.|zu Koalition\.)
    #                                                      (?:A c h t u n g\:)(?:.{0,})(?:Neufassung\:)
    #                                                      \({0,1}A c h t u n g\:.{0,}
    #                                                      (?:\(\s{0,1}Achtung\:)(?:[^)]{1,})(?:\))
    #                                                      (?:\(\s{0,1}Der Beitrag)(?:[^)]{1,})(?:\))
    # Reference to the website:                            (?:\(\s{0,1}URL\:)(?:[^)]{1,})(?:\))
    #                                                      (?:\(\s{0,1}Internet\:)(?:[^)]{1,})(?:\))
    # Reference to internal notes separating several
    # parts of the article:
    #                                                      (?:dpa rt kb)(?:.{0,})(?:Debatte sechs)
    #                                                      (?:dpa ke kb)(?:.{0,})(?:Debatte zwei)
    #                                                      (?: [Ff]olgt [Dd]ebatte )(?:zwei |drei |vier |fünf |sechs |sieben |acht |neun |zehn |elf |zwölf |13 |14 |15 |16 |17 |18 )(?:und Schluß ){0,1}(?:\(Solms\) ){0,1}(?:dpa ku|dpa ke|dpa dr|dpa js|dpa rf|dpa rt|dpa he|dpa hö|dpa rx|dpa hs|dpa wb|dpa li|dpa sm|dpa ta|dpa ct)(?:.+?)(?<!\(Berichtigung - )(?:Debatte |Deabtte )(?:zwei |drei |vier |fünf |sechs |sieben |acht |neun |zehn |elf |zwölf |13 |14 |15 |16 |17 |18 )(?:und Schluß){0,1}
    # Reference to a legal case:
    #                                                      (?:\(\s{0,1}Rechtssachen)(?:[^)]{1,})(?:\))    
    return(text)