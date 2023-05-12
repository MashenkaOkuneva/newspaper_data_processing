# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 21:30:27 2023

@author: mokuneva
"""

import re

def clean_sz_articles(text):
    
    """
    This function removes information that is unlikely to be relevant for sentiment and topic
    analysis.
    """
    
    # Remove unnecessary strings from the text with the method replace
    to_replace = ['Hören Sie zu diesem Thema auch den Podcast.']
 
    for string in to_replace:    
        text = text.replace(string, ' ') 
        
    # Remove unnecessary strings from the text with regular expressions and keep
    # information about the source
    text = re.sub("""# dpa-Notizblock.{20,}""", "dpa", text)
    
    # Remove unnecessary strings from the text with regular expressions 
    text = re.sub("""(?<=\. )(?:Die wichtigsten Adressen:|Internet-Adressen:|Wichtige Adressen:)(?:.{0,})|
    |\S+\.gov\.za[^. ]*|
    |SZ-ONLINE: Alle Rechte.{0,}|
    |Alle Rechte vorbehalten.{0,}|
    |\(FOTO\: [^)]+\)|
    |\(Photo\: [^)]+\)|
    |@* *Weitere Informationen unter.{0,}|
    |@* *Weitere Informationen im Internet.{0,}|
    |@* *Weitere Informationen und Anmeldung unter.{0,}|
    |@* *Weitere Informationen zum Thema.{0,}|
    |@* *Weitere Informationen\: (?!www\.ichundmeinauto\.info).{0,}|
    |@* *Weitere Informationen gibt es unter.{0,}|
    |(?:Weitere Informationen:)(?: www\.ichundmeinauto\.info)?|
    |(?<!ein )(?<!am )(?<!per )(?<!ihr )(?<!ins )(?<!und )(?<!zum )(?<!über )(?<!aufs )(?<!nur )(?<!via )(?<!pro )(?<!oder )(?<!das )(?<!dem )(?<!Kita-)(?<!Tatwaffe )(?<!smarte )(?<!Ins )(?<!erste )(?<!normales )(?<!Service-)(?<!durchs )(?<!Beispiel )(?:Telefon|Tel\.)(?:\:[^a-zA-Z«]+)|
    |(?<!per )(?<!ein )(?<!einem )(?:Fax:[^a-zA-ZÜÄÖüäö]+)|
    |\(Seite \d{1,2}\)|
    |\({0,1}Foto: dpa\){0,1}|
    |Hier steht der Grundtext.{0,}|
    |@* *Die Langfassung dieses Interviews.{0,}|
    |Informationen zum Wettbewerb.{0,}|
    |(?:Leserfragen zu Anlagethemen bitte an(?: \@Alle bisherigen Beiträge unter(?= Ulf-Eike| Andreas| Leserfrage)?| oder per Fax 089 \/ 21 83 - 86 60)?)""", " ", text)
    
    # The addresses/Internet addresses: (?<=\. )(?:Die wichtigsten Adressen:|Internet-Adressen:|Wichtige Adressen:)(?:.{0,})
    # websites: \S+\.gov\.za[^. ]*
    # copyright information: SZ-ONLINE: Alle Rechte.{0,}
    #                        Alle Rechte vorbehalten.{0,}
    # reference to the photo source: \(FOTO\: [^)]+\)
    #                                \(Photo\: [^)]+\)
    #                                \({0,1}Foto: dpa\){0,1}
    # reference to additional information: @* *Weitere Informationen unter.{0,}
    #                                      @* *Weitere Informationen im Internet.{0,}
    #                                      @* *Weitere Informationen und Anmeldung unter.{0,}
    #                                      @* *Weitere Informationen zum Thema.{0,}
    #                                      @* *Weitere Informationen\: (?!www\.ichundmeinauto\.info).{0,}
    #                                      @* *Weitere Informationen gibt es unter.{0,}
    #                                      (?:Weitere Informationen:)(?: www\.ichundmeinauto\.info)?
    #                                      Informationen zum Wettbewerb.{0,}
    # telephone and fax numbers:           (?<!ein )(?<!am )(?<!per )(?<!ihr )(?<!ins )(?<!und )(?<!zum )(?<!über )(?<!aufs )(?<!nur )(?<!via )(?<!pro )(?<!oder )(?<!das )(?<!dem )(?<!Kita-)(?<!Tatwaffe )(?<!smarte )(?<!Ins )(?<!erste )(?<!normales )(?<!Service-)(?<!durchs )(?<!Beispiel )(?:Telefon|Tel\.)(?:\:[^a-zA-Z«]+) 
    #                                      (?<!per )(?<!ein )(?<!einem )(?:Fax:[^a-zA-ZÜÄÖüäö]+)
    # reference to the page:               \(Seite \d{1,2}\)
    # this text contains a sentence that is repeated 96 times: Hier steht der Grundtext.{0,}
    # reference to an extended version of an interview: @* *Die Langfassung dieses Interviews.{0,}
    # reference to contact information: (?:Leserfragen zu Anlagethemen bitte an(?: \@Alle bisherigen Beiträge unter(?= Ulf-Eike| Andreas| Leserfrage)?| oder per Fax 089 \/ 21 83 - 86 60)?)
    # reference to the podcast: Hören Sie zu diesem Thema auch den Podcast.
    return(text)