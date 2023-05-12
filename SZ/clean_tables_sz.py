# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 14:54:29 2023

@author: mokuneva
"""

import re

def clean_tables_sz(text):
    
    """
    This function removes tables.
    """
    
    # Remove tables using regular expressions
    text = re.sub("""Münchner SchlußkurseNotierungen.{0,}|
    |Bernhard Wild Münchner Kassa.{0,}|
    |bwi Münchner Kassa.{0,}|
    |Reihenfolge nach prozentualer Veränderung.{0,}|
    |Martin Reim Münchner Kassa.{0,}|
    |sec Was deutsche Aktien und Anleihen den Anlegern.{0,}|
    |Paul Katzenberger Frankf\. Schlusskurse.{0,}|
    |Antonie Bauer Call-by-Call-Tarife.{0,}|
    |Münchner Kassa-KurseNotierungen.{0,}|
    |Frankfurter KassakurseNotierungen.{0,}|
    |Xetra-SchlusskurseNotierungen.{0,}|
    |Quellen\: Europäisches Parlament\, Stand.{0,}|
    |\- Die durchschnittlichen Auflagenzahlen der übrigen Münchner Blätter\:.{0,}|
    |Die Wahltermine in diesem Jahr\..{0,}|
    |Dividenden vom Tage\..{0,}|
    |Wirtsch\.Lit\.\:.{0,}|
    |Einzelergebnisse aus den Wahlkreisen\..{0,}|
    |H\. Wichtigste unmittelbare Beteiligungen.{0,}|
    |Spenden für Ruanda\..{0,}|
    |Renditen vom Tage\..{0,}|
    |Samstag AN=SAQUOTEN.{0,}|
    |Die Kontingente der einzelnen Länder\:.{0,}|
    |\- Die Auflagenentwicklung der übrigen Münchner Blätter.{0,}|
    |Renditen vom T age.{0,}|
    |1996\* 1995\* 1994.{0,}|
    |Die Auflagen der übrigen Münchner Blätter\:.{0,}|
    |- Belgien\: 1000 Soldaten.{0,}|
    |Beispiele für Durchschnittspreise:.{0,}|
    |- Die Auflagen der übrige Münchner Blätter.{0,}|
    |Hans Einhell AG\, Landau: Für 1995.{0,}|
    |Konditionen für Baudarlehen sinken.{0,}|
    |- Die übrigen Münchner Blätter melden für.{0,}|
    |- Die Auflage der übrigen Münchner Blätter.{0,}|
    |Budgetdefizit \(in Prozent.{0,}|
    |Vorhersage bis Freitag.{0,}|
    |Die jahresdurchschnittlichen Inflationsraten 1997.{0,}|
    |100 Prozent nur für Hans-Jochen.{0,}|
    |Die weltweit größten Finanz-Ehen seit.{0,}|
    |Unternehmen\, OrtBrancheUmsatz.{0,}|
    |Im Zwei-Monats-Vergleich ergaben sich gegenüber.{0,}|
    |Ausgewählte Aktienanleihen im ÜberblickKupon.{0,}|
    |Soziale Dienste im Würmtal\..{0,}|
    |Hirsch in Zahlen \(.{0,}|
    |Waagrecht: 1.{0,}|
    |Kramnik\`s Technik\..{0,}|
    |An den Osterfeiertagen:.{0,}|
    |Zum 70\. Geburtstag alles Gute\..{0,}|
    |Pfarreien\. Planegg.{0,}|
    |Waagrecht: 2.{0,}|
    |Sizilianischer Konter\..{0,}|
    |Was Hypothekendarlehen kosten \(.{0,}|
    |Der Paukenschlag\..{0,}|
    |Häufigste Kundenkarten mit Zahlungsfunktion.{0,}|
    |Theater Bellevue.{0,}|
    |Mittwoch\, 12\. Mai Theater.{0,}|
    |Waagrecht: 3.{0,}|
    |Theater DT-Kammerspiele.{0,}|
    |Auf Biegen und Brechen\. Judit.{0,}|
    |Blinde Meister\..{0,}|
    |Mittwoch\, 2\. Juni Theater carrousel.{0,}|
    |Donnerstag\, 3\. Juni Theater.{0,}|
    |Theater Atrium.{0,}|
    |Waagrecht: 3.{0,}|
    |Die größten Telekom-Konzerne der Welt nach Marktkapitalisierung.{0,}|
    |Springer ohne Heimat\. Kasparov.{0,}|
    |Sonntag\, 13\. Juni Theater.{0,}|
    |Theater DT-Baracke.{0,}|
    |99 deutsche Abgeordnete\. CDU.{0,}|
    |Die zweite Front\. Topalow.{0,}|
    |Eckwerte der Konjunktur Volkwirtschaftl\. Schlüsselzahlen.{0,}|
    |Theater Brotfabrik.{0,}|
    |Romantischer Russe\. Fedorow.{0,}|
    |Theater Chapeau.{0,}|
    |Ertragsteuerzahlungen deutscher Großunternehmen im In- und AuslandDeutsche.{0,}|
    |Was Hypothekardarlehen kosten \(.{0,}|
    |Beschäftigte in der VersicherungswirtschaftJahr.{0,}|
    |Die neue Größe Alcan.{0,}|
    |1\) prozentuale Veränderung gegenüber.{0,}|
    |Das Steuerreform-Konzept auf einen Blick.{0,}|
    |Renate Daum Wertentwicklung ausgewählter Japan.{0,}|
    |Nimmt man den Referenzkurs vom Donnerstag.{0,}|
    |FrankreichGroßbritannienItalien.{0,}|
    |Die größten Management-Berater in Deutschland.{0,}|
    |Veränderungen des realen BIP und der VerbraucherpreiseBrutto.{0,}|
    |Die Konditionen ausgewählter AktienanleihenWKN.{0,}|
    |Wirtschaftliche Eckdaten für Deutschland.{0,}|
    |DIE BESTEN 25.{0,}|
    |Christine Beckler Call-by-Call-Tarife für Telefonate.{0,}|
    |Neulinge an deutschen Börsen seit Anfang.{0,}|
    |Martin Reim Debütanten an deutschen Börsen seit Anfang.{0,}|
    |Das Einkommen der US-Manager hängt am Bonus.{0,}|
    |Die neue Führung der CDU\. Vorsitzende\:.{0,}|
    |Die Titel am Prädikatsmarkt der Bayerischen Börse \(.{0,}|
    |Ausgewählte Aktienanleihen \(.{0,}|
    |Betriebsergebnisse Kernkraftwerke.{0,}|
    |Top 15 der internationalen Börsenplätze.{0,}|
    |NameStreubesitz Gewicht.{0,}|
    |Die Grundentschädigung beträgt in Bund und Ländern.{0,}|
    |\(Firmen des Tages\)\. BMW-Gruppe in Zahlen.{0,}|
    |Wer im vergangenen Monat an deutschen Börsen debütierte 1\)NameBörsen-.{0,}|
    \Wer seit Anfang August an die Börse gegangen ist\.\.\..{0,}|
    |NameStreubesitz in \%.{0,}|
    |MAN-Nutzfahrzeuge Teilkonzern.{0,}|
    |Das zahlen ausgewählte Banken.{0,}|
    |Heute in Berlin\:.{0,}|
    |ABB Mannheim-Konzern in Zahlen.{0,}|
    |BBS-Konzern in Zahlen.{0,}|
    |Scharpings Flüge von und nach Frankfurt.{0,}|
    |Spendenkonten für Afghanistan\..{0,}|
    |Die Wahlen der Beisitzer hatten folgendes Ergebnis.{0,}|
    |Die Preisträger der letzten 25 Jahre.{0,}|
    |Die Flutkatastrophe: Was das verheerende Hochwasser.{0,}|
    |Spendenkonten für Irak\..{0,}|
    |Das Kabinett von Machmud Abbas\..{0,}|
    |Die Mutmacher\. 22 Unternehmen beweisen.{0,}|
    |Die Resultate der Bürgerschaftswahl auf Bezirksebene:.{0,}|
    |Milliarden-Hilfe für die Flutopfer.{0,}|
    |Beispiele\. Beispiel 1:.{0,}|
    |Die Top 50 der Welt: Die Gewinne.{0,}|
    |Bungalows und Wohncontainer\..{0,}|
    |Spenden für Pakistan\. Diakonie-Katastrophenhilfe.{0,}|
    |Die Geschichte der Bundeswehr\..{0,}|
    |Die Angeklagten\. Was den obersten.{0,}|
    |Die Urteile\. Am 1\. Oktober.{0,}|
    |Für jeden Geschmack das Richtige\..{0,}|
    |Ein-Prozent-Methode oder Pauschale.{0,}|
    |Was das Jahr 2008 bringt\..{0,}|
    |Billig: iPhone\, Nüsse\, Gurken Teuer:.{0,}|
    |Auf dem Treppchen\. Unternehmen Firmensitz Umsatz.{0,}|
    |Nordrhein-Westfalen 2009 \%.{0,}|
    |(?:Belgien Prozent Sitze 2009)(?:.{0,})(?=So schlimm)|
    |Irland Prozent Sitze 2009.{0,}|
    |Messekalender\. Wasser Berlin.{0,}|
    |Messekalender\. Stone\+tec.{0,}|
    |Schleswig-Holstein 1 Flensburg.{0,}|
    |Messetermine\. Bildung:.{0,}""", " ", text)
    
    return(text)