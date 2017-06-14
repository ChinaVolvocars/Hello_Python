# coding=utf-8

# 条件判断和循环

# 条件判断
age = 18
if age >= 18:
    print '播放下一集'
    print '广告'

if age >= 18:
    print '农夫山泉'
    print '卡里什'
else:
    print '卡巴斯基'

# if语句执行有个特点，从上往下执行，如果某个判断上是True，就把改判断对应的语句执行了，就会忽略剩下的elif和else
time = 200
if time > 100:
    print '杭州'
elif time > 120:
    print '江南'
else:
    print '东京'

# 循环
# for...in循环，一次把list和tuple中的每一个元素迭代出来
types = ['水果', '蔬菜', '酒']
for type in types:
    print type

types = ('a', 'b', 'c',)
for type in types:
    print type

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    sum = sum + x
    print sum
print sum

# 0,1,2,3,4
print range(5)

# 有序数列0-100
print range(101)

som = 0
for x in range(101):
    som = som + x
print som

# while循环 只要条件满足，一直循环，条件不满足是结束
op = 0
n = 3
while n > 0:
    op = op + n
    n = n - 2
    print n
print op

# raw_input 和 int ;注意将输入的字符转换为int
age = raw_input('你的年龄：')
print age
if age < 1800:
    print '通过'
else:
    print '年龄太小'

birth = raw_input('birth: ')
print birth
if birth < 2000:
    print '00前'
else:
    print '00后'

age = raw_input('你的年龄：')
print age
ag = int(age)
if ag < 18:
    print '通过'
else:
    print '年龄太小'
