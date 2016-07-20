# !/usr/bin/env python
# -*- coding: utf-8 -*-
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
def identifylabel():
    from DButil import db
    sql='select count(*) from testdata '
    size=db.get(sql)['count(*)']
    i=57254
    while i<size:


        sql = 'select ip,port,keywords from testdata limit %d,1' % i
        result=db.get(sql)
        ip= result['ip']
        port=result['port']
        keywords=result['keywords']
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
            sql ="update  testdata set label = '%s' ,contentlength= '%s',headlabel= '%s',place= '%s',front= '%s',component= '%s',language= '%s' where ip = '%s' and port = %s" %(newwords,contentlength,headlabelmsg,cityset,frontendmsg,componentmsg,languagemsg,ip,port)
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
def getlabel():
    lableary = {}
    from DButil import db
    sql='select count(*) from testdata '
    size=db.get(sql)['count(*)']
    for i in xrange(size):
        sql = 'select ip,port,label from testdata limit %d,1' % i
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

    writefile(lableary)
def writefile(lableary):
    f = file('3.txt','w')
    keyset=lableary.keys()
    for i in keyset:
        f.write(i+'------------------'+str(lableary[i])+'\n')
    f.close()
if __name__ == "__main__":
    identifylabel()
    # getlabel()
    # addwork()