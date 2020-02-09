# -*- coding: utf-8 -*-
# @Time    : 08/02/2020
# @Author  : Haolin Zhang
# @File    : knowledge_graph_wrapper.py
# @Software: VS Code

import utilities.google_search as search
import utilities.keywords_extraction as keywords
import wiki_model.pretrained_model as pretrained_word2vec

if __name__ == '__main__':
    keyword = 'IBM'
    query = ['ireland', 'IBM', 'Trafficking']
    topn = 50
    restrict_vocab = 10000
    entity_list = list()

    '''
    Word Embedding
    '''
    # entities: List of tuples
    entities = pretrained_word2vec.get_relavant_entities(
        query, topn, restrict_vocab)
    for each in entities:
        entity_list.append(each[0])

    '''
    Google Search Engine
    '''
    google_search_links = list()

    for each_entity in entity_list:
        google_query = keyword + ' ' + each_entity
        google_search_entity = {
            'query': google_query,
            'links': search.google_search(google_query)
        }
        google_search_links.append(google_search_entity)
    
    # print(google_search_links)

    '''
    Keywords Extraction
    '''