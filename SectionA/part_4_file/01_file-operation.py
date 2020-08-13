# Author 张楚潼
# 2020/7/28 16:28

# import datetime
# import time
# f = open("02_black_names.txt", "r")
# f = open("test.txt", "r")

# print(f.tell())
# print(f.read(5))

# print(f.readline())
# print(f.readlines(200))

# num = 0
# for i in f.readlines():
#     num += 1
#     if num == 6:
#         i = "".join([i.strip(),"ooo"])
#     print(i.strip())

# 此种方法不占用内存，推荐
# for i in f:
#     num += 1
#     if num == 6:
#         i = "".join([i.strip(), "ooo"])
#     print(i.strip())

# f.seek(21)
# print(f.read(1))


# f.flush()
# f.close()
