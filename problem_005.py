# -*- coding: utf-8 -*-
"""
PYTHON CHALLENGE

PROBLEM: 5

URL: http://www.pythonchallenge.com/pc/def/peak.html

"""

import urllib, pickle

myurl="http://www.pythonchallenge.com/pc/def/banner.p"

handle= urllib.urlopen(myurl)

object = pickle.load(handle)

handle.close()

for item in object:
    print "".join(i[0] * i[1] for i in item)