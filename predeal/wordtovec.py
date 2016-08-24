# !/usr/bin/env python
# -*- coding: utf-8 -*-

from gensim.corpora import Dictionary
from gensim.models import LdaModel
import gensim
import re

def get_stop_words_set(file_name):  
    with open(file_name,'r') as file:  
        return set([line.strip() for line in file])  
  
def get_words_list(file_name,stop_word_file):  
    stop_words_set = get_stop_words_set(stop_word_file)  
    print "共计导入 %d 个停用词" % len(stop_words_set)  
    word_list = []  
    with open(file_name,'r') as file:  
        for line in file:  
            tmp_list = list(jieba.cut(line.strip(),cut_all=False))  
            word_list.append([term for term in tmp_list if str(term) not in stop_words_set]) #注意这里term是unicode类型，如果不转成str，判断会为假  
    return word_list  
def getfile(path,func):
    word={}
    file1 = open (path)
    temp=set()
    l=0
    train_set=[]
    while 1:
        l=l+1
        line =file1.readline()
        if not line:
            break;
        print l
        ary=func(line)
        # print ary
        train_set.append(ary)

    file1.close()
    model = gensim.models.Word2Vec(train_set, min_count=1)
    model.save('model_mysql.bin')
#     dictionary = Dictionary(train_set)
#     corpus = [ dictionary.doc2bow(text) for text in train_set]

# # lda模型训练
#     lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=20)
#     lda.print_topics(20)
def dealwiththeline(line):
    line=line.lower()
    line=confir(line)
    # line=line.decode('string_escape')
    import filetool
    line=filetool.chineseout(line)
    array=  re.split("[ {,:}'()\n\r\\\"<>/-]", line)
    return array

def confir(str):
    for i in range(0,32):
        str = str.replace(chr(i),' ')
    for i in range(127,256):
        str = str.replace(chr(i),' ')
    return  str
import string

def clean(instr):
    return instr.translate(None, string.punctuation + ' ')
# getfile('mysqlkey.txt',dealwiththeline)
new_model = gensim.models.Word2Vec.load('model_mysql.bin')
# print new_model.doesnt_match("not allowed".split())
# content="5.5.44-MariaDB-log\05­\0\0WLS?}zn8\0ÿ÷!\0 \0\0\0\0\0\0\0\0\0\0l6g(/P)xC&3l\0mysql_native_password\0}    mysql"
# content=content.lower()
# print ''.join(e for e in content if e.isalnum())
print new_model['mysql']
# searchary=re.split("[ {,:}'()\n\r\\\"<>/-]", confir(content))
# searchary= list(set(searchary))
# print searchary
# print new_model.most_similar(searchary,  topn=20)
# print new_model.similarity('ssh','ftp')
# print new_model['smtp']
# print new_model.accuracy('nohttpreal.txt')

