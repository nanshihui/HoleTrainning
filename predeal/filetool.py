# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 读取文本,并进行过滤
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


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
def chineseout(line):
	import re,chardet
	# print line
	# print type(line),len(line)
	if line is None or line =='':

		return line

	chardit1 = chardet.detect(line)

	if chardit1['encoding'] is None:
		return line
	if chardit1['encoding']!='utf-8':
		try:
			line=line.decode(chardit1['encoding']).encode('utf-8')
		except Exception,e:
			print e
	item="\xe4[\xb8-\xbf][\x80-\xbf]|[\xe5-\xe8][\x80-\xbf][\x80-\xbf]|\xe9[\x80-\xbd][\x80-\xbf]|\xe9\xbe[\x80-\xa5]"
	replacedStr = re.sub(item, " ", line)
	
	return line
	
chineseout('输入网址的某些地方有as数据库到你看叫事地方卡萨丁上电脑放看见你误，可能是因为')
# writefile(getfile('scriptdickxey.txt',filterd),'scriptkey.txt')d