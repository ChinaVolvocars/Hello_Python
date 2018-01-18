# coding=utf-8

class Animal(object):
    def run(self):
        print 'Animal is running'


class Dog(Animal):
    def run(self):
        print 'Dog is run....'


class Cat(Animal):
    pass


dog = Dog()

dog.run()

a = list()
b = Animal()
c = Dog()

print isinstance(a, list)
print isinstance(b, Animal)
print isinstance(c, Dog)

print isinstance(c,Animal)

import os


print os.name
