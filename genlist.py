
#coding:utf-8

import sys
import os

my_path = './list'

files = os.listdir(my_path)

outstr = '{"musics":['
for f in files:
    print(f)
    name = f.split('.')
    name = name[0]
    outstr += '{"name":"' + name + '","file":"' + f + '"},'
    
outstr += ']}'

outstr = outstr.replace(",]","]")

with open('list.json','w',encoding='utf8') as f:
    f.write(outstr)
    

""" for line in lines:
    ll = line.split()
    txt = r'{"order":"' + ll[0] + r'","name":"' + ll[1] + r'"},' + '\r\n'
    with open('hrm14new.txt','a') as f:
        f.write(txt)
 """