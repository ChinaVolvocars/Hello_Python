# coding=utf-8

# 函数定义
# 在python中定义函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:,然后在缩进
# 块中编写函数体，函数的返回值用return语句返回

# 定义一个求绝对值的函数
def mine_abs(x):
    if x > 0:
        return x
    else:
        return -x


print mine_abs(111)
print mine_abs(-111)


# 注意：函数体内的语句在执行时，一旦执行到return是，
# 函数执行完毕，并将结果返回，因此函数内部可以通过判
# 断和循环实现非常复杂的逻辑
# 如果没有return语句，函数执行完毕后也后返回结果，只是结果为None
# return None 简写：return

# 空函数 定义一个什么都不做的空函数，可以用pass语句
def nop():
    pass


# pass什么都不做，实际上用来当做占位符，比如还没想好写函数的代码，
# 就可以用pass代替，先让代码运行起来
a = 11
if a > 11:
    pass


# 无pass 运行会有语法错误

# 参数检查，对传入的参数进行类型比对，如果不对就报错
def mine_abs(x):
    if not isinstance(x, int or float):
        raise TypeError('参数类型不匹配')
    if x > 0:
        print x
    else:
        return -x


# 添加了参数检查，如果传入的参数类型错误，函数则会抛出一个异常

# 返回多个值 ,返回值是一个tuple
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print move(199, 222, 22, math.pi / 6)

# 定义函数时，需要确定函数名和参数个数；
# 如果有必要，可以先对参数的数据类型做检查；
# 函数体内部可以用return随时返回函数结果；
# 函数执行完毕也没有return语句时，自动return None。
# 函数可以同时返回多个值，但其实就是一个tuple。
