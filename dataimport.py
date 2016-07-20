# !/usr/bin/env python
# -*- coding: utf-8 -*-


from DButil import db











sql="insert into testdata(ip,port,timesearch,state,name,product,version,script,detail,head,portnumber,hackinfo,keywords,disclosure)  SELECT ip,port,timesearch,state,name,product,version,script,detail,head,portnumber,hackinfo,keywords,disclosure FROM snifferdata where name='http' order by timesearch desc limit 0,100000"

result = db.execute(sql)
if 0 == result:
    print 'success'