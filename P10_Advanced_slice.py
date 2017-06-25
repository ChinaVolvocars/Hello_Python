# coding=utf-8
# 娶一个lsit或tuple的部分元素是非常常见的操作
L = ['A', 'B', 'C', 'D', 'E']
# 取前三个元素
print L[0], L[1], L[2]
# 取前n个元素
r = []
n = 3
for i in range(3):
    r.append(L[i])
print r

# 使用python的切片操作符
print '使用切片', L[0:3]
# 从1开始
print L[1:3]

# 倒数切片 倒数第一个元素的索引是-1。
print L[-1]
print L[-3]
print L[-2]

# 创建以恶搞0-99的数列
L = range(100)
print L

print '取出前10个数', L[:10]
print '取出后10个数', L[-10:]
print '取出前11-20个数', L[10:20]
print '前10个，每俩个取一个', L[:10:2]
print '所有数，每5个取一个', L[::5]
print '只写[:]就可以原样复制一个list', L[:]

# tuple也是一种list，唯一的区别是tuple是不可变，tuple切片操作，结果仍然是tuple、
t = (0, 1, 2, 3, 4, 5)
print '取出前3个数', t[:3]
print '取出后3个数', t[-3:]

# 字符串也可切片，结果啥事字符串
s = 'ABCDEF'
print '取出前3个', s[:3]
