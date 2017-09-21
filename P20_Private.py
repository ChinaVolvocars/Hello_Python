# coding=utf-8

# 不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，
# 实例的变量名如果以__开头，就变成了一个私有变量（private），
# 只有内部可以访问，外部不能访问，所以，我们把Student类改一改

class Play(object):
    def __init__(self, name, size):
        self.__name = name
        self.__size = size

    def print_score(self):
        print self.__name, self.__size
