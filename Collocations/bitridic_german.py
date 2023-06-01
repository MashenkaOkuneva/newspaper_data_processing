# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 11:48:02 2019

@author: mOkuneva
"""
import nltk
import pickle
import os
from itertools import chain
with open('nltk_pos.pickle', 'rb') as f:
    tagger = pickle.load(f)
    
path_nltk = os.getcwd() + '\\\nltk_data'
nltk.data.path.append(path_nltk)


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
        
        def check_bigram_condition(a, b):
            """
            This function checks the POS conditions for a bigram.
            """
            condition_1 = (a[1] in ['ADJA', 'ADJD']) and (b[1] in ['NN', 'NE']) and (b[0] not in [u'%', u'S']) and (a[0] not in [u'lip', u'%'])
            condition_2 = (a[1] in ['NN', 'NE']) and (b[1] in ['NN', 'NE']) and (b[0] not in [u'%', u'of', u'W.', u'THE']) and (a[0] not in [u'of', u'W.', u'THE', u'lip', u'%'])
            return condition_1 or condition_2
    
        def bi(sents):
            return [a[0] + ' ' + b[0] for (a,b) in nltk.bigrams(sents) if check_bigram_condition(a, b)]
        
        self.bigr = map(bi, self.sents)
        
    def trigr(self):
        
        def check_trigram_condition(a, b, c):
            """
            This function checks the POS conditions for a trigram.
            """
            condition_1 = (a[1] in ['NN', 'NE']) and (b[1] in ['APPR', 'APPRART']) and (c[1] in ['NN', 'NE']) and (a[0] not in [u'%'])
            condition_2 = (a[1] in ['NN', 'NE']) and (b[1] in ['PPOSAT', 'ART', 'PIAT', 'PDAT']) and (c[1] in ['NN', 'NE']) and (a[0] not in [u'%']) and (c[0] not in [u'D'])
            condition_3 = (a[1] in ['ADJA', 'ADJD']) and (b[1] in ['ADJA', 'ADJD']) and (c[1] in ['NN', 'NE']) and (a[0] not in [u'%']) and (c[0] not in [u'S'])
            return condition_1 or condition_2 or condition_3
        
        def trigr(sents):
            return [a[0] + ' ' + b[0] + ' ' + c[0] for (a,b,c) in nltk.trigrams(sents) if check_trigram_condition(a, b, c)]
        
        self.trigr = map(trigr, self.sents)
        