# coding=utf-8

# 匿名函数
# 当我们传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便
# 在python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(X)的函数外，还可以直接传入匿名函数
l = map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print l


# 通过对比可以看出，匿名函数lambda x:x*x 实际上就是
def f(X):
    return X * X


# 关键字lambda表示匿名函数，冒号前面的x表示匿名参数

# 匿名函数有个限制，就是只能有一个表达式，不用写reture，返回值就是该表达式的结果
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把
# 匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print f(2)
