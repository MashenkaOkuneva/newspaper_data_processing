# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:48:02 2019

@author: mOkuneva
"""
import nltk
import pickle
from itertools import chain
with open('nltk_pos.pickle', 'rb') as f:
    tagger = pickle.load(f)
   
nltk.data.path.append('E:\\Userhome\\mokuneva\\newspaper_data_processing\\Collocations\\nltk_data')



class BiTriDic():
    
    """
    This class creates a list of two-word and three-word collocations.
    """
        
    def __init__(self, doc):
        self.sents = [nltk.sent_tokenize(doc.replace(u'\ufeff', ''))]
            
    def tagger(self):
        def tag(sents):
            return list(chain.from_iterable([tagger.tag(nltk.word_tokenize(s)) for s in sents]))
        self.sents = map(tag, self.sents)
        
    def bigr(self):
        def bi(sents):
            return [a[0] + ' ' + b[0] for (a,b) in nltk.bigrams(sents) if \
                (a[1] == 'ADJA' or a[1] == 'ADJD') and (b[1] == 'NN' or b[1] == 'NE' or b[1] == 'CARD') and (b[0] != u'%') or \
                (a[1] == 'NN' or a[1] == 'NE' or a[1] == 'CARD') and (b[1] == 'NN' or b[1] == 'NE' or b[1] == 'CARD') and (b[0] != u'%') and (b[0] != 'of')]
        self.bigr = map(bi, self.sents)
        
    def trigr(self):
        def trigr(sents):
            return [a[0] + ' ' + b[0] + ' ' + c[0] for (a,b,c) in nltk.trigrams(sents) if \
                (a[1] == 'NN' or a[1] == 'NE' or a[1] == 'CARD') and (b[1] == 'APPR' or b[1] == 'APPRART') and (c[1] == 'NN' or c[1] == 'NE' or c[1] == 'CARD')  and (a[0] != u'%') or \
                (a[1] == 'NN' or a[1] == 'NE' or a[1] == 'CARD') and (b[1] == 'PPOSAT' or b[1] == 'ART' or b[1] == 'PIAT' or b[1] == 'PDAT') and (c[1] == 'NN' or c[1] == 'NE' or c[1] == 'CARD') and (a[0] != u'%') or \
                (a[1] == 'ADJA' or a[1] == 'ADJD') and (b[1] == 'ADJA' or b[1] == 'ADJD') and (c[1] == 'NN' or c[1] == 'NE' or c[1] == 'CARD') and (a[0] != u'%')]
        self.trigr = map(trigr, self.sents)
        