# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 17:18:08 2017

@author: Z
"""

import json
from urllib.request import  urlopen

def getCountry(ipAdd):
    response= urlopen('http://freegeoip.net/json/'+ipAdd).read().decode('utf-8')
    #print(response)
    responeJson=json.loads(response)
    #print(responeJson)
    return responeJson.get("city")

print(getCountry("222.22.45.18"))

