# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 14:39:10 2017

@author: Z
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
html = urlopen("http://www.baidu.com")
bsObj=BeautifulSoup(html, "lxml")
#nameList=bsObj.findAll('span',{'class':'red'})
#
#find返回单个
#findAll返回多个
#nameList=bsObj.find({'h1','h2'})
#nameList=bsObj.findAll(id='text')
nameList=bsObj.findAll(class_='mnav')
#nameList=bsObj.Comment
#print(nameList[0].get_text())
for name in nameList:
    print(name.get_text())
