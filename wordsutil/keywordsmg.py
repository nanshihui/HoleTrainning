# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re,json

def getkeywordsitem(jsonobj,label):
    array = set()
    for i in jsonobj.get(label,[]):

        a = ''
        if i.get('version','none') =='none':
            a+=i.get('type','unknow')
        else:
            a+=i.get('type','unknow')+'/'+i.get('version','')
        array.add(a)
    return array
def getkeywords(jsonobj,label):
    tmp=set()
    language=jsonobj.get(label, 'unknow')
    if type(language)==list:
        language=",".join(map(str, language))
    tmp.add(language)
    return tmp
def getheaders(jsonobj,label):
    item=set()
    keys=jsonobj.get(label,{})
    for i in keys:
        value=keys[i]
        # print i,value
        if i=='server':
            if '(' in value:
                value= re.split("[() ]",value)

                item|=set(value)
            else:
                item.add(value)
        elif i=='date':
            pass
        elif i=='keep-alive':
            pass
        elif i=='content-type':
            value = re.split("[; ]", value)

            item |= set(value)
        elif i=='etag':
            pass
        elif i=='last-modified':
            pass
        elif i=='set-cookie':

            pass
        elif i=='redirected':
            pass
        elif i=='location':
            pass
        elif i=='expires':
            pass
        elif i=='www-authenticate':
            pass
        elif i=='x-content-security-policy':
            pass
        else:
            item.add(keys[i])


    return item
def getkeywordslocation(jsonobj):
    item=set()
    keys=jsonobj.get('geoip',{})
    city=keys.get('city',{}).get('name','unknow')
    latitude=keys.get('location',{}).get('latitude','unknow')
    longitude=keys.get('location',{}).get('longitude','unknow')
    return city,latitude,longitude
def keywordstojson(kewords):
    result=None
    try:
        result=json.loads(kewords)
    except Exception,e:
        print e
        item=None
        item = delplacer(kewords)
        print item
        item=replace_quotation(item)
        print item
        item=replace_triplequotation(item)
        print item
        item=item.replace(" u'\\xdcr\\xfcmqi'", " u'unknow'")
        item = item.replace('"', '\'')

        item = item.replace(' u\'', ' \'')
        print item
        item=item.replace('\'','"')
        item=item.replace('\t','')
        item=item.replace('none,','"none",')
        print item
        return json.loads(item)
def getkeyword(msg):
    if msg is None:
        return ['']
    kewords = msg.lower()
    try:
        jsonobj = keywordstojson(kewords)
    except Exception,e:
        print e
        return [kewords]
    if type(jsonobj)==dict:

        lableary = set()
        lableary |= getkeywordsitem(jsonobj, 'frontend')
        # print lableary
        lableary |= getkeywordsitem(jsonobj, 'component')
        # print lableary
        lableary |= getkeywords(jsonobj, 'language')
        # print lableary
        lableary |= getheaders(jsonobj, 'headers')
        city,latitude,longitude=getkeywordslocation(jsonobj)
        lableary.add(city)
        # print lableary
        return lableary
    else:

        return msg
def delplacer(msg):
    regex="""u\"\w+\'\w+\""""
    reobj = re.compile(regex)
    match = reobj.search(msg)
    if match:
        result = match.group()
    else:
        result = ""
    item=result
    item=item.replace('\'','')
    item=item.replace('\"','\'')

    return msg.replace(result,item)
def replace_quotation(msg):
    regex="\"(.*?)\""
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            item = i.replace('\'', '')
            msg=msg.replace(model, item)
    else:
        result = ""
    return msg

def replace_triplequotation(msg):
    msg=replace_containlequotation(msg)
    regex=": (\'.*?\".*?\".*?\')}"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            if s
            item = i.replace('\"', '')
            msg=msg.replace(model, item)

    regex = ": (\'.*?\".*?\".*?\'),"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:
            model = i
            item = i.replace('\"', '')
            msg = msg.replace(model, item)
    return msg
def replace_containlequotation(msg):
    regex="(\'\".*?\"\')"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            item = i.replace('\"', '')
            msg=msg.replace(model, item)


    return msg