# coding=utf-8

# list 有序集合

namelist = ['Tom', 'Car', 'Vov', 'Bao']
print namelist
print len(namelist)

print namelist[0]
print namelist[1]
print namelist[2]
print namelist[3]
# 最后一个的索引
print namelist[len(namelist) - 1]

# -1 做索引取的是最后一个元素
print namelist[-1]
print namelist[-2]
print namelist[-3]
print namelist[-4]

# 追加元素到末尾
namelist.append('Win')
print namelist

# 将元素插入指定位置
namelist.insert(1, 'Cou')
print namelist

# 删除list末尾的元素
namelist.pop()
print namelist

# 删除指定位置的元素
namelist.pop(1)
print namelist

# 把某一个元素替换成别的元素
namelist[1] = 'LTD'
print namelist

# 不同的数据类型
lc = ['A', 1, ['n', 'c', 'v', "a", 100], True]
print lc
print len(lc)

# 空的lsit
p = []
print len(p)

# tuple 元组,一旦初始化就不能修改
tp = ('HAHA', 'Tiger', 1)
print tp
print tp[0]
print tp[1]
print tp[2]

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (100, 200, 300)
print t

# 空的tuple
t = ()
print t

# 1个元素的tuple,需要加个逗号, ，来消除奇异；显示的时候：(188,)
t = (188,)
print t

# 定义的不是tuple，
# 是10这个数！
# 这是因为括号()既可以表示tuple，
# 又可以表示数学公式中的小括号，
# 这就产生了歧义，因此，Python规定，
# 这种情况下，按小括号进行计算，计算结果自然是10。
t = (10)
print t

# 可以变的tuple，不是说一旦定义就不能变的吗
g = ('1', '2', '3', ['Q', 'W', 'E'])
print g
g[3][0] = 'q'
g[3][1] = 'w'
g[3][2] = 'e'
print '\'tuple\'变了', g
