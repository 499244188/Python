# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:19:09 2017

@author: Z
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
#import random
#import datetime

#random.seed(datetime.datetime.now())
#def getLinks(articleUrl)
html=urlopen('http://baike.baidu.com/view/451254.htm')
bsObj=BeautifulSoup(html,'lxml')
for link in bsObj.findAll("a",href=re.compile("^(/view/)([0-9]+)\.(htm)$")):
    print(link)
    #if 'href' in link.attrs:
       # print(link.attrs['href'])
