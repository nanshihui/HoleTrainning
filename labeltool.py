# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 从数据库读取关键词字段分词并转存到另一张表里
import  json,re
from wordsutil import log

from wordsutil import keywordsmg as KeywordsUtil
def escapeword(word):
    import MySQLdb
    if word is None:
        return ''
    else:
        content=''
        content = str(MySQLdb.escape_string(word))
        return content
def identifylabel(table='traindata'):
    from DButil import db
    sql='select count(*) from %s ' %table
    size=db.get(sql)['count(*)']
    i=1837
    while i<size:


        sql = "select ip,port,keywords,script from %s  limit %d,1" % (table,i)
        result=db.get(sql)
        ip= result['ip']
        port=result['port']
        keywords=result['keywords']
        script=result['script']
        script=KeywordsUtil.getHttpGenerate(str(script))
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
            sql ="update  %s set label = '%s' ,contentlength= '%s',headlabel= '%s',place= '%s',front= '%s',component= '%s',language= '%s',webapp='%s' where ip = '%s' and port = %s" %(table,newwords,contentlength,headlabelmsg,cityset,frontendmsg,componentmsg,languagemsg,script,ip,port)
            log.INFO(str(i)+'----'+str(ip)+'----'+str(port)+'----'+str(keywords))
            log.INFO(sql)
            result=db.execute(sql)
        except Exception,e:
            print e
            pass
        if 0== result:
            print 'success'
        i=i+1
def addwork():
    from DButil import db
    sql='select count(*) from testdata '
    size=db.get(sql)['count(*)']
    import wordstask
    item=wordstask.getObject()
    for i in xrange(size):
        item.add_work([i])
def getlabel(table='traindata'):
    lableary = {}
    from DButil import db
    sql='select count(*) from %s ' % table
    size=db.get(sql)['count(*)']
    for i in xrange(size):
        sql = 'select ip,port,label from %s limit %d,1' % (table,i)
        result=db.get(sql)
        ip= result['ip']
        port=result['port']
        keywords=result['label']
        print i,keywords
        if keywords is not None:
            ary=keywords.split(',')
            for i in ary:
                if lableary.get(i,'')=='':
                    lableary[i]=1
                else:
                    lableary[i] =lableary[i]+1

    writefile(lableary,table)
def writefile(lableary,table='traindata'):
    f = file(table+'.txt','w')
    keyset=lableary.keys()
    for i in keyset:
        f.write(i+'------------------'+str(lableary[i])+'\n')
    f.close()
if __name__ == "__main__":
    identifylabel()
    # getlabel()
    # addwork()