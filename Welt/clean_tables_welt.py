# -*- coding: utf-8 -*-
"""
Created on Wed May 10 13:03:33 2023

@author: mokuneva
"""

import re

def clean_tables_welt(text):
    
    """
    This function removes tables.
    """
    
    # Remove tables using regular expressions
    text = re.sub("""Zinsen in Prozent\. Tagesgeld.{0,}|
    |Eichels Streichliste\. HIGHLIGHT\:.{0,}|
    |rtr REPOWER Systems\. WKN.{0,}|
    |Hier kann man drahtlos surfen\..{0,}|
    |Tips für die Buchung\..{0,}|
    |1 \(2\) Simplify your life.{0,}|
    |Im Haspax sind folgende 25 Unternehmen vertreten.{0,}|
    |Messe-Termine\..{0,}|
    |Große WELT-Telefonaktion zum Thema Investmentfonds \(.{0,}|
    |So hat sich das Leben in New York seit dem vergangenen Jahr geändert.{0,}|
    |Kleine Tipps zum Ausfüllen des Lottoscheins.{0,}|
    |Tabelle: Arbeitslose in Deutschland im Oktober 2009 Quelle.{0,}|
    |Tabelle: Jahressonderzahlung.{0,}|
    |Tabelle: Die Verluste.{0,}|
    |Weblink: \. Oktober 2009\. September 2009.{0,}|
    |Tabelle: Welche Dinge die Deutschen.{0,}|
    |Tabelle: Top Ten der Lieblings-Arbeitgeber von Akademikern 2009|
    |Weblink: \. Platz\. Wirtschaftswiss\..{0,}|
    |Tabelle\: Umsatz im Einzelhandel.{0,}|
    |Tabelle: Zukunftsangst der Konsumenten.{0,}|
    |Tabelle: Als was ehemalige Hartz-IV-Empfänger arbeiten Anmerkung: 429 Befragte\, Quelle: IAB\.|
    |Weblink: \. Berufliche Stellung.{0,}|
    |Tabelle: Die zehn schlechtesten.{0,}|
    |Messe Termine\..{0,}""", " ", text)
    
    return(text)