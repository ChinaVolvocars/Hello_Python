#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    pass

class Cat(Animal):
    def run(self):
        print('Cat is running')


dog = Dog()
print(dog.run())
cat = Cat()
print(cat.run())

