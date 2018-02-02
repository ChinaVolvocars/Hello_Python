#!/usr/bin/python
# -*- coding: UTF-8 -*-

# filter()用于过滤
def is_odd(n):
    return n % 2 == 1


i = filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
l = list(i)
print(l)

print('-----------------------------')


def not_empty(s):
    return s and s.strip()


iterator = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
list1 = list(iterator)
print(list1)
