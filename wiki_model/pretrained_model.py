import logging
import json
import gensim.downloader as api

MODEL = api.load('fasttext-wiki-news-subwords-300')

# info = api.info()
# logging.basicConfig(
#     format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# for model_name, model_data in sorted(info['models'].items()):
#     print(
#         '%s (%d records): %s' % (
#             model_name,
#             model_data.get('num_records', -1),
#             model_data['description'][:40] + '...',
#         )
#     )


def get_relavant_entities(query, topn, restrict_vocab=None):
    '''
    query: list of keywords
    topn: number of return entities
    restrict_vocab: is an optional integer which limits the range of vectors
    which are searched for most-similar values. For example,
    estrict_vocab=10000 would only check the first 10000 word vectors in the vocabulary order.
    (This may be meaningful if you’ve sorted the vocabulary by descending frequency.)
    '''
    return MODEL.most_similar(positive=['ireland', 'IBM', 'Trafficking'], topn=50, restrict_vocab=restrict_vocab)


if __name__ == '__main__':
    query = ['ireland', 'IBM', 'Trafficking']
    topn = 50
    restrict_vocab = 10000
    entities = get_relavant_entities(query, topn, restrict_vocab)
    for each in entities:
        print(type(each))
        print(each[0])
        print(each)
