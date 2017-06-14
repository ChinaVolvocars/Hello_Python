# coding=utf-8
# 数据类型和变量

print 'hello python'
print 'hello world'
print 'This is python', 'leraning coding', 'wole'
print 100 + 200
print '100 + 200 =', 100 + 200

# name = raw_input()
# print name

# sex = raw_input("please enter your sex")
# print sex

# 输出和输入 print raw_input()

a = 100
if a > 200:
    print 'learning'
else:
    print  'world'

# 数据类型和变量
# 数据类型：整数、浮点数、字符串、布尔值、空值

# 字符串 转义字符 \
print 'I\'m \"OK\"'
print "I'm ok"

# 转义字符 \n 表示换行；\t 表示制表符；\\ 表示转义字符就是\
print 'I\'m learning \n python'

#
print ('\\\t\\')

# r''表示''内部的字符串默认不转义
print (r'\\\t\\')

# '''...'''的格式表示多行内容,多行字符串'''...'''还可以在前面加上r使用
print('''line1
... line2
... line3''')
print ('''Meahu
公司
已经成立
30年''')
print r'''
多行字符串\'\'\'\.\.\.\'\'\'
还可以在前面
加上r使用
'''

# 布尔值
print '布尔值', True
print '布尔值', False

# 布尔值运算 and 、or、not
# and 运算相同结果为True，不同结果则为False
print 'True and True =', True and True
print 'True and False =', True and False
# or 运算只要有True，结果就是True
print 'True or True =', True or True
print 'True or False =', True or False
# 非运算，True变成False，False变成True
print 'not True =', not True
print 'not False =', not False

# 空值 None 具有特殊意义的一个值
print None

# 变量
a = 1
print a
a = a + 1
print a
an = True
v = 'ABC'  # 内存中创建一个'ABC'的字符串；内存中创建一个a的变量，并把它指向'ABC'

aa = 'ABC'
bb = aa
aa = 'XYZ'
print bb

# 常亮
PI = 3.14159265359
print PI

# 整数除以整数永远是整数，如果一个是浮点数结果就不在市整数了
print 10 / 3
print 10.0 / 3

# 取余数
print 10 % 8

