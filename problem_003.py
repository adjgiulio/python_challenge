# -*- coding: utf-8 -*-
"""
PYTHON CHALLENGE

PROBLEM: 3

URL: http://www.pythonchallenge.com/pc/def/equality.html

"""

import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
page = urllib.urlopen(url).read()

htmlstr = page.decode()
print(htmlstr)

txt = htmlstr[495:-4]

pattern = r'[^A-Z][A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]'

print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", txt))