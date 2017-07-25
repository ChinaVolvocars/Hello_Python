# coding=utf-8

# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。

# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 23, 4, 5, 66, 33)
print f  # <function sum at 0x0017F930>

# 调用函数f时，才真正计算求和的结果：
print f()

# 在这个例子中我们在函数lazy_sum()中定义了函数sum，
# 并且，内部函数sum可以引用外部函数lazy_num的参数和局部变量时
# 当lazy_num返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为‘闭包（closure）’
# 注意：我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的函数
f1 = lazy_sum(1, 2, 3, 4, 5)
f2 = lazy_sum(1, 2, 3, 4, 5)
print 'f1 == f2 :', f1 == f2


# 闭包
# 注意到返回的函数在其定义内部引用了局部变量args，所以,当一个函数返回一个函数后，其内部的局部变量还是被新函数引用
# 所以，闭包用起来简单，实现起来可不容易
# 另外需要注意:返回的函数并没有立刻执行,而是直到调用f()才执行
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs

print f1
print f2
