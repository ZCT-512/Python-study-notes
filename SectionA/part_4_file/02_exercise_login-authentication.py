# Author 张楚潼
# 2020/7/29 20:51
dic_users = {
    "张楚潼": "123456",
    "jwg": "234567",
    "czh": "345678"
}
# 用户注册判断
name = input("用户名：")
while name not in dic_users.keys():
    print("该用户未注册！")
    name = input("用户名：")

# 是否在黑名单判断
flag = 1
f = open("02_black_names.txt", "r")
black_list = f.readlines()
for num in range(len(black_list)):
    if name == black_list[num].strip():
        print("您已被加入黑名单！")
        flag = 0
        f.close()

# 登录密码判断
times = 0
while (times < 3) and (flag == 1):
    password = input("密码：")
    if password == dic_users[name]:
        flag = 0
        print("欢迎登陆，%s！" % name)
    else:
        times += 1
        print("用户名或密码错误，请重新输入!")

# 锁定判断操作
if times == 3:
    print("您的账户已被锁定！")
    f = open("02_black_names.txt", "a")
    f.write("".join([name, "\n"]))
    f.close()
else:
    f.close()
# 2020/7/29 22:02 完成基本功能，问题1：当输入的用户名不在字典字典中时，输完密码会直接锁定该用户名
# 2020/7/30 11:05 解决了问题1，增加了用户注册判断
