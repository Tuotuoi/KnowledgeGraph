#!/usr/bin/env python
# coding=utf-8
import jieba
from jieba import analyse
sentence = open('/home/luojinxv/1.Cprogram/KnowledgeGraph/1.knowledgegraph_军队编制.txt','rb').read()
#jieba.load_userdict('/home/luojinxv/1.Cprogram/KnowledgeGraph/dict.txt')
jieba.enable_parallel(4)
#words = jieba.cut(sentence=sentence, cut_all = False)
#words = jieba.cut_for_search(sentence=sentence, HMM=True)
word_list = jieba.lcut(sentence=sentence)  # 默认精准分词
result = ' '.join(word_list)
print(result)
key_words = analyse.extract_tags(sentence=sentence, topK=20, withWeight=False,allowPOS=())
print(key_words)
