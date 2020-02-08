import logging
import json
import gensim.downloader as api

info = api.info()

logging.basicConfig(
    format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

for model_name, model_data in sorted(info['models'].items()):
    print(
        '%s (%d records): %s' % (
            model_name,
            model_data.get('num_records', -1),
            model_data['description'][:40] + '...',
        )
    )

model = api.load('fasttext-wiki-news-subwords-300')
model.most_similar('united way')