# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取文本,并进行过滤



def getfile(path,func):
	file1 = open (path)
	temp=set()
	while True:
		line =file1.readline()
		if not line:
			break;
		item=func(line)
		temp|=item
	file1.close()
	return  temp

def writefile(word,filename):
	f = file(filename,'w') 	
	for j in word:
		f.write(j+'\n')
	f.close()

def filterd(line):

	ary=line.split(',')
	# print ary[0]

	return set([ary[0]])
writefile(getfile('scriptdickey.txt',filterd),'scriptkey.txt')