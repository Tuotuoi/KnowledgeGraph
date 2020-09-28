#!/usr/bin/env python
# coding=utf-8
import jieba
import re
from jieba import analyse
def merge_two_list(a, b):
    '''
        c = merge_two_list(["你好","很好","非常好"],["abc","ade","abcd","abc",'efg']
        ----> c = ['你好', 'abc', '很好', 'ade', '非常好', 'abcd', 'abc', 'efg']
    :param a:
    :param b:
    :return: c
    '''
    # 传入两个list,将b中元素分别从a[i]位置插入到a中,
    c = []
    len_a, len_b = len(a), len(b)
    minlen = min(len_a, len_b)
    for i in range(minlen):
        c.append(a[i])
        c.append(b[i])

    if len_a > len_b:
        for i in range(minlen, len_a):
            c.append(a[i])
    else:
        for i in range(minlen, len_b):
            c.append(b[i])
    return c

sentence = open('/home/luojinxv/1.Cprogram/KnowledgeGraph/1.knowledgegraph_军队编制.txt','r', encoding="utf8")
regex1 = r'(.*?)年(.*?)月(.*?)日'
regex2 = r'第(.*?)军'
regex3 = r'第(.*?)路军'
p1 = re.compile(regex1)
p2 = re.compile(regex2)
p3 = re.compile(regex3)
for line in sentence.readlines():
    result1 = p1.findall(line)
    if result1:
        regex_re1 = result1
        line = p1.sub("FLAG1", line)
        print(line)
    result2 = p2.findall(line)
    if result2:
        line = p2.sub("FLAG2", line)
        print(line)
    result3 = p3.findall(line)
    if result3:
        line = p3.sub("FLAG3", line)
        print(line)

jieba.load_userdict('/home/luojinxv/1.Cprogram/KnowledgeGraph/dict.txt')
jieba.enable_parallel(4)
#words = jieba.cut(sentence=sentence, cut_all = False)
#words = jieba.cut_for_search(sentence=sentence, HMM=True)
word_list = jieba.cut(sentence)  # 默认精准分词
result = ''.join(word_list)
if "FLAG1" in result:
            result = result.split("FLAG1")
            result = merge_two_list(result, result1)
            result = "".join(result)
if "FLAG2" in result:
            result = result.split("FLAG2")
            result = merge_two_list(result, result2)
            result = "".join(result)
if "FLAG3" in result:
            result = result.split("FLAG3")
            result = merge_two_list(result, result3)
            result = "".join(result)

key_words = analyse.extract_tags(sentence=sentence, topK=20, withWeight=False,allowPOS=())
print(result)
print(key_words)
