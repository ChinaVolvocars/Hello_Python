#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 切片

d = ['a', 'b', 'c', 'd']

# 去前三个元素
d_ = d[0:3]
print(d_)
print(d[:3])
# 倒着切片
print(d[-2:-1])

l = list(range(50))
print(l)
print(l[0:10])
print(l[-10:])
print(l[10:20])
print(l[0:10:2])
print(l[::6])
print(l[:])

t = (0, 1, 2, 3, 4, 5)
print(t[:3])
# 字符串也可以进行切片
