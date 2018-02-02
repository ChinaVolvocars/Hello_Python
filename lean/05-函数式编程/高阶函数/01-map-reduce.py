#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# 把函数作为参数传入,这样的函数称为高阶函数,
# 函数式编程就是指这种高度抽象的编程范式
'''


# map() 接受俩个参数,一个函数,一个Iterable
# map将传入的函数依次作用到序列的每个元素,并把结果作为新的Iterator返回

def f(X):
    return X * X


i = map(f, [1, 2, 3, 4, 5, 6])
print(i)
print(list(i))

print('------------------------------')

iterator = map(str, [1, 2, 3, 4, 5, 6])
print(iterator)
print(list(iterator))

'''
reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：

reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
'''
from functools import reduce


def add(x, y):
    return x + y


reduce1 = reduce(add, [1, 3, 5, 7, 9])
print(reduce1)


def fn(x, y):
    return x * 10 + y


reduce2 = reduce(fn, [1, 3, 5, 7, 9])
print(reduce2)


def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]


reduce3 = reduce(fn, map(char2num, '13579'))
print(reduce3)

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return DIGITS[s]

    return reduce(fn, map(char2num, s))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
