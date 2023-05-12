# -*- coding: utf-8 -*-
"""
Created on Tue May  9 13:28:40 2023

@author: mokuneva
"""

import re

def clean_welt_articles(text):
    
    """
    This function removes information that is unlikely to be relevant for sentiment and topic
    analysis.
    """
        
    # Remove unnecessary strings from the text with regular expressions 
    text = re.sub("""(?<=\. )(?:Internet-Adressen:)(?:.{0,})|
    |Weitere Informationen unter.{0,}|
    |Weitere Informationen im Internet.{0,}|
    |Weitere Informationen zum Thema.{0,}|
    |Weitere Informationen\: (?!Bauernland Bayern|IT-Standort Nummer eins|Privatisierungserlöse wurden|Privatisierungserlöse|Die Messe|Fehlanzeige).{0,}|
    |Weitere Informationen gibt es unter (?!Wer).{0,}|
    |Weitere Informationen gibt es unter|
    |(?<!Festnetz-)(?<!IP-)(?<!als )(?<!am )(?<!per )(?<!dem )(?<!zum )(?<!das )(?<!ihr )(?<!oder )(?:Telefon|Tel\.)(?:\: Die kostenlose Aktionstelefonnummer lautet|\: Die Gratis-Aktionstelefonnummer lautet)(?: [^a-zA-Z«]+)|
    |(?<!Festnetz-)(?<!IP-)(?<!am )(?<!als )(?<!per )(?<!dem )(?<!zum )(?<!das )(?<!ihr )(?<!oder )(?:Telefon|Tel\.)(?<!per )(?:\:[^a-zA-Z«]+)|
    |(?<!per )(?<!ein )(?<!einem )(?<!beim )(?:Fax: Siekönnen Ihre Anmeldung oder Ihre Depotunterlagen auch per Fax senden:|Fax: Sie können Ihre Anmeldung oder Ihre Depotunterlagen auch per Fax an die DAB Bank senden:)(?:[^a-zA-ZÜÄÖüäö]+)|
    |(?<!per )(?<!ein )(?<!einem )(?<!beim )(?:Fax:[^a-zA-ZÜÄÖüäö]+)|
    |\(Seite \d{1,2}\)|
    |\({0,1}Foto: dpa\){0,1}|
    |Bestellen Sie jetzt das neue Gabler-Wirtschaftslexikon.{0,}|
    |(?:fotos:.{0,})(?=Nummer eins bei Nahrungsmitteln|Jeanette Biedermann|Die meisten Fernseher)|
    |fotos:.{0,}|
    |(?:Fotos:.{0,})(?=Michael Frenzel|Die meisten Experten|Der Marathonläufer|Patienten müssen|\"Work Hard\"|Künstler und Politiker|Ein Provokateur|Das Maß für Qualität|Backwerk im Namen|Der Unternehmer|Denkmäler|Der Berg ruft|Das Kaffee-Buch|Nach Delaware|\"Boom\, Boom\, Boom\"|Confindustria|Der 64|Constantin-Chef Fred|Philip Bowman|Der Manager|Barbesucherin|Gary Becker wurde|Ex-Filmhändler|Sandford \"Sandy\"|Preisgekrönt|Jörg Muchametow|Kaum ein Konzern|Der chinesische Markt)|
    |Fotos:.{0,}""", " ", text)
    
    
    # Remove photo source references and photo descriptions,
    # but only if the text following "Foto:" or "FOTO:" consists of 30 words or fewer.
    photo_matches = re.findall(r'Foto:.{0,}|FOTO:.{0,}', text)

    filtered_matches = [match for match in photo_matches if len(match.split(' ')) <= 30]
    
    for match in filtered_matches:
        text = re.sub("""Foto:.{0,}|FOTO:.{0,}""", " ", text)

    
    # Internet addresses: (?<=\. )(?:Internet-Adressen:)(?:.{0,})
    # reference to the photo source: \({0,1}Foto: dpa\){0,1}
    #                                (?:fotos:.{0,})(?=Nummer eins bei Nahrungsmitteln|Jeanette Biedermann|Die meisten Fernseher)
    #                                fotos:.{0,}
    #                                (?:Fotos:.{0,})(?=Michael Frenzel|Die meisten Experten|Der Marathonläufer|Patienten müssen|\"Work Hard\"|Künstler und Politiker|Ein Provokateur|Das Maß für Qualität|Backwerk im Namen|Der Unternehmer|Denkmäler|Der Berg ruft|Das Kaffee-Buch|Nach Delaware|\"Boom\, Boom\, Boom\"|Confindustria|Der 64|Constantin-Chef Fred|Philip Bowman|Der Manager|Barbesucherin|Gary Becker wurde|Ex-Filmhändler|Sandford \"Sandy\"|Preisgekrönt|Jörg Muchametow|Kaum ein Konzern|Der chinesische Markt)
    #                                Fotos:.{0,} 
    #                                Foto:.{0,}
    #                                FOTO:.{0,}
    # reference to additional information: Weitere Informationen unter.{0,}
    #                                      Weitere Informationen im Internet.{0,}
    #                                      Weitere Informationen zum Thema.{0,}
    #                                      Weitere Informationen\: (?!Bauernland Bayern|IT-Standort Nummer eins|Privatisierungserlöse wurden|Privatisierungserlöse|Die Messe|Fehlanzeige).{0,}
    #                                      Weitere Informationen gibt es unter (?!Wer).{0,}
    #                                      Weitere Informationen gibt es unter
    # telephone and fax numbers:           (?<!Festnetz-)(?<!IP-)(?<!als )(?<!am )(?<!per )(?<!dem )(?<!zum )(?<!das )(?<!ihr )(?<!oder )(?:Telefon|Tel\.)(?:\: Die kostenlose Aktionstelefonnummer lautet|\: Die Gratis-Aktionstelefonnummer lautet)(?: [^a-zA-Z«]+) 
    #                                      (?<!Festnetz-)(?<!IP-)(?<!am )(?<!als )(?<!per )(?<!dem )(?<!zum )(?<!das )(?<!ihr )(?<!oder )(?:Telefon|Tel\.)(?<!per )(?:\:[^a-zA-Z«]+)
    #                                      (?<!per )(?<!ein )(?<!einem )(?<!beim )(?:Fax: Siekönnen Ihre Anmeldung oder Ihre Depotunterlagen auch per Fax senden:|Fax: Sie können Ihre Anmeldung oder Ihre Depotunterlagen auch per Fax an die DAB Bank senden:)(?:[^a-zA-ZÜÄÖüäö]+)
    #                                      (?<!per )(?<!ein )(?<!einem )(?<!beim )(?:Fax:[^a-zA-ZÜÄÖüäö]+)
    # reference to the page:               \(Seite \d{1,2}\)
    # advertisement for the new Gabler-Wirtschaftslexikon: Bestellen Sie jetzt das neue Gabler-Wirtschaftslexikon.{0,}
    
    return(text)