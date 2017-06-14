# coding=utf-8

# 字符串和编码

# python的诞生比Unicode标准发布还早，最早的python只支持ASCII

# 字母和对应ASCII编码 使用ord(),chr() 相互转换
print ord('a')
print ord('A')
print ord("a")
print ord("A")

print chr(97)
print chr(65)

# Unicode表示的字符串用u'...'
print u'中文'
u'中文'
print u'\u4e2d'

# 把u'xxx'转换为UTF-8编码的'xxx'用encode('utf-8')
print u'abc'.encode('utf-8')
print u'中文'.encode('utf-8')

# 英文字符转换后表示的UTF-8的值和Unicode值相等（但占用的存储空间不同）
# ，而中文字符转换后1个Unicode字符将变为3个UTF-8字符，你看到的\xe4就是其中一个字节，
# 因为它的值是228，没有对应的字母可以显示，所以以十六进制显示字节的数值。
print len(u'ABC')
print len('ABC')
print len(u'中文')
print len('\xe4\xb8\xad\xe6\x96\x87')

# UTF-8编码表示的字符串'xxx'转换为Unicode字符串u'xxx'用decode('utf-8')
print 'ABC'.decode('UTF-8')
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 格式化 用%实现，如果只有一个括号可以省略
print 'hello,%s' % 'world'
print 'hi %s,you have $%d' % ('Michael', 1000)

print '中国,%s个民族,%d万平方公里,%d个士兵' % ('56', 960, 20000000000)

# 常见占位符
# %d 整数
# %f 浮点数
# %s 字符串
# %x 十六进制整数
print '%d-%d' % (6, 1)
print '%2d-%d' % (6, 1)
print '%2d-%02d' % (6, 1)
print '%2d-%03d' % (6, 1)

# 不确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串
print '大叔: %s. 西瓜: %s' % (25, True)

# 转义%
print '%d %%' % 12
print '%d %% ,占个总数%d %%' % (23, 56)
