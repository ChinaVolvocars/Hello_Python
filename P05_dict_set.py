# coding=utf-8

# dict和set
# dict 全称dictionary ,其他语言称为map，使用键-值（key-value）进行存储，查找速度快
name = ['D', 'C', 'B', 'A']
fruits = ['74', '75', '76', '78']

d = {'D': '4', 'C': '5', 'B': '6', 'A': '8'}
print d['D']

# 水果对应价格
fruit = {'apple': 3.5, 'w': 2.7, 'x': 3.3}
print fruit['apple']

# 通过key把value放入
fruit['apple'] = 4
print fruit['apple']

# 通过in的方式判断key是否存在
print 'apple' in fruit
print 'am' in fruit

# 通过dict提供的get方法，如果key不存在，就可以返回None，或者自己指定value
print fruit.get('apple')
print fruit.get('apple', -1)

print fruit.get("a")
print fruit.get('a', -12)
# 注意：返回None的时候Python的交互式命令行不显示结果。

# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。

# 空间来换取时间的一种方法
# dict的key必须是不可变对象

# 为了保证hash的正确性，作为key的对象就不能变；在python中，字符串，证书都是不可变的
# 因此可以放心的作为key；而list是可以变的，就不能作为key


# set
# set和dict类似，也就是一组key，但不存储value，由于可key不能重复，所以在set集合中
# 没有重复的key
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 2, 3, 4])
print s
# 注意，传入的参数[1,2,3]是一个list，而显示的set([1,2,3,4])
# 只是告诉你这个set内部有1，2，3，4这4个元素，显示的[]不表示这是一个list

# 重复的元素在set中被自动过滤
v = set([1, 1, 1, 2, 3, 44, 4, 44])
print v

# 通过add(key)的方法可以添加元素到set中，但是重复的不起效果
v.add(3)
print v
v.add(3)
v.add(3)
print v

# 通过remove(key)的方法删除元素
v.remove(3)
print v
