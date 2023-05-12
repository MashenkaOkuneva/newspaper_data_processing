# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 16:35:29 2022

@author: mOkuneva
"""

import re

def clean_hb_articles(text):
    
    """
    This function removes information that is unlikely to be relevant for sentiment and topic
    analysis.
    """

    # Remove unnecessary strings from the text with the method replace
    to_replace = ['Weitere Informationen über die Aktivitäten der Allianz gibt es im Internet unter',
                  'Weitere Informationen und Internetadressen unter Anlegerprofil.']
    # 'Weitere Informationen über die Aktivitäten der Allianz gibt es im Internet unter':
    #  exception from the rule to delete everything after 'Weitere Informationen über'
    # 'Weitere Informationen und Internetadressen unter Anlegerprofil.':
    #  exception from the rule to delete everything after 'Weitere Informationen und'   

    for string in to_replace:    
        text = text.replace(string, ' ')
        
        
    # Remove unnecessary terms from the text with regular expressions and keep
    # information about the source
    text = re.sub("""# dpa-Notizblock.{20,}""", " dpa", text)
    
    # Remove unnecessary terms from the text with regular expressions 
    # including groups
    text = re.sub("""(Special[. ]*)?(\(*@*-* *Weitere Informationen zum Thema.{0,})|
    |(Special[. ]*)(\(*@*-* *Weitere Informationen über.{0,})|
    |(@*-* *Weitere Informationen\.? zu)(?! den neuen Indizes)(.{0,})|
    |(Weitere Informationen gibt)(?! es nicht bis Mittwoch| es auf Knopfdruck)(.{0,})|
    |(Weitere Informationen über)(?! die aktuelle| die Zukunft| die Gespräche)(.{0,})|
    |(@*-* *Weitere Informationen)(.{0,})(siehe auch unter)|
    |(@?Weitere Informationen sowie)(?! eine begründete Erklärung)(.{0,})|
    |(?<!mannshohen weißen )(?<!siehe )(?<!Mark )(?<!siehe auch )(?<!im )(?<!Familienfirmen bisweilen agieren können. )(Kasten:)(?! Fortsetzung| Stifter, Spender| Zehn Lehren aus| Das Wunder von Detroit| Machtpoker um Schloss| Aufstieg und Fall des Drogeriekönigs)(.{0,})|
    |(?<=\.)([a-zA-Z ]*)(Adressen:)(?! Japans Mitsubishi| Die abgewählten| Intel ist Marktführer| Berlin und Paris)(.{0,})|
    |(FAKTEN UND |WEB-|MAIL-|WEITERE |INTERNET-|SERVICE & |BESCHWERDE|NÜTZLICHE |WICHTIGE |SILVESTER-)?(ADRESSEN)(?!. Teurer Markenschutz)(.{0,})|
    |(Bestellung von )?(Sonderseiten zum Thema.{0,})|
    |(Service & )(Adressen\..{0,})|
    |(Ort:.{0,})(Veranstalter:|Öffnungszeiten:)(.{0,})""", " ", text)
    
    # Remove unnecessary terms from the text with regular expressions that do
    # not include groups
    text = re.sub("""@* *Weitere Informationen zu diesem Thema.{1,}|
    |@*-* *Weitere Informationen erhalten Sie unter.{0,}|
    |@*-* *Weitere Informationen erhalten Sie beim.{0,}|
    |\(*@*-* *Weitere Informationen:.{0,}|
    |Weitere Informationen durch.{0,}|
    |Weitere Auskünfte unter.{0,}|
    |Weitere Auskünfte bei.{0,}|
    |Weitere Informationen\.? unter.{0,}|
    |Weitere Informationen bei.{0,}|
    |Weitere Informationen bietet das Buch.{0,}|
    |Weitere Informationen bietet hierzu.{0,}|
    |@?Weitere Informationen bieten.{0,}|
    |@?Weitere Informationen können.{0,}|
    |Weitere Informationen\.? im.{0,}|
    |Weitere Informationen auch.{0,}|
    |Weitere Informationen für.{0,}|
    |Weitere Informationen enthält.{0,}|
    |Weitere Informationen hält die Deutsche Messe.{0,}|
    |Weitere Informationen sind erhältlich.{0,}|
    |Weitere Informationen sind abzurufen.{0,}|
    |Weitere Informationen siehe unter.{0,}|
    |@?Weitere Informationen und.{0,}|
    |Weitere Informationen auf.{0,}|
    |@?Weitere Informationen\.? finden.{0,}|
    |@?Weitere Informationen kann.{0,}|
    |@?Weitere Informationen$|
    |@?Weitere Informationen von.{0,}|
    |@?Weitere Informationen rund um.{0,}|
    |@ ?Weitere Informationen lesen Sie unter:?|
    |@Weitere Informationen, Umfragen.{0,}|
    |Weitere Informationen in.{0,}|
    |Weitere Informationen stehen.{0,}|
    |Weitere Informationen, insbesondere.{0,}|
    |Weitere Informationen sind abrufbar.{0,}|
    |Weitere Informationen sind auf.{0,}|
    |@?Weitere Informationen Unter.{0,}|
    |PANORAMA\..{0,}|
    |HANDELSBLATT-EUROKONJUNKTUR-INDIKATOR\..{0,}|
    |EUROKONJUNKTUR-INDIKATOR KOMPAKT\..{0,}|
    |LINK INS INTERNET.{0,}|
    |HANDELSBLATT - ANLEGERSPIEL.{0,}|
    |DIE FINANZZEITUNG NUTZEN.{0,}|
    |UR - UND ERSTAUFFÜHRUNGEN.{0,}|
    |Messen, Kongresse, Seminare.{0,}|
    |Messen, Kongresse, Events, Seminare.{0,}|
    |Das Herbst-Programm.{0,}""", " ", text)
    
    # Additional information meant for the author: "# dpa-Notizblock.{20,}"
    # the list of articles on a particular topic: "(Special[. ]*)?(\(*@*-* *Weitere Informationen zum Thema.{0,})"
    #                                             "(Special[. ]*)(\(*@*-* *Weitere Informationen über.{0,})"
    # reference to additional information: "(@*-* *Weitere Informationen\.? zu)(?! den neuen Indizes)(.{0,})"
    #                                      "(Weitere Informationen gibt)(?! es nicht bis Mittwoch| es auf Knopfdruck)(.{0,})"
    #                                      "(Weitere Informationen über)(?! die aktuelle| die Zukunft| die Gespräche)(.{0,})"
    #                                      "(@*-* *Weitere Informationen)(.{0,})(siehe auch unter)"  
    #                                      "(@?Weitere Informationen sowie)(?! eine begründete Erklärung)(.{0,})"
    #                                      "@* *Weitere Informationen zu diesem Thema.{1,}"
    #                                      "@*-* *Weitere Informationen erhalten Sie unter.{0,}"
    #                                      "@*-* *Weitere Informationen erhalten Sie beim.{0,}"
    #                                      "\(*@*-* *Weitere Informationen:.{0,}"
    #                                      "Weitere Informationen durch.{0,}"
    #                                      "Weitere Auskünfte unter.{0,}"
    #                                      "Weitere Auskünfte bei.{0,}"
    #                                      "Weitere Informationen\.? unter.{0,}"
    #                                      "Weitere Informationen bei.{0,}"
    #                                      "Weitere Informationen bietet das Buch.{0,}"
    #                                      "Weitere Informationen bietet hierzu.{0,}"
    #                                      "@?Weitere Informationen bieten.{0,}"
    #                                      "Weitere Informationen können.{0,}"
    #                                      "Weitere Informationen\.? im.{0,}"
    #                                      "Weitere Informationen auch.{0,}"
    #                                      "Weitere Informationen für.{0,}"
    #                                      "Weitere Informationen enthält.{0,}"
    #                                      "Weitere Informationen hält die Deutsche Messe.{0,}"
    #                                      "Weitere Informationen sind erhältlich.{0,}"
    #                                      "Weitere Informationen sind abzurufen.{0,}"
    #                                      "Weitere Informationen siehe unter.{0,}"
    #                                      "@?Weitere Informationen und.{0,}"
    #                                      "Weitere Informationen auf.{0,}"
    #                                      "@?Weitere Informationen\.? finden.{0,}"
    #                                      "@?Weitere Informationen kann.{0,}"
    #                                      "@?Weitere Informationen$"
    #                                      "@?Weitere Informationen von.{0,}"
    #                                      "@?Weitere Informationen rund um.{0,}"
    #                                      "@ ?Weitere Informationen lesen Sie unter:?"
    #                                      "@Weitere Informationen, Umfragen.{0,}"
    #                                      "Weitere Informationen in.{0,}"
    #                                      "Weitere Informationen stehen.{0,}"
    #                                      "Weitere Informationen, insbesondere.{0,}"
    #                                      "Weitere Informationen sind abrufbar.{0,}"
    #                                      "Weitere Informationen sind auf.{0,}"
    #                                      "@?Weitere Informationen Unter.{0,}"
    # the calendar of events: "PANORAMA\..{0,}"
    # the composition of an index: "HANDELSBLATT-EUROKONJUNKTUR-INDIKATOR\..{0,}"
    #                              "EUROKONJUNKTUR-INDIKATOR KOMPAKT\..{0,}"
    # the box with additional information on the topic: "(?<!mannshohen weißen )(?<!siehe )(?<!Mark )(?<!siehe auch )(?<!im )(?<!Familienfirmen bisweilen agieren können. )(Kasten:)(?! Fortsetzung| Stifter, Spender| Zehn Lehren aus| Das Wunder von Detroit| Machtpoker um Schloss| Aufstieg und Fall des Drogeriekönigs)(.{0,})"
    # the addresses/Internet addresses: "(?<=\.)([a-zA-Z ]*)(Adressen:)(?! Japans Mitsubishi| Die abgewählten| Intel ist Marktführer| Berlin und Paris)(.{0,})"
    #                                 : "(FAKTEN UND |WEB-|MAIL-|WEITERE |INTERNET-|SERVICE & |BESCHWERDE|NÜTZLICHE |WICHTIGE |SILVESTER-)?(ADRESSEN)(?!. Teurer Markenschutz)(.{0,})"
    #                                 : "(Service & )(Adressen\..{0,})"
    # the links: "LINK INS INTERNET.{0,}"
    # the word game for investors: "HANDELSBLATT - ANLEGERSPIEL.{0,}"
    # information on how special pages on the topic can be ordered: "(Bestellung von )?(Sonderseiten zum Thema.{0,})"
    # educational articles on how to understand financial news: "DIE FINANZZEITUNG NUTZEN.{0,}"
    # announcement of premieres: "UR - UND ERSTAUFFÜHRUNGEN.{0,}"
    # announcement of trade fairs: "Messen, Kongresse, Seminare.{0,}"
    #                            : "Messen, Kongresse, Events, Seminare.{0,}"
    # announcement of events: "Das Herbst-Programm.{0,}"
    # place and time/organizer of the event: "(Ort:.{0,})(Veranstalter:|Öffnungszeiten:)(.{0,})"
    return(text)