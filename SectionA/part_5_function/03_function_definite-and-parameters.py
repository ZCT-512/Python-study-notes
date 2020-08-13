# Author 张楚潼
# 2020/8/3 10:34


# def print_info(name, age):
#     print("Name : %s" % name)
#     print("Age  : %d" % age)
#
#
# print_info("zct", 20)  # 必须参数
# print_info("20", 22)
#
# print_info(name="zct", age=20)  # 关键字参数
# print_info(age=20, name="zct")


# def print_info(name, age, sex="male"):  # 默认参数,(需要跟在其他参数后)
#     print("Name : %s" % name)
#     print("Age  : %d" % age)
#     print("Sex  : %s" % sex)
#
#
# print_info("zct", 20)
# print_info("czh", 20, "female")


# def add(*nums):  # 不定长参数 nums = (1, 2, 3, 5, 6, 7, 435)
#     res = 0
#     for i in nums:
#         res += i
#     print(nums)
#     print(res)
#
#
# add(1, 2, 3, 5, 6, 7, 435)


# def print_info(name, sex="male", *args, **kwargs):  # *args放在左边，**kwargs放在右边
#     print("name : %s" % name)
#
#     print("sex : %s" % sex)
#
#     print(args)
#
#     for i in kwargs:
#         print(i, kwargs[i])
#
#
# print_info("zct", "male", 2, 3, "io", jib="student", age=20)
#
# # 参数位置 ：关键字参数, 默认参数, *args, *kwargs

# def f(*args):
#     print(args)
#
#
# # # 若想将一个列表的值放在f里，只需
# f(*[1, 2, 3])   # (1, 2, 3)
# f(*[1, 2, 3], *[4, 5, 6], [7, 8, 9])  # (1, 2, 3, 4, 5, 6, [7, 8, 9])

# def f(**kwargs):
#     print(kwargs)
#
#
# # # 若想将字典放到f里，只需
# f(**{"a":1,"b":2},**{"c":3,"d":4})  # {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# def f(x, y):  # x,y为形参
#     print(x+y)
#
#
# f(1, 2)  #  1，2是实参

# import time
#
#
# def logger(m):
#     time_format = "%Y-%m-%d %X"
#     time_current = time.strftime(time_format)
#     with open("03_log-record", "a") as f:
#         f.write("%s end action%d\n" % (time_current, m))
#
#
# def f1(x):
#     print("some functions")
#     logger(x)
#
#
# def f2(x):
#     print("some functions")
#     logger(x)
#
#
# def f3(x):
#     print("some functions")
#     logger(x)
#
#
# f1(2)
# f2(3)
# f3(6)
