#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
使用__slots__
但是，如果我们想要限制实例的属性怎么办？
比如，只允许对Student实例添加name和age属性。

为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

'''


class Hello():
    __slots__ = ('name', 'age')



