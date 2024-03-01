# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 14:42:57 2020

@author: mokuneva
"""

# source: https://towardsdatascience.com/a-laymans-guide-to-fuzzy-document-deduplication-a3b3cf9a05a7

from gensim.utils import simple_preprocess
from gensim import corpora
from gensim.similarities import MatrixSimilarity
import pandas as pd

def fuzzy_duplicates_test(inputs):
    """ 
    This function returns a DataFrame containing information about 
    the duplicate articles, such as the texts, indices, and similarity scores.
    """ 
    # Select a new dataframe corresponding to a particular month and year.
    documents = inputs[2][(inputs[2]['year'] == inputs[0]) & (inputs[2]['month'] == inputs[1])]
    # Articles of the same type (e.g., the ones about stock market) are often
    # classified as near duplicates. Here are the types we want to keep in the
    # data set.
    types_keep = ['DEUTSCHE AKTIEN', 'Fortsetzung von Seite']
    documents = documents[~(documents.texts.str.contains('|'.join(types_keep)))]
    # There are a few articles that are classified to be duplicates, even though
    # they are not:
    exceptions = ['Im Vorstand der neuen DZ Bank sitzen künftig sechs Vorstandsmitglieder', 
                  'Stuttgart 21\\: Ist das Projekt noch zu stoppen\\?', 
                  'Deutschland ungeschminkt\\. Die deutsche Wirtschaft wächst',
                  'DEUTSCHLAND\\, TEIL 2\\. In Führung gehen',
                  'Die wundersame Geldvermehrung. Eigentlich soll die Europäische Zentralbank',
                  'Die Sicherheit in Europa ist trügerisch',
                  'MARIO DRAGHI\\. \\"Es gibt keinen Plan B\\"',
                  'Lotsen im Nebel\\.']
    documents = documents[~(documents.texts.str.contains('|'.join(exceptions)))]       
    # Reset the index of the DataFrame.
    documents = documents.reset_index()
    # Convert documents to a collection of words.
    texts = [[text for text in simple_preprocess(doc, deacc=True)] for doc in documents.texts]
    # Create a dictionary.
    dictionary = corpora.Dictionary(texts)
    # Create a corpus (BOW representation).
    corpus = [dictionary.doc2bow(docString) for docString in texts]
    # Build a pairwise cosine similarity index.
    index = MatrixSimilarity(corpus, num_features=len(dictionary))
    
    # Parse similarities.
    doc_id = 0
    similar_docs = {}
    for similarities in index:
        similar_docs[doc_id] = list(enumerate(similarities))
        doc_id += 1
    
    # Set a similarity cutoff threshold.
    sim_threshold = 0.93
    
    # Return the indices of duplicated articles.
    delete_indices = []
    considered_pairs = []
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    column6 = []
    for doc_id, sim_doc_tuples in similar_docs.items():
        for sim_doc_tuple in sim_doc_tuples:
            sim_doc_id = sim_doc_tuple[0]
            sim_score = sim_doc_tuple[1]
            if (sim_score >= sim_threshold) and (doc_id != sim_doc_id):
                if (doc_id, sim_doc_id) not in considered_pairs:
                    considered_pairs.append((doc_id, sim_doc_id))
                    considered_pairs.append((sim_doc_id, doc_id))
                    
                    doc1_date = documents['date'][doc_id]
                    doc2_date = documents['date'][sim_doc_id]
                    
                    if doc1_date == doc2_date:
                        if documents['word_count'][doc_id] >= documents['word_count'][sim_doc_id]:
                            delete_indices.append(documents['index'][sim_doc_id])
                            delete = documents['index'][sim_doc_id]
                            not_delete = documents['index'][doc_id]
                        else:
                            delete_indices.append(documents['index'][doc_id])
                            delete = documents['index'][doc_id]
                            not_delete = documents['index'][sim_doc_id]
                    else:
                        if doc1_date < doc2_date:
                            delete_indices.append(documents['index'][sim_doc_id])
                            delete = documents['index'][sim_doc_id]
                            not_delete = documents['index'][doc_id]
                        else:
                            delete_indices.append(documents['index'][doc_id])
                            delete = documents['index'][doc_id]
                            not_delete = documents['index'][sim_doc_id]
                            
                    
                    column1.append(documents['texts'][doc_id])  
                    column2.append(documents['texts'][sim_doc_id])
                    column3.append(inputs[2]['texts'][delete])
                    column4.append(not_delete)
                    column5.append(delete)
                    column6.append(sim_score)
                    
    test_df = pd.DataFrame({'doc': column1,
                             'duplicate': column2,
                             'shorter': column3,
                             'index_nd': column4,
                             'index_d': column5,
                             'similarity': column6})

    return test_df