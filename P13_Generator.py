# coding=utf-8

# 生成器

# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，
# 列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，
# 不仅占用很大的存储空间，
# 如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白
# 浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？
# 这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的机制，称为生成器（Generator）

L = [X * X for X in range(10)]
print L
g = (x * x for x in range(10))
print g
# 创建L和g的区别仅在于最外层的[]和()，
# L是一个list，而g是一个generator。

# generator如何打印每一个元素
print g.next()
print g.next()
print g.next()
print g.next()
# 我们讲过，generator保存的是算法，
# 每次调用next()，就计算出下一个元素的值，
# 直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。

for N in g:
    print N
