#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
# 把函数作为参数传入，这样的函数称为高阶函数，
# 函数式编程就是指这种高度抽象的编程范式
'''


# map() 接受俩个参数，一个函数，一个Iterable
# map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回

def f(X):
    return X * X


i = map(f, [1, 2, 3, 4, 5, 6])
print(i)
print(list(i))
