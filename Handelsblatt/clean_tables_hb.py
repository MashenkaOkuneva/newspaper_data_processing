# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 20:37:47 2023

@author: mokuneva
"""

import re

def clean_tables_hb(text):
    
    """
    This function removes tables.
    """
    
    # Remove tables using regular expressions
    text = re.sub("""Liste der betroffenen Standorte\..{0,}|
    |Zählen wir mal durch\:.{0,}|
    |Londoner Banken berichteten von folgenden neuen Euromarkt.{0,}|
    |Bei den Dax \- Warrants geht die Laufzeit.{0,}|
    |Außerdem wurden begeben:.{0,}|
    |Außerdem wurden u\.a\. begeben:.{0,}|
    |Außerdem wurden aufgelegt:.{0,}|
    |Folgende Emissionen erschienen:.{0,}|
    |Am schweizerischen Kapitalmarkt wurden in den letzten Tagen folgende Anleihen neu zur Zeichnung aufgelegt.{0,}|
    |Wirtschaftsförderung \(Gebietskörperschaften\) in Ostwestfalen.{0,}|
    |Londoner Banken berichteten von folgenden neuen Euro.{0,}|
    |Wichtige Adressen\..{0,}|
    |In anderen Währungen wurden folgende Neuemissionen begeben.{0,}|
    |Außerdem wurden emittiert\:.{0,}|
    |Hamburg\: Jacobsen \+.{0,}|
    |Folgende Neuemissionen wurden an den Markt gebracht.{0,}|
    |OPTIONSSCHEINE / Calls.{0,}|
    |EMISSIONEN / Neue Produkte im Angebot.{0,}|
    |Am Schweizer Kapitalmarkt liegen neue Emissionen zur Zeichnung auf.{0,}|
    |Geschäftsinformationen\. Delegiertenbüro.{0,}|
    |Hier die markanten Prognosen.{0,}|
    |Eine AHK-Adressen-Liste verschickt der DIHT.{0,}|
    |^Kontaktadressen\..{0,}|
    |In anderen Währungen wurden begeben\:.{0,}|
    |Anreise\: Air Lithuania bietet Frankfurt.{0,}|
    |Flughafen - Chronik\..{0,}|
    |Wertzuwachs der ETW\. Beispiel.{0,}|
    |Außerdem wurden am Dienstag und Mittwoch u\.a\. begeben\:.{0,}|
    |BEISPIEL\: Anspruch auf Arbeitslosengeld.{0,}|
    |CHRONIK / Banken und Börsen.{0,}|
    |ÖFFENTLICHE AUFTRÄGE\. Das Technologiezentrum.{0,}|
    |BÜCHER FÜR BEWERBER\. Optimal bewerben.{0,}|
    |Am Schweizer Kapitalmarkt liegen neue Anleihen auf\:.{0,}|
    |Eintracht Frankfurt\. Gegründet.{0,}|
    |SV Werder Bremen\. Gegründet\:.{0,}|
    |GRÜNDERZENTREN\. Bundesverband.{0,}|
    |F\.C\. Hansa Rostock\. Gegründet.{0,}|
    |Beratungs - und Seminaranbieter\..{0,}|
    |Gegründet\: \d{4}\..{0,}|
    |Borussia Mönchengladbach\. Gegründet\:.{0,}|
    |1\.FC Kaiserslautern\. Gegründet\:.{0,}|
    |Am Schweizer Kapitalmarkt liegen eine Reihe.{0,}|
    |Gegründet\: \d{4} Erfolge\:.{0,}|
    |Unter der Federführung der Schweizerischen Kreditanstalt \(.{0,}|
    |Düsseldorf in Zahlen\..{0,}|
    |HEUTE IN HANNOVER\..{0,}|
    |BÜCHER UND BROSCHÜREN\..{0,}|
    |U\.a\. wurden folgende Emissionen am Euromarkt begeben.{0,}|
    |Deutsche Museen und Institute mit ständigen.{0,}|
    |Bevorzugte werden\:.{0,}|
    |HÖHEPUNKTE DER SAISON\..{0,}|
    |Neu an den Eurobondmarkt kamen bis zum.{0,}|
    |(?:Folgende US-Unternehmen gaben ihre Quartalsergebnisse bekannt)(?:.{0,})(?=Am Bondmarkt)|
    |^Service\..{0,}|
    |Adressen Weiterbildungsinstitute AFK Akademie.{0,}|
    |Eine AHK-Adressen-Liste verschickt der DIHT.{0,}|
    |ù Die Depfa stockte.{0,}|
    |Zudem gab es folgende Neu-Emissionen\:.{0,}|
    |Preiswerte Betten mit Ambiance\..{0,}|
    |Londoner Euromarktbanken berichteten darüber hinaus.{0,}|
    |Konsortialbanken berichteten zur Wochenmitte von folgenden.{0,}|
    |Aus Londoner Konsortialkreisen war von folgenden.{0,}|
    |Londoner Konsortialbanken berichteten von folgenden.{0,}|
    |WM-QUALIFIKATION\..{0,}|
    |Herausragende Köche\, die sich.{0,}|
    |CHRONOLOGIE\. 22.{0,}|
    |U\.a\. wurden begeben\:.{0,}|
    |Weiter wurden u\.a\. begeben\:.{0,}|
    |EURO-TERMINE\..{0,}|
    |Ansprechpartner für EDI und EDIFACT.{0,}|
    |Europäische Sommerausstellungen.{0,}|
    |Expo-Geschichte\..{0,}|
    |IWF-Aktionen\..{0,}|
    |MAILAND / Nützliche Adressen.{0,}|
    |MAILAND / Wo man sein müdes.{0,}|
    |FINANZIERUNGSBEISPIELE\..{0,}|
    |STEUERN / Einschränkungen.{0,}|
    |MESSEN FÜR WEINFREUNDE\..{0,}|
    |DIE ERSTEN SCHRITTE\. ANSPRECHPARTNER.{0,}|
    |TIPS UND BEISPIELE\..{0,}|
    |Salomon nennt folgende Aktien als Topfavoriten.{0,}|
    |BÜCHER \+ SEMINARE\..{0,}|
    |Eine kleine Chronologie\..{0,}|
    |CHIO IM TV\..{0,}|
    |Unter diesen \"Schirmen\".{0,}|
    |SO BERECHNET SICH DER SPEKULATIONSGEWINN.{0,}|
    |^Seminare\..{0,}'|
    |ÜBER DUBIOSE FIRMEN INFORMIERT\:.{0,}|
    |DIMA \’99.{0,}|
    |^BÜCHER\..{0,}|
    |LUXEMBURGISCHE STEUERZAHLER\..{0,}|
    |Landeszentralbanken geben Auskunft\..{0,}|
    |Kultur-Tipp\..{0,}|
    |Business-TV\. Freitag\,.{0,}|
    |(?:Business-TV\.)(?: Montag| Dienstag| Mittwoch| Donnerstag| Freitag| Samstag| Sonntag)(?:\,.{0,})|
    |POLITISCHE EREIGNISSE\..{0,}|
    |SPORTKALENDER.{0,}|
    |NEUERSCHEINUNGEN\..{0,}|
    |EURO-TERMINE\. Mai.{0,}|
    |TERMINE\. DIENSTAG.{0,}|
    |Gesundheit - Made in Berlin.{0,}|
    |OLYMPISCHE SPIELE\: 302.{0,}|
    |MITGLIEDER DES NATIONALEN ETHIKRATES.{0,}""", " ", text)
    
    return(text)