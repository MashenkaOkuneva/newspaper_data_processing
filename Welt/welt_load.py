# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 16:59:43 2023

@author: mokuneva
"""

import codecs
import re
import pandas as pd

def welt_load(file):
    
    '''This is a function which will load Welt data from one file.'''
    
    data = None
    
    # Create lists for information to store
    day = []    # day of publication
    month = []  # month of publication
    year = []   # year of publication
    texts = []  # articles
    newspaper = []  # name of the newspaper
    rubrics = []    # sections and subsections of the newspaper
    title_list = []    # title of the article (including annotation)
    kompakt_list = []  # a list with 1 for 'kompakt' section with multiple articles
    
    # Open the file with utf-8 encoding
    with codecs.open(file, "r", encoding = 'utf-8' ) as input_data:
        # Determine the number of articles in the document
        for line in input_data:
            # The line containing "Download" looks like this: "Download Request: Select Items: 601-642"
            # repeat: the number of articles in the document, here 642-601+1
            if line.find('Download') != -1:   
                repeat = int(line.split()[4].split('-')[1])-int(line.split()[4].split('-')[0])+1
                break
            # Documents from 2018: "Ausgabeauftrag: Dokument(e): 1-200"
            # This means that a search was completed in German
            elif line.find('Ausgabeauftrag') != -1:
                repeat = int(line.split()[2].split('-')[1])-int(line.split()[2].split('-')[0])+1
                break
            
        # Process each article in the document
        for i in range(repeat):
            kompakt = False
            text = []
            # Skips text before the beginning of the interesting block:
            for line in input_data:
                # Find the line containing "DOCUMENTS" or "Dokument", and skip the text before this line
                if line.find('DOCUMENTS') != -1 or line.find('Dokument') != -1:   
                    break
                    
            # NEWSPAPER NAME (makes sense to add as the data is coming from several sources) 
            for line in input_data:
                if line.find('Die Welt') != -1 or line.find('DIE WELT') != -1:
                    newspaper.append('Welt')
                    break
            
            # DAY/MONTH/YEAR
            for line in input_data:
                if line.find('.') != -1:
                    if len(line.split()) == 3:
                        day.append(line.split()[0][:-1])
                        month.append(line.split()[1])
                        year.append(line.split()[2])
                        break
                    else:
                        day.append(line.split()[1][:-1])
                        month.append(line.split()[2])
                        year.append(line.split()[3])
                        break
            
            # TITLE AND ANNOTATION
            title = []
            for line in input_data:
                if line.find('RUBRIK') != -1:
                    # Process the title:
                    # 1. Strip whitespace on both sides
                    # 2. Remove tab and line break
                    title[1] = title[1].strip().replace("\n", '').replace("\t", '').replace("\r", '')
                    # If the title ends with ";", remove it
                    title[1] = title[1].replace(";", '') 
                    # If there is no period, colon, semicolon, exclamation, or question mark
                    # at the end of the sentence, add a period.
                    if title[1][-1] not in ['.', '!', ':', ';', '?']:
                        title[1] = title[1] + '.' 
                        
                    title = ' '.join(title)
                    
                    # If the section contains 'kompakt', then the text already contains the titles
                    # of subsections, and annotation is not required.
                    if line.find('kompakt') == -1 and line.find('Kompakt') == -1:
                        kompakt_list.append(0)
                        title = title.strip().replace("\n", '').replace("\t", '').replace("\r", '')
                        # Replace ' ++' in the annotation with '.'
                        title = title.replace(' ++', '.')
                        if title[-1] not in ['.', '!', ':', ';', '?', '"']: 
                            title = title + '.'
                        title_list.append(title)
                    else:
                        kompakt = True
                        kompakt_list.append(1)
                        title_list.append('')
                        
                    # SECTION/SUBSECTION OF THE NEWSPAPER    
                    rubrics.append(line.split(':')[1].split(';')[0].strip())
                    break
                elif (line.find('AUTOR') == -1):
                    title.append(line)
            
            # TEXT
            for line in input_data:
                if line.find(u'Wörter') != -1:
                    break
            for line in input_data:
                if line.find('UPDATE') != -1:
                    break
                if kompakt == False:
                    line = line.strip()
                    line = line.replace("\n", '').replace("\r", '').replace("\t", '')
                    if line != '':
                        if ((line[-1] not in ['.', '!', ':', ';', '?', '"', "'"]) & (len(line.split(' '))<6)):
                            line = line + '.'
                        line = line.replace('Weitere Informationen im Internet unter: ', '')
                        # Remove URLs
                        line = re.sub(r'https\S+', '', line)
                        line = re.sub(r'http\S+', '', line)
                        line = re.sub(r'www.\S+', '', line)
                        # Replace non-breaking space with a regular space
                        line = re.sub('\xa0', ' ', line)
                        text.append(line)
                else:
                    text.append(line)
            if kompakt == False:
                text = ' '.join(text)
                text = text.strip()
            # If the text is not empty, merge the title, annotation, and the text
            if len(text) > 0 and len(title_list[-1]) > 0:
                text = title_list[-1] + ' ' + text
            texts.append(text)
    
    # Create a dictionary to convert month names into month numbers
    name_to_number = {u'Januar':1, u'Februar':2, u'M\xe4rz':3, u'April':4, u'Mai':5, u'Juni':6, u'Juli':7, u'August':8, u'September':9, u'Oktober':10, 
                  u'November':11, u'Dezember':12}
    
    # Convert month names to month numbers
    month_num = []
    for m in month:
        month_num.append(name_to_number[m])
        
    # Convert days and years to integers
    day = list(map(int, day))
    year = list(map(int, year))
    
    # Create a DataFrame with the extracted data
    data = pd.DataFrame({'year' : year,
     'month' : month_num,
     'day' : day,
     'newspaper': newspaper,
     'texts': texts,
     'rubrics': rubrics,
     'title': title_list,
     'kompakt': kompakt_list})
    
    return data
