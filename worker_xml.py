# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 16:08:30 2020

@author: mokuneva
"""
from bs4 import BeautifulSoup
import pandas as pd
import os

def worker_xml(folder):
    
    data = None
    day = []
    month = []
    year = []
    texts = []
    rubrics = []
    file_name = []
    length = []
    source = []
    keywords = []
    title = []
    city = []
    genre = []
    wordcount = []
    topic = []
       
    for s in [s for s in os.listdir(folder) ]: #for each file in a particular folder
            infile = open(folder + '\\' + s, "r", encoding='utf-8') ###added encoding
            
            if 'afx' in folder:
                topic = 'afx'
            else:
                topic = 'WiPo'
            
            contents = infile.read()
            soup = BeautifulSoup(contents, 'xml')
            file_name.append(s)

            if soup.find("text") is None:
                
                texts.append('')

            elif len(soup.find("text").findAll("h:p", {"class":""})) != 0:
                try:
                    paragraphs = soup.find("text").findAll("h:p", {"class":""})
                    text_new = u''
                    for p in paragraphs:
                        if p.find("br") is not None:
                            for br in p.findAll('br'):
                                br.replace_with(" ")
                        p = p.get_text() 
                        p = p.encode('utf-8').decode('utf-8')
                        p = p.lstrip()
                        p = p.strip()
                        p = p.replace("\n", ' ')  
                        p = p.replace("\t", ' ')
                        text_new = text_new + ' ' + p
                        text_new = ' '.join(text_new.split())
                    texts.append(text_new)
                except:
                    texts.append('')

            elif len(soup.find("text").findAll("h:p", {"class":""})) != 0:
           
                try:
                    paragraphs = soup.find("text").findAll("p", {"class":""})
                    text_new = u''
                    for p in paragraphs:
                        if p.find("br") is not None:
                            for br in p.findAll('br'):
                                br.replace_with(" ")
                        p = p.get_text() 
                        p = p.encode('utf-8').decode('utf-8')
                        p = p.lstrip()
                        p = p.strip()
                        p = p.replace("\n", ' ')
                        p = p.replace("\t", ' ')
                        text_new = text_new + ' ' + p
                        text_new = ' '.join(text_new.split())
                    texts.append(text_new)
                except:
                    texts.append('')
            else:
                
                try:
                    
                    text_new = soup.find("text").get_text()
                    text_new = text_new.encode('utf-8').decode('utf-8')
                    text_new = text_new.lstrip()
                    text_new = text_new.strip()
                    text_new = text_new.replace(u"\n", u' ')
                    text_new = text_new.replace(u"\t", u' ')
                    text_new = text_new.replace(u'\xab', u'')
                    text_new = text_new.replace(u'\xbb', u'')
                    text_new = text_new.replace(u'\xa0', u'')
                    texts.append(text_new)
                    
                except:
                    texts.append('')
            
            if soup.find("text") is not None:
                res_len = len(text_new.split(" "))
                length.append(res_len)
            else:
                length.append('')

            if soup.find("text") is not None:
                
                date = soup.find("date")
                day.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[2]))
                month.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[1]))
                year.append(int(date.get_text().rsplit(' ', 2)[0].split('-',3)[0]))
                
            else:
               day.append('')
               month.append('')
               year.append('')
            
            if  soup.find("ressort") and soup.find("ressort").get_text() is not None:
                rubrics.append(soup.find("ressort").get_text())
            else:
                rubrics.append('')
                
            if soup.find("source") and soup.find("source").get_text() is not None:
                source.append(soup.find("source").get_text())
            else:
                source.append('')
                
            if soup.find("title") and soup.find("title").get_text() is not None:
                title.append(soup.find("title").get_text())
            else:
                title.append('')
                
            if soup.find("city") and soup.find("city").get_text() is not None:
                city.append(soup.find("city").get_text())
            else:
                city.append('')
                
            if soup.find("genre") and soup.find("genre").get_text() is not None:
                genre.append(soup.find("genre").get_text())
            else:
                genre.append('')
                
            if soup.find('wortanzahl') and soup.find('wortanzahl').get_text() is not None:
                wordcount.append(soup.find('wortanzahl').get_text())
            else:
                wordcount.append('')

            if soup.find("keywords") is not None and len(soup.find("keywords").findAll("keyword")) != 0:
                try:
                    keywords_find = soup.find("keywords").findAll("keyword") 
                    keywords_new = u''
                    for k in keywords_find:
                        k = k.get_text()
                        k = k.encode('utf-8').decode('utf-8')
                        k = k.lstrip()
                        k = k.strip()
                        k = k.replace("\n", ' ')
                        k = k.replace("\t", ' ')
                        keywords_new = keywords_new + ' ' + k
                    keywords.append(keywords_new)
                except:
                    keywords.append(u"")
            else:
                keywords.append(u"")
                
    data = pd.DataFrame({'texts' : texts,
                     'file': file_name,
                     'length': length,
                     'day':day,
                     'month':month,
                     'year':year,
                     'rubrics': rubrics,
                     'source':source,
                     'keywords':keywords,
                     'title':title,
                     'city':city,
                     'genre':genre,
                     'wordcount':wordcount,
                     'topic':topic
          })
    return data        
    