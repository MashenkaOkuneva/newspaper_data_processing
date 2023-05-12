# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:08:30 2020

@author: mokuneva
"""
from bs4 import BeautifulSoup
import pandas as pd
import os
import re

def dpa_load(folder):
    
    """This is a function which will load dpa data from one folder."""
    
    data = None
    # create lists for information to store
    day = []    # day of publication
    month = []  # month of publication
    year = []   # year of publication
    texts = []  # articles
    rubrics = []    # section: Politics vs Economy
    file_names = [] # names of the files
    source = [] # source: dpa vs afx
    keywords = []   # keywords associated with an article
    title_list = []   # title of the article 
    city = []   # which city the news article refers to
    genre = []  # journalistic genre, e.g., chronology, story, table
    wordcount = []  # word count from the XML files
    topic = []  # topic: Finance vs Economy and Politics (afx vs dpa)
                # (same as source, but based on the folder where the files are stored)
    par_list = []
    
    # for each file in a particular folder   
    for s in [s for s in os.listdir(folder)]:
            # open a file
            infile = open(folder + '\\' + s, "r", encoding='utf-8') 
            
            # TOPIC
            # financial news (dpa-afx source) vs news about 
            # Economy and Politics (dpa source)
            if 'afx' in folder:
                topic = 'afx'
            else:
                topic = 'WiPo'
            
            # read the content of the XML file
            contents = infile.read()
            # use BeautifulSoup to parse the XML file
            soup = BeautifulSoup(contents, 'xml')
            
            # FILE NAME
            # add the name of the XML file to the list
            file_names.append(s)
            
            # TEXT LENGTH
            # split the tokens by space and calculate the length of the list
            # the second approach to calculate the text length from the Handelsblatt_clean notebook            
            #if soup.find("text") is not None:
            #    res_len = len(text_new.split(" "))
            #    length.append(res_len)
            #else:
            #    length.append('')
            
            # DAY/MONTH/YEAR
            # extract the date if there is a text tag in the XML
            if soup.find("text") is not None:
                # extract the date
                date = soup.find("date")
                # day as an integer
                day.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[2]))
                # month as an integer
                month.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[1]))
                # year as an integer
                year.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[0]))                
            else:
               day.append('')
               month.append('')
               year.append('')
               
            # SECTION
            # Politics and Economy sections
            if  soup.find("ressort") and soup.find("ressort").get_text() is not None:
                rubrics.append(soup.find("ressort").get_text())
            else:
                rubrics.append('')
            
            # SOURCE (dpa vs afx)
            # if there is text inside the source tag
            if soup.find("source") and soup.find("source").get_text() is not None and soup.find("source").get_text()!= u'':
                source.append(soup.find("source").get_text())
            # if there is no text inside the source tag but there is text inside the credit tag
            # credit also contains information about the source
            elif soup.find("source").get_text() == u'' and soup.find("credit").get_text() is not None:
                source.append(soup.find("credit").get_text())
            else:
                source.append('')
            
            # CITY
            # Which city the news refers to
            if soup.find("city") and soup.find("city").get_text() is not None:
                city.append(soup.find("city").get_text())
            else:
                city.append('')
            
            # GENRE
            # e.g., table, story, announcement of upcoming news 
            if soup.find("genre") and soup.find("genre").get_text() is not None:
                genre.append(soup.find("genre").get_text())
            else:
                genre.append('')
            
            # WORD COUNT
            # word count from the XML files
            if soup.find('wortanzahl') and soup.find('wortanzahl').get_text() is not None:
                wordcount.append(soup.find('wortanzahl').get_text())
            else:
                wordcount.append('')
            
            # KEYWORDS
            keywords_new = ''
            if soup.find("keywords") is not None and len(soup.find("keywords").findAll("keyword")) != 0:
                try:
                    keywords_find = soup.find("keywords").findAll("keyword") 
                    for k in keywords_find:
                        k = k.get_text()
                        k = k.encode('utf-8').decode('utf-8')
                        k = k.strip()
                        k = k.replace("\n", ' ')
                        k = k.replace("\t", ' ')
                        keywords_new = keywords_new + ' ' + k
                        keywords_new = ' '.join(keywords_new.split()) 
                except:
                    keywords_new = ''
            keywords.append(keywords_new)
            
            # TEXT OF THE ARTICLE
            # text consists of title + main_text (paragraphs combined together)
            text_new = ""
            
            # TITLE
            # strings helping to identify multiple articles that should be treated differently
            strings_ma = ['dpa-Nachrichtenüberblick', 'Nachrichtenüberblick', 'Kurznachrichten Wirtschaft', 'Analysten-Einstufungen', 'ANALYSTEN-EINSTUFUNGEN']
            title = ''
            # If there is a 'title' tag in the XML data, and if the title is not empty
            if soup.find("title") and soup.find("title").get_text() is not None and soup.find("title").get_text()!= u'':
                title = soup.find("title").get_text()
                title = title.encode('utf-8').decode('utf-8') # save the string as unicode
                title = title.strip() # strip whitespace on both sides
                title = title.replace("\n", ' ') # replace line break (new line character) with space
                title = title.replace("\t", ' ') # replace tab with space
                title = ' '.join(title.split()) # substitue multiple whitespaces with single whitespace
                
                # if there is no period, colon, semicolon, exclamation, question, or quotation mark 
                # at the end of the sentence, add period.
                if title != '':
                    if title[-1] not in ['.', '!', ':', ';', '?', '"']: 
                        title = title + '.'
                # add the title only if an article does not contain multiple articles
                if all(s not in title for s in strings_ma) and all(s not in keywords_new for s in strings_ma) and all(s not in soup.find("genre").get_text() for s in strings_ma): 
                    text_new = text_new + title
            # add the title to the corresponding list    
            title_list.append(title)
            
            # PARAGRAPHS
            if soup.find("text") is not None: # If there is a 'text' tag in the XML file
                # If there is at least one paragraph with the tag "h:p"                                               
                if len(soup.find("text").findAll("h:p", {"class":""})) != 0:
                    try:
                        # extract all the paragraphs as one list
                        paragraphs = soup.find("text").findAll("h:p", {"class":""})
                    except:
                        paragraphs = ''
                # If there is at least one paragraph with the tag "p"             
                elif len(soup.find("text").findAll("p", {"class":""})) != 0:
                    try:
                        # extract all the paragraphs as one list
                        paragraphs = soup.find("text").findAll("p", {"class":""})
                    except:
                        paragraphs = ''
                # If there are no paragraph tags        
                else:
                    try:
                        # extract the text and add it to a list
                        paragraphs = [soup.find("text")]
                    except:
                        paragraphs = ''
                
                par_list_text = []
                # clean the paragraphs
                for p in paragraphs:
                    # replace all the line breaks with space
                    if p.find("br") is not None:
                        for br in p.findAll('br'):
                            br.replace_with(" ")
                    p = p.get_text()    # extract the text 
                    p = p.encode('utf-8').decode('utf-8') # save the string as unicode
                    # pre-process further only if an article does not contain multiple articles
                    if all(s not in title for s in strings_ma) and all(s not in keywords_new for s in strings_ma) and all(s not in soup.find("genre").get_text() for s in strings_ma):      
                        p = p.strip()  # strip whitespace on both sides
                        p = p.replace("\n", ' ') # replace line break (new line character) with space 
                        p = p.replace("\t", ' ') # replace tab with space
                    # If an artilce contains multiple articles, use the word 'PARAGRAPH'
                    # to separate paragraphs for easier splitting.
                    if all(s not in title for s in strings_ma) and all(s not in keywords_new for s in strings_ma) and all(s not in soup.find("genre").get_text() for s in strings_ma):    
                        text_new = text_new + ' ' + p
                    else:
                        text_new = text_new + ' PARAGRAPH ' + p
                    # replace a non-breaking space with a space
                    text_new = re.sub('\xa0', ' ', text_new)
                    # remove soft-hyphen
                    text_new = re.sub('\xad', ' ', text_new)
                    # pre-process further only if an article does not contain multiple articles
                    if all(s not in title for s in strings_ma) and all(s not in keywords_new for s in strings_ma) and all(s not in soup.find("genre").get_text() for s in strings_ma): 
                        text_new = ' '.join(text_new.split()) # make sure that there are no extra white spaces
                    par_list_text.append(p)
            texts.append(text_new)
            par_list.append(par_list_text)
              
    data = pd.DataFrame({'texts' : texts,
                     'file': file_names,
                     'day':day,
                     'month':month,
                     'year':year,
                     'rubrics': rubrics,
                     'source':source,
                     'keywords':keywords,
                     'title':title_list,
                     'city':city,
                     'genre':genre,
                     'wordcount':wordcount,
                     'topic':topic,
                     'paragraphs': par_list 
          })
    return data        
    