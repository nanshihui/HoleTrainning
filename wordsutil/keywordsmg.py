# !/usr/bin/env python
# -*- coding: utf-8 -*-
import re,json
import sys;
reload(sys);

sys.setdefaultencoding('utf8');
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
    labelset=set()
    keys=jsonobj.get(label,{})
    length='0'
    for i in keys:
        value=keys[i]
        # print i,value
        if i=='server':
            item|=getServer(value)

        elif i=='date':
            pass
        elif i=='keep-alive':
            pass
        elif i=='content-type':
            pass
            # value = re.split("[; ]", value)
            #
            # item |= set(value)
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
        elif i=='x-webkit-csp':
            pass
        elif i=='content-location':
            pass
        elif i=='x-squid-error':
            pass
        elif i=='x-robots-tag':
            pass
        elif i == 'p3p':

            pass
        elif i=='x-request-id':
            pass
        elif i=='via':
            pass
        elif i=='cache-control':
            pass
        elif i=='pragma':
            pass
        elif i=='link':
            pass
        elif i=='x-ua-compatible':
            pass
        elif i=='x-runtime':
            pass
        elif i=='x-request-id':
            pass
        elif i=='content-length':
            length=value
        else:
            pass
            # k=keys[i].replace('\'','')
            # k = k.replace('\"', '')
            # item.add(k)

        labelset.add(i)
    return item,labelset,length
def getkeywordslocation(jsonobj):
    item=set()
    keys=jsonobj.get('geoip',{})
    city=keys.get('city',{}).get('name','unknow')
    city=city.replace('\'','')
    # city=city.encoding()
    city=decodewords(str(city))
    latitude=keys.get('location',{}).get('latitude','unknow')
    longitude=keys.get('location',{}).get('longitude','unknow')
    return city,latitude,longitude
def keywordstojson(kewords):
    item=None
    item=kewords
    result=None
    try:
        item=eval(kewords)
        return item
    except Exception,e:
        print e,'85'
        # item=None
        # item=replace_quotation(item)
        # print item
        # item=replace_triplequotation(item)
        # print item
        item= decodewords(item)
        item = placename(item)
        item = equotation_out(item)

        item = equotation_in(item)


        item=item.replace(" u'\xdcr\xfcmqi'", " u'unknow'")
        item = item.replace('"', '\'')

        item = item.replace(' u\'', ' \'')

        item=item.replace('\'','\"')
        item=item.replace('\t','')
        item=item.replace('none,','"none",')
        item = item.replace("\\xdcr\\xfcmqi", "rmqi")


        print item

        item=json.loads(item)
        return item
def holelabel(msg):
    pass
def getkeyword(msg):
    frontendset = set()
    componentset = set()
    languageset = set()
    lableary = set()
    headlabel = set()
    contentlength='0'
    cityset = ''
    kewords=None
    if msg is None:
        return lableary,frontendset,componentset,languageset,headlabel,cityset,contentlength
    kewords = msg.lower()
    try:
        jsonobj = keywordstojson(kewords)
    except Exception,e:
        print e,'112'
        return [kewords],frontendset,componentset,languageset,headlabel,cityset,contentlength
    if type(jsonobj)==dict:
        frontendset=set()
        componentset=set()
        languageset=set()
        lableary = set()
        headlabel=set()
        cityset=''
        frontendset |= getkeywordsitem(jsonobj, 'frontend')

        componentset |= getkeywordsitem(jsonobj, 'component')

        languageset |= getkeywords(jsonobj, 'language')

        lableary,headlabel,contentlength= getheaders(jsonobj, 'headers')
        cityset,latitude,longitude=getkeywordslocation(jsonobj)

        return lableary,frontendset,componentset,languageset,headlabel,cityset,contentlength
    else:

        return lableary,frontendset,componentset,languageset,headlabel,cityset,contentlength
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
    # regex="\"(.*?)\""
    # reobj = re.compile(regex)
    # match = reobj.findall(msg)
    # if match:
    #     for i in match:
    #         if ': \'' in i :
    #             pass
    #         else:
    #
    #             model = i
    #             item = i.replace('\'', '')
    #             msg=msg.replace(model, item)
    # else:
    #     result = ""
    # return msg

    msg = replace_containlequotation(msg)
    regex = ": (\".*?\'.*?\'.*?\")}"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            if i.count('\"') > 2 or i.count('\'') % 2 > 0:
                pass
            else:
                item = i.replace('\'', '')
                msg = msg.replace(model, item)

    regex = ": (\".*?\'.*?\'.*?\")"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            if i.count('\"') != 2 or i.count('\'') % 2 > 0:
                pass
            else:
                item = i.replace('\'', '')
                msg = msg.replace(model, item)
    return msg

