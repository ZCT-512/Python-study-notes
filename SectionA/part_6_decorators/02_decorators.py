# Author 张楚潼
# 2020/8/5 12:18
# # 装饰器的作用：是个函数，是为其他函数增加功能用的
# # 问题：要在执行函数时输出运行时间
# def f():
#     s = time.time()
#     print("something!")
#     time.sleep(2)
#     e = time.time()
#     print(e - s)
#
# f()
# # 1.爱原函数内修改代码，若函数过度，代码重复

# def show_func_runtime(func):
#     import time
#     s = time.time()
#     func()
#     e = time.time()
#     print(e - s)
#
#
# def f():
#     print("aaa")
#
#
# show_func_runtime(f)
# # 2.定义一个函数用来计时，但改变了原来函数的调用方式


# # 一、不带参数的装饰器
# import time
#
#
# def show_func_runtime(func):
#     def inner():  # 闭包函数
#         s = time.time()
#         func()
#         e = time.time()
#         print("运行时间为 %s" % (e - s))
#     return inner
#
#
# def f1():
#     time.sleep(1)
#     print("aaa")
#
#
# f1 = show_func_runtime(f1)
#
#
# @show_func_runtime   # 在函数开头添加装饰器，相当于在函数后面加 f2 = show_func_runtime(f2)
# def f2():
#     time.sleep(2)
#     print("bbb")
#
#
# @show_func_runtime
# def f3():
#     time.sleep(3)
#     print("ccc")
#
#
# f1()
# f2()
# f3()


# # 二、带参数的功能函数的装饰器
# import time
#
#
# def show_func_runtime(func):
#     def inner(*args, **kwargs):  # 闭包函数
#         s = time.time()
#         func(*args, **kwargs)
#         e = time.time()
#         print("运行时间为 %s" % (e - s))
#     return inner
#
#
# @show_func_runtime
# def add(*args, **kwargs):
#     ret = 0
#     for i in args:
#         ret += i
#     print(ret)
#     time.sleep(1)
#
#
# add(1, 2, 3, 4, 5)


# # 三、带参数的装饰器
# import time
# #
# #
# def looger(flag=0):
#     def show_func_runtime(func):     # 闭包函数
#         def inner(*args, **kwargs):  # 闭包函数
#             s = time.time()
#             func(*args, **kwargs)
#             e = time.time()
#             print("运行时间为 %s" % (e - s))
#             if flag:                         # 因为这里需要一个参数判断是否要输出日志，而判断参数由外层给出
#                 print("03_log-record ")            # 故要再扩一层，故 show_func_runtime 变为一个闭包函数
#         return inner
#     return show_func_runtime
#
#
# @looger(True)   # 先执行looger函数，返回show_func_runtime，故相当于  @show_func_runtime
# def add(*args, **kwargs):
#     ret = 0
#     for i in args:
#         ret += i
#     print(ret)
#     time.sleep(1)
# #
# #
# @looger()
# def f2():
#     time.sleep(2)
#     print("bbb")
#
#
# add(2, 4, 6)
# f2()
