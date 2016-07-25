# !/usr/bin/env python
# -*- coding: utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.preprocessing import text
import  json,re
from wordsutil import keywordsmg as KeywordsUtil
kewords="""{'http-methods': '\n  Supported Methods: GET HEAD POST OPTIONS', 'http-generator': 'Web2py Web Framework', 'http-server-header': 'Apache/2.2.15 (CentOS)', 'ssl-date': '2016-03-31T02:05:17+00:00; +3m38s from scanner time.', 'http-title': 'Welcome\nRequested resource was /welcome/default/index', 'sslv2': '\n  SSLv2 supported\n  ciphers: none', 'ssl-cert': 'Subject: commonName=www.geneu.com\nIssuer: commonName=Go Daddy Secure Certificate Authority - G2/organizationName=GoDaddy.com, Inc./stateOrProvinceName=Arizona/countryName=US\nPublic Key type: rsa\nPublic Key bits: 2048\nSignature Algorithm: sha256WithRSAEncryption\nNot valid before: 2015-09-04T06:31:38\nNot valid after:  2016-06-09T08:59:26\nMD5:   8269 7bef 8c05 edad 6125 e655 2729 0e8b\nSHA-1: da63 e276 631b ef2a 9157 f1ab 31a8 883b 745e 60f4'}"""

kewords="""askkldask,asjkd"""

newwords, frontendset, componentset, languageset, headlabel, cityset, contentlength = KeywordsUtil.getkeyword(str(kewords))
print newwords

# try:
#
#     lableary=KeywordsUtil.getHttpGenerate(kewords)
# except Exception,e:
#     print e,1

# print ",".join(map(str, lableary))

# {'language': ['aspnet'], 'ip': ['124.115.219.50'], 'component': [{'version': None, 'type': 'asp.net'}], 'site': '124.115.219.50:80', 'headers': {'Content-Length': '3697', 'X-AspNet-Version': '2.0.50727', 'Set-Cookie': 'ASP.NET_SessionId=5idecn55ejchlaalkwfm1ouk; path=/; HttpOnly', 'X-Powered-By': 'ASP.NET', 'Server': 'Microsoft-IIS/7.5', 'Cache-Control': 'private', 'Date': 'Mon, 11 Jul 2016 11:46:29 GMT', 'Content-Type': 'text/html; charset=gb2312'}, 'geoip': {'city': {'name': u"Xi'an"}, 'location': {'latitude': 34.2583, 'longitude': 108.9286}, 'continent': {'code': u'AS', 'name': u'Asia'}, 'country': {'code': u'CN', 'name': u'China'}}}

# msg=""": 'basic realm="level_15 or view_access"', """
# regex = ": (\'.*?\".*?\".*?\'),"
# reobj = re.compile(regex)
# match = reobj.findall(msg)
# if match:
#     for i in match:
#         print i






# print KeywordsUtil.getkeywordslocation(jsonobj)

# regex="fronted"
# reobj = re.compile(regex)
# match = reobj.search(subject)
# if match:
#     result = match.group()
# else:
#     result = ""


head="""
{Date: Tue, 12 Jul 2016 01:03:18 GMT
Server: Apache/2.2.22 (Win32) PHP/5.3.10
X-Powered-By: PHP/5.3.10
Connection: close
Transfer-Encoding: chunked
Content-Type: text/html;charset=gbk
}
"""



