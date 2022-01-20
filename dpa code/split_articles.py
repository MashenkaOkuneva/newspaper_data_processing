# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:21:11 2021

@author: jbaer
"""

import re
import pandas as pd

# Define a function that splits up collections of articles into single articles
def split_articles(multiple_articles):
    """
    Returns split up articles
    """
    
    split_art =[]
    
    multiple_articles.reset_index(inplace = True, drop = True)
    
    for index, row in multiple_articles.iterrows():
        
        if row["year"] in range(2001, 2008):
            
            # check if capitlaizeted words exist in text.
            capital_words = re.findall(r'\b[A-ZÄÖÜß:\-]+\b', row["texts"])
             
            if len(capital_words) > 1:
                # split articles based on paragraphs and the occurence of uppercase
                # words (a.k.a titles)
                mult_art = re.findall(r'[A-ZÄÖÜß:-]{2,}(?:\s+[A-ZÄÖÜß:\-]+)+.{20,}?(?:\s{2,}|$)', row["texts"])    

        else:
            
            # search for dpa references
            dpa_ref = re.findall(r'\(dpa.+?\)', row["texts"])

            # if there are more than on dpa reference search for mutliple articles
            if len(dpa_ref) > 1:
                  
                # split articles based on paragraphs and the occurence of a dpa reference in each paragraph
                mult_art = re.findall(r'.{5,}?\(dpa.{50,}?(?:\s{2,}|$)', row["texts"])   
                
                # the existence  of more dpa references than number of articles indicate that we need
                # a different pattern for splitting the articles
                if len(mult_art) < len(dpa_ref):
                
                    headlines = re.findall(r'((?:^|(?<=\.))[^.]+?(?=\(dpa.+?))', row["texts"])
                    txt = row["texts"]
                    for headline in headlines:
                        txt = txt.replace(headline, 'SEP')
                    mult_art = [i.strip() for i in txt.split('SEP')][1:]
                    mult_art = [headline + art for headline, art in zip(headlines, mult_art)]
                    
            else:
                
                mult_art = re.findall(r'.+?(?:\s{2,})', row["texts"])    

        if mult_art != []:
            
            for art in mult_art:
                # Store the meta data for the article
                seperated_articles = multiple_articles.iloc[index][multiple_articles.iloc[index] != 'texts']
                # Assign the new text to the matching meta data
                seperated_articles['texts'] = art
                split_art.append(seperated_articles)
                    
            else:
                split_art.append(row) 

    return(pd.concat(split_art, axis=1).transpose())


# Easyjet-Erstflug ab Tegel - Größeres Angebot auf deutschem Markt Berlin (dpa) - Flugreisende innerhalb Deutschlands können wieder auf günstigere Ticketpreise hoffen. Mit ihrem Erstflug von Berlin-Tegel nach München hat die britische Fluggesellschaft Easyjet am Freitag den Inlandsverkehr aufgenommen. Damit bekommen der Marktführer Lufthansa und seine Billigflugtochter Eurowings mehr Wettbewerb. Mitte Dezember hatte Easyjet die in Tegel stationierten 25 Maschinen der insolventen Air Berlin übernommen einschließlich der wichtigen Start- und Landerechte. Easyjet geht an diesem Sonntag mit 15 Flugzeugen und 19 Strecken ab Tegel an den Start, wie Deutschlandchef Thomas Haagensen am Freitag ankündigte. Darunter sind die innerdeutschen Verbindungen nach Frankfurt, Stuttgart, München und Düsseldorf. Zum Ende der Sommersaison sollen es dann mehr als 40 Strecken sein. Umsätze im Einzelhandel stark gestiegen Wiesbaden/Berlin (dpa)- Im deutschen Einzelhandel sind die Umsätze im Jahr 2017 auf ein Rekordniveau gestiegen. Nach einer am Freitag veröffentlichten Schätzung des Statistischen Bundesamtes lagen die Erlöse der Händler zu aktuellen Preisen zwischen 4,5 und 4,9 Prozent über den Werten aus dem Jahr zuvor. Eine ähnlich starke Steigerung hat es in der seit 1994 vergleichbaren Statistik noch nie gegeben, wie ein Sprecher inWiesbaden mitteilte. Um die Preissteigerungen bereinigt stieg der Umsatz aber nur zwischen 2,7 und 3,1 Prozent. Hier hatte es 2015 mit einem Zuwachs von 3,8 Prozent ein stärkeres Wachstum gegeben.     
            
# re.findall(r'.+?(?:\s{2,}|:\..+?\(dpa\)|$)', a)
# re.findall(r'.+?\..+?\(dpa\)', a)
# re.findall(r'.+?(?:\..+?\(dpa\)|$)', a)
# re.findall(r'.+?(?:\..+?\(dpa\)|$)', a)
# re.findall(r'.+?(\(dpa.{50,}?(?:\s\s+|$)|.+?\..+?(?=\(dpa\)))', a)
# re.findall(r'.+?\..+?(?=\(dpa\))', a)