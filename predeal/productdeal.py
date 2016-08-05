# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 从数据库中读取字段,并降序排列到文本
import sys
sys.path.append("..")
from DButil import db
def getlabel(label):
    f = file(label+'.txt','w')
    # sql="SELECT product,count(*) FROM datap.snifferdata group by product order by count(*) desc limit 0,1000"
    sql="SELECT %s,count(*) FROM traindata group by %s order by count(*) desc limit 0,1000" %(label,label)
    result=db.iter(sql)
    for i in result:
    	    # f.write(str(i[label])+','+str(i['count(*)'])+'\n')
    	    f.write(str(i[label])+'\n')
    # product=result['product']
    # num=result['count(*)']
    f.close()
def getdetail():

    f = file('unhttpdetail.txt','w')
    # sql="SELECT product,count(*) FROM datap.snifferdata group by product order by count(*) desc limit 0,1000"
    sql="SELECT %s,count(*) FROM traindata group by %s order by count(*) desc limit 0,1000" %(label,label)
    result=db.iter(sql)
    for i in result:
            # f.write(str(i[label])+','+str(i['count(*)'])+'\n')
            f.write(str(i[label])+'\n')
    # product=result['product']
    # num=result['count(*)']
    f.close()



# getlabel('product')
# getlabel('version')
# getlabel('port')
# getlabel('name')
getlabel('label')
getlabel('front')
getlabel('component')
getlabel('language')
getlabel('webapp')