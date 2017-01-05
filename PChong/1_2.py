# -*- coding: utf-8 -*-
"""
Created on Wed Jan  4 15:35:24 2017

@author: Z
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj=BeautifulSoup(html,'lxml')

#for sibling in bsObj.find('table',{'id':'giftList'}).children:
#    print(sibling)


#for sibling in bsObj.find('table',{'id':'giftList'}).tr.next_siblings:
#    print(sibling)

#for sibling in bsObj.find('img',{'src':'../img/gifts/img2.jpg'}).parent.previous_siblings:
#    print(sibling)

images=bsObj.findAll('img',{'src':re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:    
    print(image)
#children 当前标签里的标签
#next_siblings 当前标签的下一个标签

#gift2 > td:nth-child(4) > img
#<img src="../img/gifts/img2.jpg">