#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys


# from __future__ import unicode_literals


def test():
    args = sys.argv
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()

# 别名

try:
    import cStringIO as StringIO
except ImportError:
    import StringIO

try:
    import json
except ImportError:
    import simplejson as json  # python <= 2.5


# 作用域
# 非公开（private） _XXX 和__xxx

def _pivate_1(name):
    return 'HELLO ,%s' % name


def _prvate_2(name):
    return 'hi ,%s' % name


def getName(name):
    if len(name) > 2:
        return _pivate_1(name)
    else:
        return _prvate_2(name)


# 使用第三方模块
# 使用__future__
# 使用新语法
# from __future__ import unicode_literals

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)

# 'xxx' is unicode? True
# u'xxx' is unicode? True
# 'xxx' is str? False
# b'xxx' is str? True

print 10 / 3  # //地板除
print 10.0 / 3

# from __future__ import division

print 10 / 3
