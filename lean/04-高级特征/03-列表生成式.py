#!/usr/bin/python
# -*- coding: UTF-8 -*-

print(list(range(1, 11)))

L = []
for x in range(1, 11):
    L.append(x * x)
print(L)
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])

print([m + n for m in 'abc' for n in 'sdf'])

import os

print([d for d in os.listdir('..')])
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
items_ = [k + '=' + v for k, v in d.items()]
print(items_)

h = ['Hellow', 'World', 'IBM', 'APPLE']
h_ = [s.lower() for s in h]
print(h_)

L1 = ['Hello', 'World', 18, 'Apple', None]
str_ = [l.lower() for l in L1 if isinstance(l, str)]
print(str_)