# coding=utf-8

# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 我们判断对象类型，使用type函数
# 基本类型用type判断

print  type(123)
print type('str')
print type(None)


# 一个变量指向函数或者类，也可以用type()判断
print type(abs)

class Dog(object):
    def __init__(self):
        print 'HA'


dog = Dog()

print type(dog)


# 限制属性 slots