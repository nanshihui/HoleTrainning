# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用keras进行数据预处理
import keras
from keras.preprocessing.text import base_filter
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.preprocessing import text

text="""imap-ntlm-info
drda-info
"""
def test(text):
	print keras.preprocessing.text.text_to_word_sequence(text, 
	filters=base_filter(), lower=True, split=" ")
	print keras.preprocessing.text.one_hot(text, 5,
	filters=base_filter(), lower=True, split=" ")
# test(text)




