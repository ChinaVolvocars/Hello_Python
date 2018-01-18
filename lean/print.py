# -*- coding: utf-8 -*-
'''
:ivar


'''

import sys

print('hello wordl')
print('hhah', 'hahaha', 'china')
print(1)
print(1 + 2)
print(1 == 2)

# s = input('please input your name')
# print(s)

print('1023*768 = ', 'xxx')
print('%s%d%f%x' % ('hahah', 1, 0.2, 0xfff))
print(r'''hello,\n
world''')
print(r'\\\t\\')
print('中文的str')
print(ord('a'))
print(ord('A'))
print(chr(5526))
print(chr(85224))
print(chr(752))
print('\u4e2d\u6587')

x = b'ABC'
print(x)
encode = 'ABC'.encode('ascii')
print(encode)
b = '中文'.encode('utf-8')
print(b)

i = len('ABC')
len1 = len('中文')
print(i)
print(len1)
print(len(b'aaaaa'))
print(len('中文'.encode('utf-8')))
'''
%d  整数
%f  浮点数
%s  字符串
%x  十六进制整数
'''

for i in range(1, 5):
    for k in range(1, 5):
        print('%d%d' % (i, k))

l = [1, 2, 3, 55, 43, 222, 68]

_ = (1,)
print('-----------------')
_1 = (11, 221, 3453, 45657665, 7875)
l.append(_1)
print(l.__sizeof__())

for e in range(6):
    l.append(e)
print('-----------------')
for ee in l:
    print(ee)

if i > 1:
    print("++++")
elif i < 0:
    print("llll")
else:
    print("-----")
'''
height = 1.75
weight = 80.5
bmi = weight / height
if bmi < 18.5:
    print("过轻")
elif 18.5 >= bmi < 25:
    print("正常")
elif bmi >= 25 & bmi < 28:
    print("过重")
elif bmi >= 28 & bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')
'''
height = 1.75
weight = 80.5
bmi = weight / height
if bmi < 18.5:
    print("过轻")
elif 18.5 >= bmi < 25:
    print("正常")
elif 25 >= bmi < 28:
    print("过重")
elif 28 >= bmi < 32:
    print('肥胖')
else:
    print('严重肥胖')

# [] ()
# {}
l1 = set([1, 3, 4, 55, 55, 67, 84, 22])
print(l1)

b_ = {'A': 1, 'B': 2}
l2 = set([1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6])
print(l2)

# list []
l3 = [1, 2, 3, 4, 5, 56, 6, 77, 777]
print('list:', l3)
# tuple ()
_2 = (1, 2, 3, 4, 56, 7, 8, 9)
print('tuple：', _2)
# dict {}
c_ = {'a': 1, 'b': 2, 'c': 3}
print('dict:', c_)
# set set([])
s = set([1, 2, 3, 3, 5, 6, 6, 7, 7, 8, 88])
print('set:', s)

print('--------------------')
print(hex(255))
print(hex(22))
print(hex(360))
