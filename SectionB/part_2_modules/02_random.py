# Author 张楚潼
# 2020/8/10 11:17
import random

# print(random.random())  # [0, 1)  0.6791264325691629
# print(random.randint(1, 10))  # the interval in [a, b]  !整数
# print(random.choice([1, 2, 3, "a", [2, 6, 5]]))
# print(random.sample((1, 2, 3, "a", "b", "c"), 2))  # 在给定序列里随机选择指定个数个元素，以列表形式输出

# b = [1, 2, 3, "a", [2, 6, 5]]
# print(random.shuffle(b))  # 打乱顺序
# print(b)

# print(random.randrange(1, 3))  # range(1,3) -> 1,2 两个元素


# # 验证码生成
def verification_code():
    code = ""
    for i in range(5):
        add_num = random.choice([chr(random.randint(65, 90)), str(random.randrange(10))])
        code += add_num
    return code


print(verification_code())
