# -*- coding: utf-8 -*-
"""
Created on Wed Apr  22 16:08:30 2020

@author: mokuneva
"""
# Disclaimer: the code was initially written in Python 2. 

# import ElementTree module to load data from an XML file
import xml.etree.ElementTree as ET
import pandas as pd
import os
import re


def sz_load(folder):
    
    '''This is a function which will load SZ data from one folder.'''
    
    data = None 
    
    # for each file in a particular folder
    for s in [s for s in os.listdir(folder) ]:
        # create tree structure with the parse function
        tree = ET.parse(folder + '\\' + s)  
        root = tree.getroot()
        
        # create lists for information to store
        day = []           # day of publication
        month = []         # month of publication
        year = []          # year of publication
        texts = []         # articles
        newspaper = []     # name of the newspaper
        rubrics = []       # sections and subsections of the newspaper
        title_list = []    # title of the article (including a kicker and a subheading)
        quelle_texts = []  # description of the source, useful for filtering out regional articles
        page_list = []     # page number in the newspaper
        
        for article in root.findall('artikel'):
            if article.find('inhalt') is not None: # if an article is not empty
                
                # SOURCE, DESCRIPTION
                quelle_text = ''
                if article.find('metadaten').find('quelle_text') is not None:
                    quelle_text = article.find('metadaten').find('quelle_text').text
                    quelle_text = quelle_text.encode('utf-8').decode('utf-8') # save the string as unicode
                    quelle_text = quelle_text.strip() # strip whitespace on both sides
                    quelle_text = quelle_text.replace("\n", ' ') # replace line break (new line character) with space
                    quelle_text = quelle_text.replace("\t", ' ') # replace tab with space
                quelle_texts.append(quelle_text)
                    
                # DAY/MONTH/YEAR
                if article.find('metadaten').find('quelle').find('datum') is not None:
                    # save date as a string
                    date = article.find('metadaten').find('quelle').find('datum').text
                    
                # if the date is missing, use the date of the previous article (I load the data in a chronological order)
                day.append(date[6:]) # part with the day as a string
                month.append(date[4:6]) # part with a month as a string
                year.append(date[0:4]) # part with a year as a string
                                
                # SECTION/SUBSECTION OF THE NEWSPAPER
                rubric = ''
                if (article.find('inhalt').find('titel-liste') is not None):
                    # if there is info about the section of the newspaper
                    if (article.find('inhalt').find('titel-liste').find('ressort') is not None):                       
                        # section of the newspaper (e.g., Politics, Economics)
                        rubric = article.find('inhalt').find('titel-liste').find('ressort').text 
                        rubric = rubric.encode('utf-8').decode('utf-8') # save the string as unicode
                        rubric = rubric.strip() # strip whitespace on both sides
                        rubric = rubric.replace("\n", ' ') # replace line break (new line character) with space
                        rubric = rubric.replace("\t", ' ') # replace tab with space
                rubrics.append(rubric)
    
                # NESPAPER NAME (makes sense to add as the data is coming from several sources)       
                news = ''
                if article.find('metadaten').find('quelle').find('name') is not None: # newspaper name (source)  
                    news = article.find('metadaten').find('quelle').find('name').text
                    news = news.encode('utf-8').decode('utf-8') # save the string as unicode
                newspaper.append(news)
                
                # PAGE NUMBER IN THE NEWSPAPER
                page = ''
                if article.find('metadaten').find('quelle').find('seite-start') is not None: 
                    page = article.find('metadaten').find('quelle').find('seite-start').text
                    page = page.encode('utf-8').decode('utf-8')  # save the string as unicode
                page_list.append(page)     
    
                # TEXT OF THE ARTICLE        
                # text consists of title + annotation + main_text
                paragraphs = ""
                
                # SUBHEADING ('UNTERTITEL')
                # Starting from 1999, a new metadata tag 'untertitel' appears in XMLs.
                # If 'untertitel' is present, simply add it to the title.
                untertitel = ''
                if article.find('inhalt').find('titel-liste') is not None:
                    if article.find('inhalt').find('titel-liste').find('untertitel') is not None:
                        try:
                            article.find('inhalt').find('titel-liste').find('untertitel').text
                            untertitel = article.find('inhalt').find('titel-liste').find('untertitel').text
                            untertitel = untertitel.encode('utf-8').decode('utf-8') # save the string as unicode
                            untertitel = untertitel.strip() # strip whitespace on both sides
                            untertitel = untertitel.replace("\n", ' ') # replace line break (new line character) with space
                            untertitel = untertitel.replace("\t", ' ') # replace tab with space
                            untertitel = ' '.join(untertitel.split()) # substitue multiple whitespaces with single whitespace
                            
                            # if there is no period, colon, semicolon, exclamation, question, or quotation mark 
                            # at the end of the sentence, add period.
                            if untertitel[-1] not in ['.', '!', ':', ';','?', '"']: 
                                untertitel  = untertitel  + '.'
                        except:
                            untertitel = ''
                            
                # KICKER
                # a smaller line above the headline ('Dachzeile')
                
                # Starting from 1999, a new metadata tag 'dachzeile' appears in XMLs.
                # If 'dachzeile' is present, simply add it to the title.
                kicker = ''
                if (article.find('inhalt').find('titel-liste') is not None):
                    if (article.find('inhalt').find('titel-liste').find('dachzeile') is not None):
                        try:
                            article.find('inhalt').find('titel-liste').find('dachzeile').text
                            kicker = article.find('inhalt').find('titel-liste').find('dachzeile').text
                            kicker = kicker.encode('utf-8').decode('utf-8') # save the string as unicode
                            kicker = kicker.strip() # strip whitespace on both sides
                            kicker = kicker.replace("\n", ' ') # replace line break (new line character) with space
                            kicker = kicker.replace("\t", ' ') # replace tab with space
                            kicker = ' '.join(kicker.split()) # substitue multiple whitespaces with single whitespace
                            
                            # if there is no period, colon, semicolon, exclamation, question, or quotation mark 
                            # at the end of the sentence, add period.
                            if kicker[-1] not in ['.', '!', ':', ';','?', '"']: 
                                kicker  = kicker  + '.'
                        except:
                            kicker = ''            
                             
                # TITLE
                title = ''
                if (article.find('inhalt').find('titel-liste') is not None):
                    if (article.find('inhalt').find('titel-liste').find('titel') is not None):
                        try:
                            article.find('inhalt').find('titel-liste').find('titel').text
                            title = article.find('inhalt').find('titel-liste').find('titel').text
                            title = title.encode('utf-8').decode('utf-8') # save the string as unicode
                            title = title.strip() # strip whitespace on both sides
                            title = title.replace("\n", ' ') # replace line break (new line character) with space
                            title = title.replace("\t", ' ') # replace tab with space
                            title = ' '.join(title.split()) # substitue multiple whitespaces with single whitespace
                            
                            # if there is no period, colon, semicolon, exclamation, question, or quotation mark 
                            # at the end of the sentence, add it.
                            if title[-1] not in ['.', '!', ':', ';', '?', '"']: 
                                title = title + '.' 
                            
                            if untertitel != '':
                                title = title + ' ' + untertitel # add the untertitel if present
                                
                            if kicker != '':
                                title = kicker + ' ' + title # add the kicker if present                         
                                                       
                            # In 1995-1998, the main text already includes the title.
                            if date[0:4] not in ['1995', '1996', '1997', '1998']:
                                paragraphs = paragraphs + title
                                
                        except:
                            title = ''
                            
                title_list.append(title)
                
                # ANNOTATION
                if article.find('inhalt').find('vorspann') is not None:
                    annot = article.find('inhalt').find('vorspann').text
                    annot = annot.encode('utf-8').decode('utf-8')
                    if annot is not None:
                        annot = annot.strip()
                        annot = annot.replace('\n', '')
                        annot = annot.replace('\t', '')
                        paragraphs = paragraphs + ' ' + annot
                
                # PARAGRAPHS
                if article.find('inhalt').find('text') is not None:
                    for par in article.find('inhalt').find('text').findall('p'):
                        par_text = ''
                        # the second condition removes paragraphs like '-------'
                        if (par.text is not None) and ('-----' not in par.text): 
                            par_text = par.text.encode('utf-8').decode('utf-8')
                            par_text = par_text.strip()
                            par_text = par_text.replace("\n", ' ')
                            par_text = par_text.replace("\t", ' ')
                                                            
                            # If the last paragraph is about the copyright, exclude it.
                            if par_text in ('SZ-ONLINE: Alle Rechte vorbehalten - Süddeutscher Verlag GmbH.', 
                                            'SZ-ONLINE: Alle Rechte vorbehalten - Sueddeutscher Verlag GmbH',
                                            'SZ-ONLINE: Alle Rechte vorbehalten - Süddeutscher Verlag GmbH'):
                                par_text = ''
                            
                            paragraphs = paragraphs + ' ' + par_text
                            
                            # replace a non-breaking space with a space
                            paragraphs = re.sub('\xa0', ' ', paragraphs)
                            # remove soft-hyphen
                            paragraphs = re.sub('\xad', ' ', paragraphs)
                            # remove "►", a right-pointing triangle
                            paragraphs = re.sub('&#9658;', ' ', paragraphs)
                            
                            # make sure that there are no extra white spaces
                            paragraphs = ' '.join(paragraphs.split()) 
                texts.append(paragraphs)
        
        # convert string to integer
        day = list(map(int, day)) 
        month = list(map(int, month))
        year = list(map(int, year))
        newspaper_2 = ['SZ']*len(day) # add column with nespaper name ('SZ') (same name across all articles)
    
        data_intermediate = pd.DataFrame({'year' : year,
         'month' : month,
         'day' : day,
         'newspaper': newspaper,
         'newspaper_2': newspaper_2,
         'texts': texts,
         'rubrics': rubrics,
         'title': title_list,
         'quelle_texts': quelle_texts,
         'page': page_list                                
          })
        
        if data is not None:
            data = data.append(data_intermediate, ignore_index = True)
        else:
            data = data_intermediate
        
        
    return data