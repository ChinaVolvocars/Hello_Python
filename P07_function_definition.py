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

# 参数检查
