#!python3
#encoding=utf-8
from __future__ import print_function, division
import chardet
import re
import sys

DEBUG = sys.flags.debug or False
def debug(*args):
    '''funciona como print, mas só é executada se sys.flags.debug == 1'''
    if not DEBUG:
        return ;
    print(*args)


with open(sys.argv[1], 'rb') as file:
    data = file.read()
    chdet = chardet.detect(data)
    debug("chdet:", chdet)
    encode = chdet['encoding']
    if encode is None:
        sys.exit(0)
    if re.match(r'windows-12\d\d', encode):
        encode = 'windows-1252'
    debug("encode:", encode)
    newEncode = 'utf-8' if encode != 'utf-8' else 'iso-8859-1'
    debug("newEncode:", newEncode)
    print(encode, "to", newEncode)
    newData = data.decode(encode).encode(newEncode)
    debug("newData:", newData)

with open(sys.argv[1], 'wb') as file:
    file.write(newData)
