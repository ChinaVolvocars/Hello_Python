# coding=utf-8

# fuction
# 绝对值
print abs(-222)
print abs(333)
print abs(12.44)
print abs(-12.4444)

# print abs(1,2) 报错TypeError
# print abs('12') 报错TypeError

# 比较  Return negative if x<y, zero if x==y, positive if x>y.
print cmp(1, 3)  # 返回 -1
print cmp(1, 1)  # 返回 0
print cmp(4, 3)  # 返回 1

# 数据类型转换
print int('123')
# print int('12.44')
print int(12.44)
print int(-1)
print int(0)
print int(0.77)

# >>> a = abs # 变量a指向abs函数
# >>> a(-1) # 所以也可以通过a调用abs函数
# 调用Python的函数，需要根据函数定义，传入正确的参数。
# 如果函数调用出错，一定要学会看错误信息，所以英文很重要！
