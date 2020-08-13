# Author 张楚潼
# 2020/8/4 13:50

# def f():
#     print("aaa")
#     return 10   # 结束函数（后面的语句不被执行），返回某个值。若没有return,则返回None
#
#
# a = f()
# print(a)


def f():
    return 1, 2, "aa", [1, 4, "12"], {"a": 1}


print(f())  # (1, 2, 'aa', [1, 4, '12'], {'a': 1})
# # 若后有多个对象，则自动以元组形式打包返回


# x = int(3.5)  # int built_in
# g_count = 2  # global 全局变量
#
#
# def outer():
#     o_count = 1  # enclosing
#
#     def inner():
#         l_count = 4  # local 局部变量
#         print(l_count)
#
#     inner()
#     print(o_count)
#
# outer()

# count = 10
#
#
# def f():
#     # global count  # 函数内不能修改全局变量，除非 global 声明
#     # print(count)
#     count = 5
#     print(count)
#
# f()
# print(count)


# def outer():
#     o_count = 1
#
#     def inner():
#         nonlocal o_count  # 作用和 global 一样
#         o_count = 4
#         print(o_count)
#
#     inner()
#     print(o_count)
#
# outer()


# # 作用域查找顺序： 局部 > 外层 > 当前模块中的全局 > 内置
# # 只有模块、类、函数才能引入新的作用域



