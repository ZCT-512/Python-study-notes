# Author 张楚潼
# 2020/8/4 18:44

# # 高阶函数
# # 1.函数名可作为参数输入
# # 2.函数名可以作为返回值
# def f(x):
#     return x**2
#
#
# def g(x, y, func):
#     return func(x) + func(y)
#
#
# print(g(2, 4, f))
# # 函数名可以当作函数参数

# def f():
#     print("aaa")
#
#
# g = f
# g()  # aaa
# # 函数名可以赋值


# def z():
#     def in_f():
#         return 10
#     return in_f  # 此处返回的是函数名
#
#
# print(z())  # <function z.<locals>.in_f at 0x000001D7C5E7EF70>
# d = z()
# print(d())  # 10
# # 函数名可以作为返回值


# # 递归函数
# def f(x):   # 循环方法
#     s = 1
#     for i in range(1, x+1):
#         s *= i
#     return s
#
#
# print(f(5))


# def g(x):   # 递归方法
#     if x == 1:
#         return 1
#     else:
#         return x * g(x-1)
#
#
# print(g(5))

# # 递归特点：
# #1.调用自身
# #2.一定有结束条件

# #但凡可以用递归解决的问题，循环也可以
# #递归效率很低


# def h(x):    # 斐波那契数列
#     if x == 1 or x == 2:
#         return 1
#     else:
#         return h(x-1) + h(x-2)
#
#
# for i in range(1, 11):
#     print(h(i), end=" ")


# # 几个重要的内置函数
# filter 过滤器， 过滤内容在fun1中定
# def func1(s):
#     if s != "a":
#         return s
#
#
# str1 = "abcd"
# ret1 = filter(func1, str1)
# print(ret1)   # <filter object at 0x0000021AD0F50CD0>
# print(list(ret1))

# # map函数
# def fun2(s):
#     return s + "something"
#
#
# str2 = "abcd"
# ret2 = map(fun2, str2)
# print(ret2)   # <map object at 0x0000021AD0FC9520>
# print(list(ret2))

# #reduce 函数
# from functools import reduce
#
#
# def add(x, y):
#     return x * y
#
#
# print(reduce(add, range(1, 10)))  # reduce结果就是一个值
# # 阶乘

# # lambda 匿名函数
# # lambda x, y: x + y

# print(reduce(lambda x, y: x * y,range(1, 10)))
# # 简化
