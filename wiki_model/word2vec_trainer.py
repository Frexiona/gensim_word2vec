# -*- coding: utf-8 -*-
# @Time    : 29/01/2020
# @Author  : Haolin Zhang
# @File    : word2vec_trainer.py
# @Software: VS Code


import logging
import os.path
import sys
import multiprocessing

from gensim.corpora import  WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # Check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python word2vec_trainer.py")
        sys.exit(1)

    inp, outp = sys.argv[1:3]

    # Word2vec model configuration
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5, workers= multiprocessing.cpu_count())

    # Trip unneeded model memory = use (much) less RAM
    model.init_sims(replace=True)

    model.save(outp)