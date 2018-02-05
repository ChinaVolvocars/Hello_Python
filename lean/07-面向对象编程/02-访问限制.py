#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Hello(object):

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        print('%s：%s' % (self.__name, self.__age))