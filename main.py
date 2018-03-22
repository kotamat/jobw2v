# -*- coding: utf-8 -*-
from gensim.models import KeyedVectors
import sys

MODEL_FILENAME = "w2v_crawled_jobs_100D.bin"
w2v = KeyedVectors.load_word2vec_format(MODEL_FILENAME, binary=True)

for line in iter(sys.stdin.readline,  ""):
    try:
        line = line.rstrip('\r\n')    # 改行が残ってるので削除
        line = line.decode('utf-8')

        tmp = w2v.most_similar(line, topn=30)
        for t in tmp:
            print t[0], t[1]
    except:
        print 'undefined word'

