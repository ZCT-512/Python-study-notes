# Author 张楚潼
# 2020/8/7 18:28
# #生成器的两种创建方式
# # 1.（列表生成式）
# a = (x*2 for x in range(5))
# # print(a)  # <generator object <genexpr> at 0x0000022F5F29A190>  生成器对象 不存在值，需要时可以生成出来，不需要时没有，不占内存，
#           # 比较列表生成器，值全在内存，当range里的数很大时，会卡
# print(next(a))  # print(a.__next__())

# for i in (x*3 for x in range(5)):  # 生成器是可迭代对象
#     print(i ,end=" ")

# # 2. yield


# def f():
#     print("a")
#
#     yield 1
#
#     print("b")
#     yield 2


# f()  # 不执行print（”ok“）
# print(f)    # <function f at 0x000001C4CEBC61F0>
# g = f()
# print(g)  # <generator object f at 0x0000029D78F1A190>

# print(next(g))  # a 1
# print(next(g))  # b 2

# next(g)  # 超过次数，StopIteration


# for i in f():
#     print(i)
# a 1 b 2
# # for的in后面加的是内部有iter方法的对象


# def fib(x):
#     n, before, after = 0, 0, 1
#     while n < x:
#         # print(after, end=" ")
#         yield after
#         before, after = after, before + after
#         n += 1
#
#
# g = fib(10)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

# # send方法（可以向里发送值的next方法）

# def f():
#     print("ok1")
#     count = yield 1
#     print(count)
#
#     yield 2
#
#
# g = f()
#
# g.send(None)  # 第一次调用，值写None,相当于next(g)
# print(g.send("qwe"))
