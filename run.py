#!python
#-*- coding:utf8 -*-
# author			: glacier@insight-labs.org (BaCde)
# version			: v1.0
import sys
from tasks import getHTTPinfo

url = sys.argv[1]
getHTTPinfo.delay(url)