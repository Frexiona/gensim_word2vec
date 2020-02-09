# Knowlege Graph based on Gensim

This is a test project to mimic the performance of the knowledge graph

## Installation

Install [requirements.txt](https://github.com/Frexiona/gensim_word2vec/blob/master/requirements.txt)
```bash
pip install requirements.txt
```

## Project Structure

### Word Embedding (Pretrained & Selftrained)

* **Pretrained [pretrained_model.py](https://github.com/Frexiona/gensim_word2vec/blob/master/wiki_model/pretrained_model.py)**

Find relavant words by using pretrained model (Fast & Outdated)

* **Selftrained [word2vec_trainer.py](https://github.com/Frexiona/gensim_word2vec/blob/master/wiki_model/word2vec_trainer.py)**

Find relavant words by using latest Wiki corpus trained model (Slow & Latest)

### Google Search Engine

Return Google search links related to query and relavant words

### Keywords Extracter

Implement keyword extraction algorithm based on **Text Rank** on the content of links obtained through Google Search Engine