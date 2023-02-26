# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 15:06:59 2023

@author: mokuneva
"""

import re

def clean_tables(text):
    
    """
    This function removes tables.
    """
    
    # Remove tables using regular expressions
    text = re.sub("""Im einzelnen ergaben sich folgende Veränderungen.{0,}|
    |Lebenshaltungspreise Veränderung zu Neuer Dezember Vorjahr.{0,}|
    |Die Kfz-Zulassungszahlen im Monats- und Jahresvergleich.{0,}|
    |Im einzelnen ergab sich folgende Entwicklung.{0,}|
    |Entwicklung des Außenwerts der D-Mark .{0,}|
    |Im einzelnen gab es folgende Entwicklung.{0,}|
    |Im Vergleich zum Zeitraum Januar/Februar des Vorjahres traten.{0,}|
    |Im einzelnen kam es zu folgenden Veränderungen.{0,}|
    |Im einzelnen ergaben sich folgende Veränderungen.{0,}|
    |Nachfolgend der Jahresvergleich im Detail.{0,}|
    |Exporte 2000 nach Ländern.{0,}|
    |Exporte 2001 nach Ländern.{0,}|
    |Veränderung in Prozent.{0,}|
    |Weltautomobilproduktion \(in Millionen Wagen\).{0,}""", " ", text)
    
    return(text)