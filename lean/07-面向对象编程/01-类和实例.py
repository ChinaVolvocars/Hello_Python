#!/usr/bin/python
# -*- coding: UTF-8 -*-

# class

class Ha(object):
    pass


ha = Ha()
print(ha)

ha.name = 'china'
ha.age = 77

print('name:%s,age:%d' % (ha.name, ha.age))


#  注意：特殊方法“__init__”前后分别有两个下划线！！！

class Hei(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


hei = Hei('财经', 34)
print(hei.name, hei.age)
