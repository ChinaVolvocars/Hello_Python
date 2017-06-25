# coding=utf-8

# 函数的参数,正常的参数，还可以定义默认参数，可变参数，关键字参数

# 默认参数
def power(x):
    return x * x


# 调用的时候只需要传入一个参数x

print power(2)
print power(3)


# 如果计算x的3次方，x的4次方...
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print power(2, 3)
print power(2, 4)


# print power(2) 是失败的
# 这个时候，默认参数就排上用场了。
# 由于我们经常计算x2，所以，完全可以把第二个参数n的默认值设定为2：
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print '====', power(2)


# 设置默认参数时注意
# 必选参数在前，默认参数在后
# 当函数有多个参数的时候，将变化大的参数放到前面，变化小的放到后面，变化小的可以当默认参数

def student(name, sex):
    print name
    print sex


print student('红孩儿', '男')


def student(name, sex, city='hangzhou', age=12):
    print 'name', name
    print 'sex', sex
    print 'city', city
    print 'age', age


print student('哪吒', '男')


# 默认参数使用不当
def add_end(L=[]):
    L.append('END')
    return L


# 当你正常调用时，结果似乎不错
print add_end([1, 2, 3, 4])
print add_end()  # ['END']
print add_end()  # ['END', 'END']
print add_end()  # ['END', 'END', 'END']


# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 下面的例子
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print add_end()
print add_end()
print add_end()
print add_end()
print add_end()


# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，
# 对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。
# 此外，由于对象不变，多任务环境下同时读取对象不需要加锁，
# 同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，
# 那就尽量设计成不变对象。

# 可变参数 参数可以是一个，俩个，三个......
# 例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
def calc(*num):
    sum = 0
    for n in num:
        sum = sum + n * n
    return sum


print calc(1, 2, 3)

# 如果已经有有一个list或者tuple，要调用可变参数怎么办
nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])

# 以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
calc(*nums)
print calc(*nums)


# 关键字参数 允许传入0个或者任意个含参数名的参数，这些关键字参数在函数内部组装成一个dict
def person(name, age, **kw):
    print 'name：', name, ',age:', age, ',other:', kw


# 函数person除了必选参数name和age外，还接受关键字参数kw
print person('熊猫', 222)
# 传入关键字参数
print person('熊猫', 222, CITY='HANGHZHOU')
print person('熊猫', 222, CITY='HANGHZHOU', Country='CN')
# 关键字参数作用：扩展函数的功能，在person函数里，我们保证能接受name和age俩个参数
# 如果调用者愿意提供更多的参数，我们也能收到。注册的时候除了用户名和年龄必填项之外，
# 其他都是可选项，利用关键字参数来定义可以满足注册需求

# 和可变参数类似，也可以先封装出一个dict，然后把dict转换为关键字参数穿进去
kw = {'CITY': 'HANGHZHOU', 'Country': 'CN'}
print person('哈哈', 22, CITY=kw['CITY'], Country=kw['Country'])
# 简化写法
print person('哈哈', 22, **kw)


# 参数组合 定义函数可以使用必选参数、默认参数、可变参数、关键字参数、这4中参数可以一起使用
# 注意顺序：必选参数、默认参数、可变参数、关键字参数
def func(A, B, C=0, *args, **kw):
    print 'A =', A, 'B =', B, 'C =', C, 'args =', args, 'kw =', kw

print func('A', 'B')
print func('A', 'B', C=44)
print func('A', 'B', C=44, args=('a', 'b'))
print func(1, 2, 3, 'a', 'b', x=99)

# 通过一个tuple和dict，你也可以调用该函数：
arg = (1, 2, 3, 45, 55)
kw = {'ss': 333}
print func(*arg, **kw)
# 所以，对于任意函数，
# 都可以通过类似func(*args, **kw)的形式调用它，
# 无论它的参数是如何定义的

# 默认参数一定是不可变对象，如果是可变对象，运行会有逻辑错误
# 注意:
# *args是可变参数,args接收的是一个tuple
# **kw是关键字参数,kw接收的是一个dict

# 可变参数可以直接传入:func(1,2,3),也可以先组装成list或tuple,再通过*args传入fun(*(1,2,3))
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
