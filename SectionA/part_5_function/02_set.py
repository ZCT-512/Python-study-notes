# Author 张楚潼
# 2020/8/2 10:30

# set_a = ("ABCDABCDEFG")
# print(set(set_a), type(set(set_a)))
#
# set_b = ["A", "B", "C", "A", "B", "AB"]
# print(set(set_b), type(set(set_b)))
#
# # set内的元素必须可哈希的（即不可变量），但set本身是不可哈希的（即可变的），故可以对set添加修改
#
# # frozenset 冻结集合，不可变
# print(frozenset(set_a), type(frozenset(set_a)))
#
# set_c = set([1, 2, 3, 1, 2, 3])
# set_c.add(4)
# set_c.update([5, 1, 2, 3, 4, 5, "abc"])
# set_c.update("def")
# set_c.remove(1)
# m = set_c.pop()
# # set_c.clear()
# print(set_c, m)
#
#
# # 集合类型的操作
# # in 和 not in
# f = set("zct")
# print("z" in f)
#
# # == 和 !=
# print(set("zct") == set("zctzct"))
# print(set("zct") != set("zc"))
#
#
# # 交集(&) 并集(|) 差集 对称差集（反向交集）
# set_a = set([1, 2, 3, 4, 5])
# set_b = set([3, 4, 5, 6, 7])
# print(set_a.intersection(set_b))  # {3, 4, 5}.  a & b
# print(set_a.union(set_b))  # {1, 2, 3, 4, 5, 6, 7}.  a | b
# print(set_a.difference(set_b))  # {1, 2},in a but not in b.   a - b
# print(set_b.difference(set_a))  # {6, 7},in b but not in a.   b - a
# print(set_a.symmetric_difference(set_b))  # {1, 2, 6, 7}.     a ^ b
#
# # 超集（父集），子集
# print(set_a.issuperset(set_b))  # a是否是b的父集  a > b
# print(set_a.issubset(set_b))    # a是否是b的子集  a < b
