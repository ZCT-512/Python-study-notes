# Author 张楚潼
# 2020/8/2 9:18
import copy
# # 浅拷贝
# s = [[1, 2, 3], 2, 3]
#
# s1 = s
# s1[0][2]=5
# print(s, s1)
# print(id(s), id(s1))
#
# # s2 = s[0:0] 和copy一样
# # a.copy就是copy.copy(a)
# s2 = s.copy()
# print(id(s[0]), id(s2[0]))
# # copy 后，s2 的元素 3，4 等一层元素的地址与s中3，4地址不同，而列表的地址与s中的列表地址相同
# # 即copy只复制一层

# 一个小应用
# 每张卡都有户名，卡号，额度，余额信息，
# Card = ["zct", "7758", [15000, 9000]]
# Card_1 = Card.copy()
# # copy后，该副卡户名，卡号信息可以单独修改，不影响主卡对应信息
# Card_1[0] = "jwg"
# Card_1[1] = "1234"
# print(Card_1)
# # 但对于列表信息copy后是共享的，故
# Card[2][1] -= 2000
# print(Card_1)

# deepcopy 另外完全克隆一份内容
# Card_2 = copy.deepcopy(Card)
# Card_2[0] = "jky"
# Card_2[1] = "6666"
# Card_2[2][1] -= 2000
# print(Card, Card_2)
