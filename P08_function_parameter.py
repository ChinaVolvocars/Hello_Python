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

# 关键字参数
# 参数组合
