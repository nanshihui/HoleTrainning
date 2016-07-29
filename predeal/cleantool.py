# !/usr/bin/env python
# -*- coding: utf-8 -*-


def getfile(path):
	file1 = open (path)
	temp=set()
	while 1:
		line =file1.readline()
		if not line:
			break;
		array= line.split(',')
		temp|=set(array)
	file1.close()
	f = file(path,'w') 
	for word in temp:
	
		f.write(word)
	f.close()
getfile('component.txt')