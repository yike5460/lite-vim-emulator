#!/usr/bin/env python
# -*- coding: utf-8 -*-

from test_utils import cabs, move
import math

def trim(s):
    if (len(s) == 0):
        return s
    cur = 0
    last_cur = len(s)-1
    
    while (s[cur] == ' ') & (cur < last_cur):
        cur+=1
    while (s[last_cur] == ' ') & (cur < last_cur):
        last_cur-=1
    if (cur == last_cur):
        return ''
    return s[cur:last_cur+1]

if trim('hello  ') != 'hello':
    print('测试失败1')
elif trim('  hello') != 'hello':
    print('测试失败2')
elif trim('  hello  ') != 'hello':
    print('测试失败3')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4')
elif trim('') != '':
    print('测试失败5')
elif trim('    ') != '':
    print('测试失败6')
else:
    print('测试成功!')