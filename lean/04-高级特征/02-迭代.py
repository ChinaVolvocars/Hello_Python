#!/usr/bin/python
# -*- coding: UTF-8 -*-

from collections import Iterable

# list

l = [12, 4532, 1, 332323, 4, 5, 33, 56, 234, 867]
for x in l:
    print(x)
print('------------------------------------')

# tuple
t = (1, 3, 4, 5, 623, 22, 1122, 4454)
for xx in t:
    print(xx)

print('------------------------------------')
# dict
c_ = {'a': 1, 'b': 22, 'c': 55}
for ch in c_:
    print(ch)
print('------------------------------------')

for key in c_:
    print(key)
print('------------------------------------')
for values in c_.items():
    print(values)
print('------------------------------------')
for k, v in c_.items():
    print('k:%s,v:%s' % (k, v))

print('------------------------------------')
instance = isinstance('acc', Iterable)
print(instance)
print('------------------------------------')
b = isinstance([1, 2, 3], Iterable)
print(b)
print('------------------------------------')

b1 = isinstance(123, Iterable)
print(b1)
print('------------------------------------')

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

print('------------------------------------')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)


def findMinMax(L):
    min = L[0]
    max = L[0]
    for i in L:
        if i >= max:
            max = i
        if min > i:
            min = i
    return (min, max)


print('------------------------------------')

min_max = findMinMax(l)
print(min_max)


