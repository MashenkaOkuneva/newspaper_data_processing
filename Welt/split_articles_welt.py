# -*- coding: utf-8 -*-
"""
Created on Tue May  2 13:32:11 2023

@author: mokuneva
"""

import re
import pandas as pd

def split_articles_welt(multiple_articles):
    """
    This function splits up collections of articles into single articles.
    """
    split_art = []
    
    multiple_articles.reset_index(inplace = True, drop = True)
    
    for index, row in multiple_articles.iterrows():
                
        mult_art = []
        
        txt = ' '.join(row['texts'])
        
        # The purpose of this dictionary is to account for edge cases where
        # our assumption that titles are separated by newlines may not be accurate.
        # By defining specific text replacement pairs, we can address these cases
        # and improve the accuracy of our article splitting process.
        replace_dic = {
            "\r\n \r\n rtr": " rtr",
            "\r\n \r\n ddp": " ddp",
            "\r\n \r\n AP": " AP",
            "\r\n \r\n dpa": " dpa",
            "\r\n \r\n DW": " DW",
            "\r\n \r\n AFP": " AFP",
            "\r\n \r\n -\r\n \r\n": "",
            "\r\n \r\n vwd": " vwd",
            "\r\n \r\n VWD": " VWD",
            "\r\n \r\n /DW": " /DW",
            "\r\n \r\n /": " /",
            "\r\n \r\n KNA": " KNA",
            "\r\n \r\n verbraucherfragen@senwitech. verwalt-berlin.de": "",
            "\r\n \r\n .": "",
            "\r\n \r\n Informationen im Internet:\r\n \r\n": "",
            "\r\n \r\n epd": " epd",
            "\r\n \r\n wsa": " wsa",
            "\r\n \r\n dgw": " dgw",
            "\r\n \r\n /dpa": " /dpa",
            "\r\n \r\n Informationen im Internet:": "",
            "\r\n \r\n I\r\n \r\n": " I\r\n \r\n",
            "\r\n \r\n n Deutschland": "\r\n \r\n Deutschland",
            "\r\n \r\n 24": " 24",
            "\r\n \r\n Die Seite im Internet:": " Die Seite im Internet:",
            "\r\n \r\n Nun sollen": " Nun sollen",
            "\r\n \r\n In ihrem aktualisierten": " In ihrem aktualisierten",
            "\r\n \r\n Wirtschaftsförderung im Netz": " Wirtschaftsförderung im Netz",
            "\r\n \r\n Zusammen mit Wirtschaftssenator": " Zusammen mit Wirtschaftssenator",
            "\r\n \r\n VW": " VW",
            "\r\n \r\n Das Kartellamt": " Das Kartellamt",
            "\r\n \r\n Auf das Heisenberg": " Auf das Heisenberg",
            "\r\n \r\n Bewerber sollten das": " Bewerber sollten das",
            "\r\n \r\n Wie das \"Manager Magazin\" berichtet": " Wie das \"Manager Magazin\" berichtet",
            "\r\n \r\n Die Bilanzsumme beträgt": " Die Bilanzsumme beträgt",
            "\r\n \r\n Der Gesetzgeber bleibt": " Der Gesetzgeber bleibt",
            "\r\n \r\n Das Fernziel: Einsatz": " Das Fernziel: Einsatz",
            "\r\n \r\n Das Werk enthält": " Das Werk enthält",
            "\r\n \r\n seit Dienstag perfekt.": " seit Dienstag perfekt.",
            "\r\n \r\n Nach Angaben des Genossenschaftsverbandes": " Nach Angaben des Genossenschaftsverbandes",
            "\r\n \r\n WELT Hamburg Wirtschaft": "",
            "\r\n \r\n hat Hinweise zu den erhöhten": " hat Hinweise zu den erhöhten",
            "\r\n \r\n Die Firma fährt diese Ziele": " Die Firma fährt diese Ziele",
            "\r\n \r\n Informationen im Netz:": "",
            "\r\n \r\n FBi": " FBi",
            "\r\n \r\n Dabei sind auch Vertreter": " Dabei sind auch Vertreter",
            "\r\n \r\n WS": " WS",
            "\r\n \r\n Die Voraussetzungen dafür seien gut": " Die Voraussetzungen dafür seien gut",
            "\r\n \r\n Nordbank hat im ersten Halbjahr": " Nordbank hat im ersten Halbjahr",
            "\r\n \r\n Risikovorsorge von 37": " Risikovorsorge von 37",
            "\r\n \r\n Dabei stünden vor ": " Dabei stünden vor ",
            "\r\n \r\n RTR": " RTR",
            "\r\n \r\n Die Airfoil Services Sdn": " Die Airfoil Services Sdn",
            "\r\n \r\n Rei": " Rei",
            "\r\n \r\n Nach Aussage der Gewerkschaft": " Nach Aussage der Gewerkschaft",
            "\r\n \r\n Fax": " Fax",
            "\r\n \r\n zy\r\n \r\n": "\r\n \r\n",
            "\r\n \r\n Zuwachs: Das an": " Zuwachs: Das an",
            "\r\n \r\n ms": " ms",
            "\r\n \r\n sim\r\n \r\n": "\r\n \r\n",
            "\r\n \r\n tja": " tja",
            "\r\n \r\n Im vergangenen Jahr": " Im vergangenen Jahr",
            "\r\n \r\n \"Die Ware muss zu jedem Preis": " \"Die Ware muss zu jedem Preis",
            "\r\n \r\n gs": " gs",
            "\r\n \r\n stm": " stm",
            "\r\n \r\n Dpa": " Dpa",
            "\r\n \r\n nic": " nic",
            "\r\n \r\n OLA ist nun alleiniger": " OLA ist nun alleiniger",
            "\r\n \r\n cor\r\n \r\n": "\r\n \r\n",
            "\r\n \r\n Mehr im Internet\r\n \r\n": "",
            "\r\n \r\n zv": " zv",
            "\r\n \r\n Die Urteile im Netz:\r\n \r\n": "",
            "\r\n \r\n 2006/2007 lag das Umsatzplus": " 2006/2007 lag das Umsatzplus",
            "\r\n \r\n 2006 bleiben": " 2006 bleiben",
            "\r\n \r\n Auktionator leitet den Ausverkauf\r\n \r\n": " Auktionator leitet den Ausverkauf.",
            "\r\n \r\n Siemens-Ingenieur Peter Dibowski": " Siemens-Ingenieur Peter Dibowski",
            "\r\n \r\n zum neunten Mal": " zum neunten Mal",
            "\r\n \r\n die ein Eigenkapitalinvestmen": " die ein Eigenkapitalinvestmen",
            "\r\n \r\n Lesen Sie im Netz:\r\n \r\n": "",
            "\r\n \r\n cadi": " cadi",
            "\r\n \r\n 38 Prozent mehr": " 38 Prozent mehr",
            "\r\n \r\n welt.de": " welt.de",
            "\r\n \r\n Seite 15:": " Seite 15:",
            "\r\n \r\n „Die Welt ist voller Überraschungen": " „Die Welt ist voller Überraschungen",
            "\r\n \r\n Mehr zum Thema im Internet unter:": "",
            "\r\n \r\n Diese komplette Geschichte finden sie im Internet:": "",
            "\r\n \r\n Seite 21": " Seite 21",
            "\r\n \r\n rhai": "",
            "\r\n \r\n Wer vom Finanzamt": " Wer vom Finanzamt",
            "\r\n \r\n wie das Arbeitsministerium": " wie das Arbeitsministerium",
            "\r\n \r\n rex": "",
            "\r\n \r\n mig": "",
            "\r\n \r\n kyr\r\n \r\n": "\r\n \r\n",
            "\r\n \r\n bfu": "",
            "\r\n \r\n Das Video im Netz:": "",
            "\r\n \r\n „Die Kunden zeigten sich": " „Die Kunden zeigten sich",
            "\r\n \r\n er sich eines": " er sich eines",
            "\r\n \r\n Privatverkäufer bei Ebay": " Privatverkäufer bei Ebay",
            "\r\n \r\n Mehr unter:": "",
            "\r\n \r\n Mifa hatte 2013 einen": " Mifa hatte 2013 einen",
            "\r\n \r\n Wann der Airport": " Wann der Airport",
            "\r\n \r\n Dies habe den Steuerzahler": " Dies habe den Steuerzahler",
            "\r\n \r\n Wir bitten diesen Fehler zu entschuldigen": "",
            "\r\n \r\n Gründe für die Einschätzung": " Gründe für die Einschätzung",
            "\r\n \r\n Inzwischen erholen sich": " Inzwischen erholen sich",
            "\r\n \r\n Weiterer Bericht: Seite 21": " Weiterer Bericht: Seite 21",
            "\r\n \r\n Reuters\r\n \r\n": "\r\n \r\n",
            "\r\n \r\n Thema der Konferenz": " Thema der Konferenz",
            "\r\n \r\n Zur Hotel-Studie:\r\n \r\n www.treugast.com": " Zur Hotel-Studie: www.treugast.com",
            "\r\n \r\n Foto:": " Foto:",
            "\r\n \r\n (Aktenzeichen": " (Aktenzeichen"}
        
        for not_title, correction in replace_dic.items():
            txt = txt.replace(not_title, correction) 
        
        # Case 1: Handle texts that start with 'WIRTSCHAFT KOMPAKT' and contain multiple
        # articles with capitalized titles. We use the capitalized
        # titles within the text to split it into separate articles, treating each
        # capitalized title as the start of a new article.
        if re.findall(r'\r\n \r\n [A-ZÄÖÜ I&/-]+\r\n \r\n', txt) == ['\r\n \r\n WIRTSCHAFT KOMPAKT\r\n \r\n']:
            txt = txt.replace('\r\n \r\n WIRTSCHAFT KOMPAKT', '')
            texts = re.split(r'\r\n \r\n .+\r\n \r\n', txt)
            titles = re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)
            
            for i, text in enumerate(texts[1:]):
                text = text.strip()
                text = text.replace('\r\n', '').strip()
                text = text.replace('Weitere Informationen im Internet unter: ', '')
                text = re.sub(r'https\S+', '', text)
                text = re.sub(r'http\S+', '', text)
                text = re.sub(r'www.\S+', '', text)
                clean_text = "{}. {}".format(titles[i], text)
                mult_art.append(clean_text)
        
        # Case 2: Handle texts that do not start with 'WIRTSCHAFT KOMPAKT' or 'BASKETBALL'
        # and contain multiple articles with capitalized titles.
        elif re.findall(r'\r\n \r\n [A-ZÄÖÜ I&/-]+\r\n \r\n', txt)!= [] and \
            re.findall(r'\r\n \r\n ([A-ZÄÖÜ I&/-]+)\r\n \r\n', txt)[0] != 'BASKETBALL' and \
               len(re.findall(r'\r\n \r\n [A-ZÄÖÜ I&/-]+\r\n \r\n', txt)) == len(re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)):
                
            texts = re.split(r'\r\n \r\n [A-ZÄÖÜ I&/-]+\r\n \r\n', txt)
            titles = re.findall(r'\r\n \r\n ([A-ZÄÖÜ I&/-]+)\r\n \r\n', txt)
        
            for i, text in enumerate(texts[1:]):
                first_sentence, rest_text = re.split(r'\r\n', text.strip(), 1)
                first_sentence = first_sentence[0].upper() + first_sentence[1:]
                rest_text = rest_text.replace('\r\n', '').strip()
                rest_text = rest_text.replace('Weitere Informationen im Internet unter: ', '')
                rest_text = re.sub(r'https\S+', '', rest_text)
                rest_text = re.sub(r'http\S+', '', rest_text)
                rest_text = re.sub(r'www.\S+', '', rest_text)
                clean_text = "{}. {}. {}".format(titles[i], first_sentence, rest_text)
                mult_art.append(clean_text)
        
        # Case 3: Handle texts where some article titles are not capitalized.
        elif len(re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt))>1 and \
             re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)[0] != 'Stadt Diese Woche Vorwoche' and \
             re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)[0] != 'Bundesliga' and \
            'DIE WELT:' not in txt:
                 
            texts = re.split(r'\r\n \r\n .+\r\n \r\n', txt)
            titles = re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)
            
            # Only titles, no subtitles
            if re.findall(r'\r\n \r\n (.+)\r\n \r\n', txt)[0].split(' ')[0].isupper() or \
                len(re.split(r'\r\n \r\n .+\r\n \r\n', txt)[1].split('\r\n \r\n', 1)) == 1:
                    
                for i, text in enumerate(texts[1:]):
                    text = text.strip()
                    text = text.replace('\r\n', '').strip()
                    text = text.replace('Weitere Informationen im Internet unter: ', '')
                    text = re.sub(r'https\S+', '', text)
                    text = re.sub(r'http\S+', '', text)
                    text = re.sub(r'www.\S+', '', text)
                    clean_text = "{}. {}".format(titles[i], text)
                    mult_art.append(clean_text)
                    
            else:
                
                for i, text in enumerate(texts[1:]):
                    # Titles with subtitles
                    if len(re.split(r'\r\n \r\n', text.strip(), 1)) > 1:                        
                        first_sentence, rest_text = re.split(r'\r\n \r\n', text.strip(), 1)
                        first_sentence = first_sentence.replace('\r\n', '').strip()
                        first_sentence = first_sentence[0].upper() + first_sentence[1:]
                        rest_text = rest_text.replace('\r\n', '').strip()
                        rest_text = rest_text.replace('Weitere Informationen im Internet unter: ', '')
                        rest_text = re.sub(r'https\S+', '', rest_text)
                        rest_text = re.sub(r'http\S+', '', rest_text)
                        rest_text = re.sub(r'www.\S+', '', rest_text)
                        clean_text = "{}. {}. {}".format(titles[i], first_sentence, rest_text)
                    # Only titles, no subtitles
                    else:
                        text = text.strip()
                        text = text.replace('\r\n', '').strip()
                        text = text.replace('Weitere Informationen im Internet unter: ', '')
                        text = re.sub(r'https\S+', '', text)
                        text = re.sub(r'http\S+', '', text)
                        text = re.sub(r'www.\S+', '', text)
                        clean_text = "{}. {}".format(titles[i], text)                       
                    
                    mult_art.append(clean_text)
                    
        # Case 4: Handle texts where articles are separated by a newline, but
        # the title and the main body of each article are not.
        # To accurately identify and separate the individual articles, 
        # the algorithm ensures that the first article contains at least 40 tokens.          
        elif len(re.split(r'\r\n \r\n', txt.strip())) == 2 and len(re.split(r'\r\n \r\n', txt.strip())[0].split(' ')) > 40:
            
            texts = re.split(r'\r\n \r\n', txt.strip())
            
            for i, text in enumerate(texts):
                text = text.strip()
                text = text.replace('\r\n', '').strip()
                text = text.replace('Weitere Informationen im Internet unter: ', '')
                text = re.sub(r'https\S+', '', text)
                text = re.sub(r'http\S+', '', text)
                text = re.sub(r'www.\S+', '', text)
                mult_art.append(text)
                
        # Case 5: Handle instances where none of the previous patterns were identified.
        else:
            
            text = txt.replace("\n", '').replace("\r", '').replace("\t", '').strip()
            text = text.replace('Weitere Informationen im Internet unter: ', '')
            text = re.sub(r'https\S+', '', text)
            text = re.sub(r'http\S+', '', text)
            text = re.sub(r'www.\S+', '', text)
            mult_art.append(text)
        
        # Make sure that there are no extra white spaces
        mult_art = [' '.join(m.split()) for m in mult_art] 
        
        if mult_art != []:
            
            for art in mult_art:
                # Store meta data for the article
                separated_articles = multiple_articles.iloc[index][multiple_articles.iloc[index] != 'texts']
                # Assign the new text to the matching meta data
                separated_articles['texts'] = art
                split_art.append(separated_articles)
                    
        else:
            split_art.append(row) 

    return(pd.concat(split_art, axis=1).transpose())