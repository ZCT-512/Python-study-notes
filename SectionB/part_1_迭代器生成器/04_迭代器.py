# Author 张楚潼
# 2020/8/9 18:50

# 生成器都是迭代器，
list1 = [1, 2, 3]
d = iter(list1)  # 等效list1.__iter__()
# print(d)   # <list_iterator object at 0x0000025BEA390CD0>
# 什么是迭代器？
# 1.有iter方法， 2.有next方法
# print(next(d))
# print(next(d))
# print(next(d))

# for 循环内部三件事：
# 1.调用可迭代对象的iter方法生成一个迭代器。
# 2.不断调用迭代器对象的next方法。
# 3.处理StopIteration异常。

from collections import Iterable, Iterator
print(isinstance(list1, list))  # True
print(isinstance(list1, Iterable))  # True
print(isinstance(list1, Iterator))  # False
print(isinstance(d, Iterable))  # True
print(isinstance(d, Iterator))  # True
