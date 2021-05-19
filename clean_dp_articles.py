# -*- coding: utf-8 -*-
"""
Created on Wed May 19 15:22:27 2021

@author: jbaer
"""
def clean_dpa(data):

    # Remove unnecessary strings from the title and text
    data.loc[:, 'title'] = data.loc[:, 'title'].str.replace(r'(Foto - aktuell)', '')
    data.loc[:, 'texts'] = data.loc[:, 'texts'].str.replace(r'''(Wiederholung vom Wochenende)|(Wiederholung vom Vortag)|(Wiederholung vom Vorabend)|
                                              |Ad hoc-Mitteilung verarbeitet und übermittelt durch die DGAP. Für den Inhalt der Mitteilung ist der Emittent verantwortlich.|
                                              |Ende der Mitteilung|(Fortsetzung) -|ROUNDUP:
                                              |IRW-PRESS:|Der Beitrag lag dpa in redaktioneller Fassung vor.''', '')

    #  Remove unnecessary strings from the text with regular expressions
    data.loc[:, 'texts'] = data.loc[:, 'texts'].replace(to_replace='''.*\(dpa\) - | .*\(dpa/vwd\) - |.*\(dpa-AFX\) - | .*\(dpa/tk\) -|
                                          |.*\(dpa-AFX/APA\) -|.*\(euro adhoc\) -|.*\(ots\) -|.*\(dpa-AFX Broker\)|\(AFX-CH\) -|<.*?>|
                                          |# dpa-Notizblock.*|.*(FORTSETZUNG) - |Diese Meldung finden Sie auch unter.*|Originaltext:.*|
                                          |.*Die gesamte korrigierte Mitteilung lautet:|Rückfragehinweis:.*|
                                          |dpa-AFX Broker - die Trader News im dpa-AFX ProFeed.*|
                                          |Die englische Originalmeldung finden Sie unter.*|
                                          |Datum der Analyse.*|Für weitere Informationen wenden Sie sich bitte an:.*|
                                          |Weitere Informationen erhalten Sie unter:|
                                          |Bei   Rückfragen  steht  Ihnen|dpa-AFX Broker - die Trader News von dpa-AFX.*|
                                          |OTS:.*|Debitos GmbH newsroom:.*|.*Inhalt der Mitteilung ist der Emittent verantwortlich.|
                                          |/[a-zA-Z]{2,3}|Von \w+ \w+, dpa-AFX|www\..*?\.com|http:.*?\.png|Email:.*?\.com|
                                          |Achtung:Zusammenfassung bis.*''', value=r'', regex=True)

    # dpa reference: - '.*\(dpa\) - | .*\(dpa/vwd\) - |.*\(dpa-AFX\) - | .*\(dpa/tk\) - |.*\(dpa-AFX/APA\) -|.*\(euro adhoc\) -|.*\(ots\) -|.*\(dpa-AFX Broker\)
    # stock symbols: - '<.*?>'
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

    return(data)