def replace_triplequotation(msg):
    msg=replace_containlequotation(msg)
    regex=": (\'.*?\".*?\".*?\')}"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            if i.count('\'') > 2 or i.count('\"') %2>0:
                pass
            else:
                item = i.replace('\"', '')
                msg=msg.replace(model, item)

    regex = ": (\'.*?\".*?\".*?\'),"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:

            model = i
            if i.count('\'') != 2 or i.count('\"') %2>0:
                pass
            else:
                item = i.replace('\"', '')
                msg=msg.replace(model, item)
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
def equotation_out(msg):
    regex = ": \'(.*?(?!\').*?)\'"  # 识别单引号外围
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:
            model = i
            item = i.replace('\"', '')
            msg=msg.replace(model, item)
    return msg
def equotation_in(msg):
    regex = ": \"(.*?(?!\").*?)\""  # 识别双引号外围
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:
            model = i
            item = i.replace('\'', '')
            msg=msg.replace(model, item)
    msg = msg.replace("\"", "\'")
    return msg
def decodewords(msg):


    if msg is None or msg == '':
        return ' '

    import chardet
    chardit1 = chardet.detect(msg)
    return msg.decode(chardit1['encoding']).encode('utf-8')

# def placename(msg):
#     regex = ": u\'(.*?(?!\")\'.*?)\'}"  # 识别地名单引号
#     reobj = re.compile(regex)
#     match = reobj.findall(msg)
#     if match:
#         for i in match:
#             model = i
#             if ':' in model:
#                 pass
#             else:
#
#                 item = i.replace('\'', '')
#                 msg=msg.replace(model, item)
#     return msg
def placename(msg):
    regex = ": u\"(.*?(?!\")\'.*?)\"}"  # 识别地名单引号
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:
            model = i
            if ':' in model:
                pass
            else:

                item = i.replace('\'', '')
                msg=msg.replace(model, item)
    return msg
def getServer(msg):
    result=set()
    regex=" (\(.*?\))"
    reobj = re.compile(regex)
    match = reobj.findall(msg)
    if match:
        for i in match:
            model = i
            print i
            item = i[1:-1]
            if '; ' in i[1:-1]:
                ary=i[1:-1].split('; ')
                result |= set(ary)
            else:
                result.add(i[1:-1])
            msg=msg.replace(i,'')
            ary=msg.split(' ')
            result|=set(ary)
    else:
        if msg.count('/')>1:
            ary=msg.split(' ')
            result |= set(ary)


        else:
            result.add(msg)
    return result

if __name__ == "__main__":
    # kewords = """{'ip': ['60.10.135.62'], 'geoip': {'city': {'name': u'hebei'}, 'location': {'latitude': 39.8897, 'longitude': 115.275}, 'continent': {'code': u'as', 'name': u'asia'}, 'country': {'code': u'cn', 'name': u'china'}}, 'component': [{'version': none, 'type': 'tomcat'}], 'site': '60.10.135.62:8080', 'headers': {'content-length': '339', 'accept-ranges': 'bytes', 'server': 'apache-coyote/1.1', 'last-modified': 'mon, 28 sep 2015 04:29:01 gmt', 'etag': 'w/"339-1443414541000"', 'date': 'sat, 09 jul 2016 10:29:16 gmt', 'content-type': 'text/html'}}"""
    # print type(eval(equotation_out(kewords)))
    # keywords="""{'language': ['aspnet'], 'ip': ['61.185.131.213'], 'component': [{'version': none, 'type': 'asp.net'}], 'site': '61.185.131.213:84', 'headers': {'content-length': '3420', 'x-aspnet-version': '4.0.30319', 'x-powered-by': 'asp.net', 'server': 'microsoft-iis/7.5', 'cache-control': 'private', 'date': 'sat, 09 jul 2016 14:03:24 gmt', 'content-type': 'text/html; charset=utf-8'}, 'geoip': {'city': {'name': u'xi'an'}, 'location': {'latitude': 34.2583, 'longitude': 108.9286}, 'continent': {'code': u'as', 'name': u'asia'}, 'country': {'code': u'cn', 'name': u'china'}}}"""
    # print placename(keywords)
    msg="""{'language': ['aspnet'], 'ip': ['61.185.131.213'], 'component': [{'version': none, 'type': 'asp.net'}], 'site': '61.185.131.213:84', 'headers': {'content-length': '3420', 'x-aspnet-version': '4.0.30319', 'x-powered-by': 'asp.net', 'server': 'microsoft-iis/7.5', 'cache-control': 'private', 'date': 'sat, 09 jul 2016 14:03:24 gmt', 'content-type': 'text/html; charset=utf-8'}, 'geoip': {'city': {'name': u"xi'an"}, 'location': {'latitude': 34.2583, 'longitude': 108.9286}, 'continent': {'code': u'as', 'name': u'asia'}, 'country': {'code': u'cn', 'name': u'china'}}}"""
    print placename1(msg)

