# -*- coding: utf-8 -*-
# @Time    : 28/01/2020
# @Author  : Haolin Zhang
# @File    : process_wiki.py
# @Software: PyCharm

import logging
import os.path
import six
import sys

from gensim.corpora import WikiCorpus

if __name__ == '__main__':
    # sys.argv is a list in Python, which contains the command-line arguments passed to the script
    # sys.argv[0] is FILE PATH
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)

    # Creating a StreamHandler with a default Formatter and adding it to the root logger
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info(f"running {' '.join(sys.argv)}")

    # Check and process input arguments
    if len(sys.argv) != 3:
        print("Using: python process_wiki.py enwiki-latest-pages-articles.xml.bz2 wiki.en.text")
        sys.exit(1)
        
    inp, outp = sys.argv[1:3]
    space = ' '
    i = 0

    output = open(outp, 'w')
    wiki = WikiCorpus(inp, lemmatize=False, dictionary={})
    for text in wiki.get_texts():
        output.write(space.join(text) + "\n")

        i += 1
        if (i % 10000 == 0):
            logger.info("Saved " + str(i) + " articles")
    
    output.close()
    logger.info("Finished Saved " + str(i) + " articles")
