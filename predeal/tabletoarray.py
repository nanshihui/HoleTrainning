# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 将文本的分词进行编号



def getcode(path,name):
	file1 = open (path)
	temp=set()
	i=1
	while 1:
		line =file1.readline()
		if not line:
			break;
		line=line.replace('\n','')
		name[line]=i
		i=i+1
	file1.close()
	return  name
name={}
scriptkey={}
port={}
name=getcode('name.txt',name)
scriptkey=getcode('scriptkey.txt',scriptkey)
port=getcode('port.txt',port)