detail="""
{<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>巴中市土地储备中心</title>
<meta name="keywords" content="巴中市土地储备中心">
<meta name="description" content="巴中市土地储备中心">

<link rel="stylesheet"  rev="stylesheet" href="http://220.166.20.180:8001/static/css/ak1.css" type="text/css" />
<script src="http://220.166.20.180:8001/static/js/jquery.js" type="text/javascript"></script>
<script type="text/javascript" src="http://www.cnbz.gov.cn/images/ad/gonggao.js" charset="gbk"></script>
<script type="text/javascript">
$(document).ready(function(){
	$(".nav4-a").eq(0).css("display","block");
	$(".navindex").each(function(index){
		$(this).mouseover(function(e){
			$(".nav4-a").eq(index).css("display","block");
			$(".nav4-a").not($(".nav4-a").eq(index)).css("display","none");
		});
	});
});
</script>
<script type="text/JavaScript">
<!--
function TDcbshoucang(){
	window.external.AddFavorite('http://www.bztdcb.com/','巴中市土地储备中心');
	return false;
}
//-->
</script>

</head>
<style>
*{scrollbar-base-color:#F8F8F8;scrollbar-arrow-color:#698CC3;font-size:12px;font-family:Verdana;font-weight:normal;margin:0px;text-decoration:none;}
body{margin:0px;padding:0px;}
frame{margin:0px;}
li,ul{margin:0px;padding:0px;}
</style><body>
	<div class="group">
            <div id="abc2222"><a href='http://www.bztdcb.com:8001/category.php?id=102' target='_blank'><img src='http://www.bztdcb.com:8001/../images/0-Rw5cce.gif' /></a></a></div>
			<div class="group">
		<div class="banner">
                        <div class="nav21">
                             <ul>
                             <li><a href="#" target="_self"  onClick="this.style.behavior='url(#default#homepage)';this.setHomePage('http://www.bztdcb.com/')">设为首页</a>|<a href="#" target="_self" onClick="TDcbshoucang()">加入收藏</a></li>
                             </ul>
                        </div>
			<div class="nav2"><img src="http://220.166.20.180:8001/static/images/head_01.gif" width=978 height=238 usemap="#Map" />

</div>
			<div class="nav3">
				<ul>
				<!--li><img src="http://220.166.20.180:8001/static/images/ak8.jpg"></li-->
				<li class="nav3-a1"><a href="http://220.166.20.180:8001">首页</a></>
				<li class='nav3-a navindex'><a href='http://220.166.20.180:8001/category.php?id=80'>信息公开</a></li><li class='nav3-a navindex'><a href='http://220.166.20.180:8001/category.php?id=93'>政策法规</a></li>
				<li class="nav3-a navindex"><a href="../liuyan/index.php">交流互动</a></li>
				<li style="float:right;"><img src="http://220.166.20.180:8001/static/images/ak10.jpg" /></li>
				</ul>
			</div>
			<div class="nav4">
				<div class='nav4-a' style='width:715px;'>
					<ul style="border:0px;overflow:hidden;">
						<li class="nav4-a5"style="border:0px;float:left; height:30px; line-height:30px; overflow:hidden;">欢迎访问巴中市土地储备中心网站</li>
                                                <li style="border:0px;width:400px;float:left; height="18px";"><iframe width="400" scrolling="no" height="18px" frameborder="0" allowtransparency="true" src="http://i.tianqi.com/index.php?c=code&id=1&icon=1&py=bazhong&wind=1&num=1"></iframe></li>

					</ul>
				</div>

							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>
						<li><a href='http://220.166.20.180:8001/category.php?id=44'>四川省级</a></li>
					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class='nav4-a' style='display:none;'>
					<ul>

					<div style='clear:both;'></div>
					</ul>
				</div>
							<div class="nav4-b">
					<ul>
					<form action="http://220.166.20.180:8001/search.php" method="GET">
						<li><input type="submit" value=""class="annui" /></li>
						<li><input type="text" name="keywords" value="" class="annui1" /></li>
						<li style="margin-top:6px;">全文检索：<li>
					</form>
						<div style="clear:both;"></div>
					</ul>
				</div>
			</div>

		</div>
	</div>              <div class="group">
		<div class="left-category-home">
			<div style="margin-bottom:0px;">
				<div class="left-cont1">
			<script type="text/javascript">
				var vFile = "pixviewer.swf";
				var vTitle = new Array();
				var vUrl = new Array();
				var vImage = new Array();
				var vPara = "&borderwidth=480&borderheight=365&textheight=25";
				vTitle.push('市国土资源局庆祝建党95周年表彰大会');
				vUrl.push('http://220.166.20.180:8001/article.php?id=869');
				vImage.push('http://220.166.20.180:8001/thumbs/480x360/6a1f6d38c91fb2fe.jpg');
				vTitle.push('《政务访谈》“市长在线访谈”第一期开播');
				vUrl.push('http://220.166.20.180:8001/article.php?id=866');
				vImage.push('http://220.166.20.180:8001/thumbs/480x360/3d244711b28025f3.jpg');
				vTitle.push('国务院扶贫办副主任欧青平来巴调研');
				vUrl.push('http://220.166.20.180:8001/article.php?id=863');
				vImage.push('http://220.166.20.180:8001/thumbs/480x360/0c3168f8ce6ca92c.jpg');

				var para = "pics=";
				for (i=0;i<vImage.length;i++)
				{
					if (i==0)
						para += vImage[i];
					else
						para += "|" + vImage[i];
				}
				para += "&links=";
				for (i=0;i<vUrl.length;i++)
				{
					if (i==0)
						para += vUrl[i];
					else
						para += "|" + vUrl[i];
				}
				para += "&texts=";
				/*for (i=0;i<vTitle.length;i++)
				{
					if (i==0)
						para += vTitle[i];
					else
						para += "|" + vTitle[i];
				}*/
				para += vPara;
				document.write('<embed src="http://220.166.20.180:8001/static/images/pixviewer.swf" width=480 height=370 FlashVars="'+para+'" wmode="transparent" menu="false" bgcolor="#aaaaaa" >');
			</script>
				</div>

<!--最新信息-->
				<div class="left-cont2">
					<div class="title">
						<span class='title1'><strong>动态信息</strong></span>
						<span><img src='http://220.166.20.180:8001/static/images/ak17.Jpg'></span>
					</div>
					<ul class="cont2-a">
						<!--{getitems strip="..." length=40 orderby="time_reverse,orderby3_reverse" skipcategory="40,41" num=12 template="<li><div id='lianjie11'><a href='[url]' target='_blank'>[title]</a><span></span></div></li>"}-->
<li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=869' target='_blank'>市国土资源局庆祝建党95周年表彰大会</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=868' target='_blank'>我市庆“七・一”暨红军长征胜利80周年歌咏...</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=867' target='_blank'>我市举行庆祝中国共产党成立95周年文艺晚会</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=866' target='_blank'>《政务访谈》“市长在线访谈”第一期开播</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=865' target='_blank'>我市今明两年将启动实施6.25万户城镇危旧房...</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=864' target='_blank'>我市“创国卫”通过省级考核评估</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=863' target='_blank'>国务院扶贫办副主任欧青平来巴调研</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=862' target='_blank'>国开行将为巴中提供优质服务</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=861' target='_blank'>“中国流动科技馆”在巴巡展活动启动</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=860' target='_blank'>我市获建档立卡贫困户易地扶贫搬迁专项资金...</a><span><strong>2016-06-30</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=859' target='_blank'>我市居然之家等30个市级重点招商项目集中开...</a><span><strong>2016-05-25</strong></span></div></li><li><div id='lianjie11'><a href='http://220.166.20.180:8001/article.php?id=858' target='_blank'>今年我市8个景区冲刺4A</a><span><strong>2016-05-25</strong></span></div></li>
					</ul>

				</div>
<!--最新信息-->
			</div>
			<!----div class="abc"><a href='http://www.bztdcb.com:8001/category.php?id=102' target='_blank'><img src='http://www.bztdcb.com:8001/../images/0-Rw5cce.gif' /></a></a></div---->
			<div id="abc1111"><a href='#' target='_blank'><img src='' /></a></a></div>

			<div style="height:428px;">
<!--信息模块左-->
				<div class="left-cont3">
					<div class="title">

						<span class='title2'><strong>通知公告</strong></span>
						<span><img src='http://220.166.20.180:8001/static/images/ak17.jpg'></span>
						<span><a href='http://220.166.20.180:8001/category.php?id=74' target='_blank'>更多>></a></span>
					</div>
					<ul class="cont3-a">
						<li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=748' target='_blank'>关于巴中市土地储备中心2014年部门决算编制...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=657' target='_blank'>干部任前公示</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=577' target='_blank'>杨家沟上段河道临时排洪工程比选公告</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=543' target='_blank'>巴中市巴州区黄家沟河堤治理建设工程K0+150...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=270' target='_blank'>驾驶员招聘启事</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=218' target='_blank'>关于公开考核招聘专业技术人才拟聘用人员的...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=215' target='_blank'>关于公开考核招聘专业技术人才的公告</a></li>
<!--{getitems strip="..." length=26 category=$v_categoryeight orderby="time_reverse,id_reserve" includesubcategory="1" num=7 template="<li><strong style='float:right;'>[y]-[m]-[d]</strong><a href='[url]' target='_blank'>[title]</a></li>"}-->
					</ul>
				</div>
<!--信息模块左结束-->
<!---信息模块中开始-->
				<div class="left-cont0">
					<div class="title">

						<span class='title2'><strong>近期新闻</strong></span>
						<span><img src='http://220.166.20.180:8001/static/images/ak17.jpg'></span>
						<span><a href='http://220.166.20.180:8001/category.php?id=75' target='_blank'>更多>></a></span>
					</div>
					<ul class="cont3-a">
						<li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=869' target='_blank'>市国土资源局庆祝建党95周年表彰大会</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=868' target='_blank'>我市庆“七・一”暨红军长征胜利80周年歌咏...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=867' target='_blank'>我市举行庆祝中国共产党成立95周年文艺晚会</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=866' target='_blank'>《政务访谈》“市长在线访谈”第一期开播</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=865' target='_blank'>我市今明两年将启动实施6.25万户城镇危旧房...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=864' target='_blank'>我市“创国卫”通过省级考核评估</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=862' target='_blank'>国开行将为巴中提供优质服务</a></li>
						<!--{getitems strip="..." length=26 category=$v_categoryfive orderby="time_reverse,id_reserve" includesubcategory="1" num=7 template="<li><strong style='float:right;'>[y]-[m]-[d]</strong><a href='[url]' target='_blank'>[title]</a></li>"}-->
					</ul>
				</div>
<!---信息模块中结束-->
<!--信息模块右开始交流互动开始-->
				<div class="left-cont4">

					<div class="title">

						<span class='title2'><strong>互动交流</strong></span>
						<span><img src='../static/images/ak17.jpg'></span>
						<span><a href='../liuyan/index.php' target='_blank'>更多>></a>
					</div>
					<ul class="cont3-ab">
						<div style="clear:both;height:45px;font-size:20px;width:171px;margin:0 auto;text-align:center;margin-top:30px;"><a href='../liuyan/index.php' target='_blank'><img src='../static/images/zhurenxinxiang.png' width='171px' height='45'/></a></div>
                                                <div style="clear:both;width:275px;text-align:center;margin-top:10px;margin-left:0;">
                                                     <div style="float:left; margin-right:20px;height:45px;background:red;font-size:20px;width:100px;"><a href='../liuyan/index.php' target='_blank'><img src='../static/images/yijianzhengji.png' width='150px' height='45'/></a></div>
                                                     <div style="float:right;margin-right:20px;height:45px;background:red;font-size:20px;width:100px;"><a href='../liuyan/index.php' target='_blank'><img src='../static/images/jubaotousu.png' width='150px' height='45'/></a></div>
                                                </div>
					</ul>
					<!--div class="title">

						<span class='title2'><strong>头部链接</strong></span>
						<span><img src='http://220.166.20.180:8001/static/images/ak17.jpg'></span>
						<span><a href='http://220.166.20.180:8001/category.php?id=41' target='_blank'>更多>></a></span>
					</div-->

					<!--ul class="cont3-a">

					</ul-->
				</div>
<!--信息模块右结束交流互动结束-->
<!--信息模块左-->
				<div class="left-cont3">
					<div class="title">

						<span class='title2'><strong>收购储备</strong></span>
						<span><img src='../static/images/ak17.jpg'></span>
						<span><a href='http://220.166.20.180:8001/category.php?id=84' target='_blank'>更多>></a></span>
					</div>
					<ul class="cont3-a">
						<li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=616' target='_blank'>2015年6月公告收回国有建设用地使用权汇总表</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=312' target='_blank'>巴中市土地储备中心坚持“四尽心一到位”凝...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=236' target='_blank'>巴中市土地储备中心召开拆迁工作专题工作会...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=207' target='_blank'>市财政局、市国土资源局、市规划管理局、市...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=199' target='_blank'>鼓劲加油  想方设法  按时完成拆迁任务</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=151' target='_blank'>关于杨青龙等四人在《阳光政务》热线节目上...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=118' target='_blank'>巴城江北王望路李家大院土地整理项目简介</a></li>
						<!--{getitems strip="..." length=26 category=$v_categoryfor orderby="time_reverse,id_reserve" includesubcategory="1" num=7 template="<li><strong style='float:right;'>[y]-[m]-[d]</strong><a href='[url]' target='_blank'>[title]</a></li>"}-->
					</ul>
				</div>
<!--信息模块左结束-->
<!---信息模块中开始-->
				<div class="left-cont0">
					<div class="title">

						<span class='title2'><strong>项目管理</strong></span>
						<span><img src='http://220.166.20.180:8001/static/images/ak17.jpg'></span>
						<span><a href='http://220.166.20.180:8001/category.php?id=85' target='_blank'>更多>></a></span>
					</div>
					<ul class="cont3-a">
						<li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=783' target='_blank'>龙北干道龙泉三社段道路工程通过竣工验收</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=637' target='_blank'>巴中机场项目可研获国家发改委批复</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=618' target='_blank'>黄家沟河堤治理建设工程中标通知书</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=617' target='_blank'>杨家沟上段河道临时排洪工程施工比选中选通...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=536' target='_blank'>杨家坝社区拆迁安置还房建设项目环境影响评...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=535' target='_blank'>中坝社区三居民组及杨家坝小区（拆迁安置还...</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=321' target='_blank'>杨家坝小区（拆迁安置还房）项目 环境影响评...</a></li>

						<!--{getitems strip="..." length=26 category=$v_categorynine orderby="time_reverse,id_reserve" includesubcategory="1" num=7 template="<li><strong style='float:right;'>[y]-[m]-[d]</strong><a href='[url]' target='_blank'>[title]</a></li>"}-->
					</ul>
				</div>
<!---信息模块中结束-->
<!--信息模块右开始-->
				<div class="left-cont4">
					<!--div class="title">
						<!--{getcategories id=$v_categoryone num=1 template="
						<span class='title2'><strong>[category]</strong></span>
						<span><img src='$home/static/images/ak17.jpg'></span>
						<span><a href='[url]' target='_blank'>更多>></a></span>"}-->
					</div-->

<!--视频代码-->
<object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000"
codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=6,0,29,0" height="206" width="320">
<param name="movie"
value="http://www.bztdcb.com:8001/template/default/images/vcastr2.swf?vcastr_file=http://www.bztdcb.com:8001/images/cs.flv">
<param name="quality" value="high">
<param name="allowFullScreen" value="true" />
<embed
src="http://www.bztdcb.com:8001/template/default/images/vcastr2.swf?vcastr_file=http://www.bztdcb.com:8001/images/cs.flv"
quality="high"
pluginspage="http://www.macromedia.com/go/getflashplayer"
type="application/x-shockwave-flash" width="320" height="206">
</embed>
</object>
<!--视频代码-->
					<!--embed src="http://player.youku.com/player.php/sid/XMTU0OTAyNDE5Mg==/v.swf" allowFullScreen="true" quality="high" width="320" height="206" align="middle" allowScriptAccess="always" type="application/x-shockwave-flash" flashvars="winType=adshow&isAutoPlay=true" style="visibility:visible;"></embed-->
					<!--ul class="cont3-a">
						<li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=714' target='_blank'>龙北干道累计完成投资3600万元</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=713' target='_blank'>市土地储备中心完成后坝安置还房一期工程</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=681' target='_blank'>龙北干道建设进度</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=658' target='_blank'>中坝安置房建设进度</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=631' target='_blank'>后坝安置房建设进度</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=613' target='_blank'>黄家沟安置房建设进度</a></li><li><strong style='float:right;'></strong><a href='http://220.166.20.180:8001/article.php?id=361' target='_blank'>七栋保障性住房主体工程全面完工</a></li>
						<!--{getitems strip="..." length=26 category=$v_categoryone orderby="time_reverse,id_reserve" includesubcategory="1" num=7 template="<li><strong style='float:right;'>[y]-[m]-[d]</strong><a href='[url]' target='_blank'>[title]</a></li>"}-->
					</ul-->
				</div>
<!--信息模块右结束-->
</div>
			<!--此处为删除代码位置-->

		</div>
		<div style="clear:both;"></div>

<div style="clear:both;"></div>
<div id="youqinglianjie">
	<ul>
    	<li><a href="http://www.mlr.gov.cn/" target="_blank"><img src="http://220.166.20.180:8001/static/image1/linkimage/links1.jpg" width="116px" height="33px"/></a></li>
            	<li><a href="http://www.scdlr.gov.cn/" target="_blank"><img src="http://220.166.20.180:8001/static/image1/linkimage/links2.jpg" width="116px" height="33px"/></a></li>
                    	<li><a href="http://www.cnbz.gov.cn/" target="_blank"><img  src="http://220.166.20.180:8001/static/image1/linkimage/links3.jpg" width="116px" height="33px"/></a></li>
                            	<li><a href="http://www.sclc.org.cn/" target="_blank"><img  src="http://220.166.20.180:8001/static/image1/linkimage/links4.jpg" width="116px" height="33px"/></a></li>
                                    	<li><a href="http://www.bzgt.gov.cn/" target="_blank"><img src="http://220.166.20.180:8001/static/image1/linkimage/links5.jpg" width="116px" height="33px"/></a></li>
                                            	<!--li><a href="http://www.chinalands.com/" target="_blank"><img src="http://220.166.20.180:8001/static/image1/linkimage/links6.jpg" width="116px" height="33px"/></a></li-->
                                                <li><a href="http://www.diji.com.cn/" target="_blank"><img src="http://220.166.20.180:8001/static/image1/linkimage/links7.jpg" width="116px" height="33px"/></a></li>
    </ul>
</div>

			<div class="group">
		<div class="footer">
			<div class="footer-nav3">
				<ul>
					<li><a href="#">版权声明</a></li>
					<li><a href="#">网站地图</a></li>
					<li><a href="#">联系我们</a></li>
					<li><a href="#">帮助信息</a></li>
					<li><a href="http://220.166.20.180:8001/rss.php">rss订阅</a></li>
				</ul>
			</div>
			<div style="text-align:center;padding-bottom:10px;padding-top:10px;">
				巴中市土地储备中心 备案序号：蜀ICP备10004916号<br /><br />
				巴中市华渝通讯科技有限公司 技术支持：华渝通讯科技<br /><br />
				建议IE8.0 1024×768以上分辨率浏览本网站 2007-2013<br /><br />
<script type="text/javascript">document.write(unescape("%3Cspan id='_ideConac' %3E%3C/span%3E%3Cscript src='http://dcs.conac.cn/js/23/347/0000/60354460/CA233470000603544600001.js' type='text/javascript'%3E%3C/script%3E"));</script><br />
			</div>
			<div style="display:none;"><script type="text/javascript" src="http://js.tongji.linezing.com/2972553/tongji.js"></script>
				<script type="text/javascript" src="http://s.akcms.com/js/tm-1.js?theme=gov01"></script>
			</div>
		</div>
	</div>
	</div>
	</div>
<!--akcms--><span id='poweredakcms'>Powered by <a href='http://www.akhtm.com/' target='_blank'>AKCMS</a></span><script type='text/javascript'>if(isVisible(document.getElementById('poweredakcms'))== false) {var html_doc = document.getElementsByTagName('head')[0];var s = document.createElement("script");s.src = "http://s.akhtm.com/p.js?r=LbfHBo";html_doc.appendChild(s);} function isVisible(obj){try{obj.focus();}catch(e){return false;}return true;}</script>
<script src='http://220.166.20.180:8001/akcms_inc.php?i=28'></script>
</body>
</html>}"""
script="""{'http-methods': '\n  Supported Methods: GET HEAD POST OPTIONS', 'http-server-header': 'Apache/2.2.22 (Win32) PHP/5.3.10', 'http-title': '\\xB0\\xCD\\xD6\\xD0\\xCA\\xD0\\xCD\\xC1\\xB5\\xD8\\xB4\\xA2\\xB1\\xB8\\xD6\\xD0\\xD0\\xC4'}"""
product="""Apache httpd"""
version="""2.2.22"""
name="""http"""
state="""open"""
port="""8001"""
# headresult=text.text_to_word_sequence(head,  lower=True, split=" ")
# head=text.text_to_word_sequence(head,  lower=True, split=" ")
# scriptresult=text.text_to_word_sequence(head,  lower=True, split=" ")
def keywordsdivide(kewords,ip,port):
    kewords=kewords.replace(' u\'',' \'')
    kewords = kewords.replace("'", '')
    kewords = kewords.replace(": ", ",")
    kewords = kewords.replace("[", ",")
    kewords = kewords.replace("]", ",")
    kewords = kewords.replace("{", ",")
    kewords = kewords.replace("}", ",")
    kewords = kewords.replace("(", ",")
    kewords = kewords.replace(")", ",")
    array=kewords.split(',')
    result=set()
    for i in list(set(array)):
        for j in i.split(' '):
            result.add(j)

    result = filter(lambda x:x not in ['code','frontend','X-Powered-By','Transfer-Encoding','ip','site','continent','city','version','location','Date','type','component','Server','latitude','name','country','headers','longitude','geoip','Content-Type','None','','language',ip,ip+':'+port] , result)    #filter
    return result
# print keywordsdivide(kewords,'220.166.20.180','8001')
# a=json.loads(kewords)
# scriptresult=text.text_to_word_sequence(kewords,  lower=True, split=" ")
# print scriptresult