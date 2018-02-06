#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用type()

print(type(123))
print(type('222'))
print(type(0.23))
print(type(None))

import types


def nn():
    pass


function_type = type(nn) == types.FunctionType
print(function_type)
builtin_function_type = type(abs) == types.BuiltinFunctionType
print(builtin_function_type)
lambda_type = type(lambda x: x) == types.LambdaType
print(lambda_type)
generator_type = type((x for x in range(10))) == types.GeneratorType
print(generator_type)

# 使用isinstance()

class Animal(object):
    pass


animal = Animal()


class Dog(Animal):
    pass


dog = Dog()


class Cat(Animal):
    pass


cat = Cat()

print(isinstance(dog, Dog) and isinstance(dog, Animal))
