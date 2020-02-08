#!/usr/bin/python
#coding:UTF-8
import base64
str = raw_input()
#print(str)
f = open(str,'rb')
ls_f=base64.b64encode(f.read())
f.close()
print(ls_f)
