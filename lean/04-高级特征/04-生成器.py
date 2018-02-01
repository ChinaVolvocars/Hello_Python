#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 一边循环一边计算的机制，称为生成器：generator。

L = [x * x for x in range(10)]
print(L)
print('--------------------------------------------------')
g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print('--------------------------------------------------')
g1 = (x * x for x in range(10))
for v in g1:
    print(v)

print('--------------------------------------------------')


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


print(fib(5))

print('--------------------------------------------------')


def fibs(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


generator = fibs(5)
print(generator)

print('--------------------------------------------------')


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


odd1 = odd()
print(odd1)
next(odd1)
next(odd1)
next(odd1)
print('--------------------------------------------------')

odd2 = odd()
for nn in odd2:
    print(nn)

print('-----------------------sss---------------------------')

while True:
    try:
        x = next(generator)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
