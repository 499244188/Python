# -*- coding: utf-8 -*-
"""
Created on Mon Jan  9 17:19:09 2017

@author: Z
"""
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen('http://baike.baidu.com/view/451254.htm')
bsObj=BeautifulSoup(html,'lxml')
for link in bsObj.findAll("a"):
    if 'href' in link.attrs:
        print(link.attrs['href'])
