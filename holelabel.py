
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 从数据库读取攻击信息字段分词并转存到另一张表里
import  json,re
from wordsutil import log

from wordsutil import keywordsmg as KeywordsUtil


def identifylabel(table='traindata'):
    from DButil import db
    sql='select count(*) from %s ' %table
    size=db.get(sql)['count(*)']
    i=0
    while i<size:


        sql = 'select ip,port,hackinfo from %s limit %d,1' % (table,i)
        result=db.get(sql)
        ip= result['ip']
        port=result['port']
        keywords=result['hackinfo']
        newwords,frontendset,componentset,languageset,headlabel,cityset,contentlength= KeywordsUtil.getkeyword(str(keywords))
        print i, ip, port, keywords
        newwords=",".join(map(str, newwords))

        newwords=newwords.replace('%s','')
        newwords=escapeword(newwords)


        componentmsg = ",".join(map(str, componentset))
        frontendmsg=",".join(map(str, frontendset))
        languagemsg = ",".join(map(str, languageset))
        headlabelmsg = ",".join(map(str, headlabel))

        result=1

        print newwords
        try:
            sql ="update  %s set label = '%s' ,contentlength= '%s',headlabel= '%s',place= '%s',front= '%s',component= '%s',language= '%s' where ip = '%s' and port = %s" %(table,newwords,contentlength,headlabelmsg,cityset,frontendmsg,componentmsg,languagemsg,ip,port)
            log.INFO(str(i)+'----'+str(ip)+'----'+str(port)+'----'+str(keywords))
            log.INFO(sql)
            result=db.execute(sql)
        except Exception,e:
            print e
            pass
        if 0== result:
            print 'success'
        i=i+1