# -*- coding: utf-8 -*-
"""
PYTHON CHALLENGE

PROBLEM: 2

URL: http://www.pythonchallenge.com/pc/def/ocr.html

"""

import urllib
from lxml import html

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
page = urllib.urlopen(url).read()

htmlstr = page.decode()
print(htmlstr)

dict_str = {}

for k in htmlstr[845:]:
    if k in dict_str:
        dict_str[k] += 1
    else:
        dict_str[k] = 1
        

remove = ''.join([k.encode('ascii','ignore') for k in dict_str if dict_str[k]>1])     

txt = htmlstr[845:].strip()

str(txt).translate(None, remove)