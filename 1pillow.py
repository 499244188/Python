# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:32:38 2017

@author: Z
"""

from PIL import Image

#打开一个图像文件
im = Image.open(r'C:\users\z\Desktop\ab.bmp')

w,h = im.size
print('Original image size:%sx%s' %(w,h))

im.thumbnail((w**4, h*2))
print('Original image size:%sx%s' %(w*2,h*2))

im.save('e:\\aa.jpeg')













