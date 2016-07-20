#!/usr/bin/python
#coding:utf-8
from Threadutil.ThreadTool import ThreadTool
import datetime
import time

from Threadutil.TaskTool import TaskTool
worktaskinstance=None
from wordsutil import log

def getObject():
    global worktaskinstance
    if worktaskinstance is None:
        worktaskinstance=WordsTask(1)

    return  worktaskinstance
from wordsutil import keywordsmg as KeywordsUtil
def escapeword(word):
    import MySQLdb
    if word is None:
        return ''
    else:
        content=''
        content = str(MySQLdb.escape_string(word))
        return content
from DButil import db
class WordsTask(TaskTool):
    def __init__(self,isThread=1):
        TaskTool.__init__(self,isThread)
        self.set_deal_num(5)

    def task(self,req,threadname):
        print req
        print threadname+'执行被动扫描'+str(datetime.datetime.now())
        i=req
        sql = 'select ip,port,keywords from testdata limit %d,1' % i
        result = db.get(sql)
        ip = result['ip']
        port = result['port']
        keywords = result['keywords']
        newwords = KeywordsUtil.getkeyword(str(keywords))
        print i, ip, port, keywords
        newwords = ",".join(map(str, newwords))

        newwords = newwords.replace('%s', '')
        newwords = escapeword(newwords)
        print newwords
        sql = "update  testdata set label = '%s' where ip = '%s' and port = %s" % (newwords, ip, port)
        log.INFO(str(i) + '----' + str(ip) + '----' + str(port) + '----' + str(keywords))
        log.INFO(sql)
        result = db.execute(sql)
        if 0 == result:
            print 'success'
        print threadname+'执行被动扫描结束'+str(datetime.datetime.now())
        return ''