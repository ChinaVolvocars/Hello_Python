# coding=utf-8

# 我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：

# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x nf
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print fact(2)
print fact(5)
print fact(10)
print fact(100)

# 任何递归函数都存在栈溢出的问题
