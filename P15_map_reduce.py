# coding=utf-8

# Python内建了map()和reduce()函数
# map()函数接收俩个参数，一个函数，一个序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回

# 举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：
def f(x):
    return x * x


l = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print l  # [1, 4, 9, 16, 25, 36, 49, 64, 81]


def g(x):
    return x + 3


map1 = map(g, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map1

# map()传入的第一个参数是f，即函数对象本身。
#
# 你可能会想，不需要map()函数，写一个循环，也可以计算出结果：
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print L
# 的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

# 所以，map()作为高阶函数，事实上它把运算规则抽象了，
# 因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
map2 = map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print map2


# ruduce的用法。rudeuce把一个函数作用在一个序列[x1,x2...]上，这个函数必须接收俩个参数，
# reduce把结果继续和序列的下一个元素累计运算
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

# 比方说对一个序列求和，就可以用reduce实现：
def add(X, Y):
    return X + Y


print reduce(add, [1, 3, 5])


# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x, y):
    return x * 10 + y


print reduce(fn, [1, 3, 5])


# 如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print reduce(fn, map(char2num, '13579'))


def str2int(s):
    def fv(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fv, map(char2num, s))


print str2int('1234')


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# s = raw_input()


# Python内建的filter()函数用于过滤序列
def is_odd(n):
    return n % 2 == 1


print '过滤', filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])


# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
    return s and s.strip()


filter1 = filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print filter1

# sorted
print sorted([36, 5, 12, 9, 21])


# 此外，sorted()函数也是一个高阶函数，
# 它还可以接收一个比较函数来实现自定义的排序。
# 比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
# 对于两个元素x和y，如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，则返回1
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0


print sorted([36, 5, 12, 9, 21], reversed_cmp)

print sorted(['bob', 'about', 'Zoo', 'Credit'])


# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，
# 只要我们能定义出忽略大小写的比较算法就可以：
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0


print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)
