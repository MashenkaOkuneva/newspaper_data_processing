# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:42:57 2020

@author: mokuneva
"""
from gensim.utils import simple_preprocess
from gensim import corpora
from gensim.similarities import Similarity

# source: https://towardsdatascience.com/a-laymans-guide-to-fuzzy-document-deduplication-a3b3cf9a05a7
from random import randrange
def fuzzy_duplicates(inputs):
    # select a new dataframe corresponding to a particular month and year
    documents = inputs[2][(inputs[2]['year'] == inputs[0]) & (inputs[2]['month'] == inputs[1])]
    # reset the index of the DataFrame
    documents = documents.reset_index()
    # convert documents to a collection of words
    texts = [[text for text in simple_preprocess(doc, deacc=True)] for doc in documents.texts]
    # create dictionary
    dictionary = corpora.Dictionary(texts)
    # create corpus (bow representation)
    corpus = [dictionary.doc2bow(docString) for docString in texts]
    # crete a pairwise cosine similarity index
    index = Similarity(corpus=corpus,
                   num_features=len(dictionary),
                   output_prefix='on_disk_output_'+str(randrange(12)))
    
    #parse similarities
    doc_id = 0
    similar_docs = {}
    for similarities in index:
        similar_docs[doc_id] = list(enumerate(similarities))
        doc_id += 1
    
    # set a similarity cutoff threshold
    sim_threshold = 0.9
    
    # Find similar document and their corresponding indices
    delete_indices = []
    considered_pairs = []
    for doc_id, sim_doc_tuples in similar_docs.items():
        for sim_doc_tuple in sim_doc_tuples:
            sim_doc_id = sim_doc_tuple[0]
            sim_score = sim_doc_tuple[1]
            if (sim_score >= sim_threshold) and (doc_id != sim_doc_id):
                if (doc_id, sim_doc_id) not in considered_pairs:
                    considered_pairs.append((doc_id, sim_doc_id))
                    considered_pairs.append((sim_doc_id, doc_id))
                    if len(documents['texts'][doc_id]) >= len(documents['texts'][sim_doc_id]):
                        delete_indices.append(documents['index'][sim_doc_id])
                    else:
                        delete_indices.append(documents['index'][doc_id])
    return delete_indices