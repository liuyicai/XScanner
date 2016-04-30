#!python
#-*- coding:utf8 -*-
# author			: glacier@insight-labs.org (BaCde)
# version			: v1.0
import sys
from tasks import getHTTPinfo

i = 0
for url in open("list.txt"):
	i = i+1
	#if i >= 0 and i <= 18000000:
	url = url.replace("\n","")
	url = url.replace("\r","")
	url = url.replace('"',"")
	url = url.strip()
	getHTTPinfo.delay(url)
