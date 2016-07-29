# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from BaseUtil.log import  INFO
import re,collections
def getfile(path):
	word={}
	file1 = open (path)
	temp=set()
	l=0
	while 1:
		l=l+1
		line =file1.readline()
		if not line:
			break;
		print l
		array=dealwiththeline(line)
		if '\\n' in array:

			INFO(array)
			INFO(line)

		for i in array:
			# print i
			if word.get(i,0)>0:
				word[i]=word[i]+1
			else:
				word[i]=1
		
	file1.close()
	return word
def dealwiththeline(line):
	line=line.lower()
	line=line.decode('string_escape')

	array=	re.split("[ {,:}'()\n\r\\\n\"]", line)
	return array
def test():
	line="""{'http-methods': '\\n  Supported Methods: OPTIONS TRACE GET HEAD POST\\n  Potentially risky methods: TRACE', 'http-title': '\\\\xE7\\\\xBD\\\\x91\\\\xE7\\\\xAB\\\\x99\\\\xE8\\\\xAE\\\\xBF\\\\xE9\\\\x97\\\\xAE\\\\xE6\\\\x8A\\\\xA5\\\\xE9\\\\x94\\\\x99', 'http-server-header': 'Microsoft-IIS/7.5', 'http-favicon': 'Unknown favicon MD5: 00E2A50F6C8EF4B07A731AC28F5A282F'}"""
	array=dealwiththeline(line)
	print array
# test()
def sort_by_count(d):  
	#字典排序  
	d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))  
	return d  
def writefile(word):
	f = file('hzwords','w') 	
	for j in word:
		f.write(j+','+str(word[j])+'\n')
	f.close()
d=getfile('script.txt')
d=sort_by_count(d)
writefile(d)

# test()
