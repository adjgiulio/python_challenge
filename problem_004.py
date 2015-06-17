# -*- coding: utf-8 -*-
"""
PYTHON CHALLENGE

PROBLEM: 4

URL: http://www.pythonchallenge.com/pc/def/linkedlist.php

"""

import urllib
import re

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=8022"
page = urllib.urlopen(url).read()

htmlstr = page.decode()


while htmlstr[:3] == 'and':
    url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"%htmlstr[-5:]
    page = urllib.urlopen(url).read()
    htmlstr = page.decode()