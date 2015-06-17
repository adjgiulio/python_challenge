# -*- coding: utf-8 -*-
"""
PYTHON CHALLENGE

PROBLEM: 1

URL: http://www.pythonchallenge.com/pc/def/map.html

"""


from string import maketrans

have = "abcdefghijklmnopqrstuvwxyz"
want = "cdefghijklmnopqrstuvwxyzab"

trantab = maketrans(have, want)

mystring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.";
print mystring.translate(trantab);

print "map".translate(trantab)

