# coding=utf-8

# 高阶函数
# 变量可以指向函数
# 以Python内置的求绝对值的函数abs()为例，调用该函数用以下代码：
print abs(-10)

# 但是,如果只写abs呢?
print abs  # <built-in function abs>
# abs(-10)是函数调用,而abs是函数本身

# 要获得函数调用结果，我们可以把结果赋值给变量：
x = abs(-10)
print x

# 如果把函数本身赋值给变量呢？
f = abs
print f
# 结论:函数本身也可以赋值给变量，即：变量可以指向函数。

# 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
print f(-52)  # 说明变量f现在已经指向了abs函数本身

# 函数名也是变量
# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 如果把abs指向其他对象，会有什么情况发生？
abs = 10


# print abs(-10)
# Traceback (most recent call last):
#   File "C:/Users/Administrator/PycharmProjects/Hello_Python/P14_Higher_order_function.py", line 28, in <module>
#     print abs(-10)
# TypeError: 'int' object is not callable

# 把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数了！
# 当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。
# 注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def add(X, Y, F):
    return f(X) + f(Y)
add1 = add(2, 3, -7)
print add1
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式
