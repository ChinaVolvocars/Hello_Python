# coding=utf-8

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式

#  生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用range(1, 11)：
print range(1, 11)

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)

print L

# 列表生成式则可以用一行语句代替循环生成上面的list
print [x * x for x in range(1, 11)]

# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print [x * x for x in range(1, 22) if x % 2 == 0]

# 还可以嵌套
range_ = [v + s for v in range(1, 22) for s in range(44, 99)]
print range_

# 运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os  # 导入os模块

listdir___ = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print listdir___

# for循环其实可以同时使用俩个甚至多个变量，比如dict的iteritems()可以同时迭代key和value
d = {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}
for k, v in d.iteritems():
    print k, '=', v

# 因此列表生成式，也可以使用俩个变量生成list
iteritems_ = [k + '=' + v for k, v in d.iteritems()]
print iteritems_

# list中的所有字符变成小写
k = ['Kkkk', 'AAAAAA', 'BBBBB']
k_ = [s.lower() for s in k]
print k_

# 运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。
# 使用内建的isinstance函数可以判断一个变量是不是字符串：