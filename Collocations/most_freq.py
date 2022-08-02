# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:13:06 2022

@author: mokuneva
"""
import nltk
import itertools
import codecs

def most_freq(input_list, items, freq, print_output=True):
    """
    This function outputs two-words (three-words) collocations whose frequencies are above 100 (50).
    """
    fdist = nltk.FreqDist(itertools.chain(*input_list))
    most_common = [word for (word, count) in fdist.most_common()[:2000] if count >= freq]
    count = [count for (_, count) in fdist.most_common()[:2000] if count >= freq]
    mfreq = zip(most_common, count)
    if print_output:
        if items == 'bigrams':   
            with codecs.open('bigrams.csv', 'w', 'utf-8-sig') as f:
                for p in mfreq:
                    f.write("%s,%d\n" % (p[0], p[1]))
        elif items == 'trigrams':
            with codecs.open('trigrams.csv', 'w', 'utf-8-sig') as f:
                for p in mfreq:
                    f.write("%s,%d\n" % (p[0], p[1]))
    return mfreq