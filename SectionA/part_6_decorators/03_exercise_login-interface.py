# Author 张楚潼
# 2020/8/6 16:05
flag = 0   # 登录成功便置 1


def login(dic_users):
    # 用户注册判断
    name = input("用户名：")
    while name not in dic_users.keys():
        print("该用户未注册！")
        name = input("用户名：")

    # 是否在黑名单判断
    # flag_password = 1
    l_f = open("03_black-names", "r")
    black_list = l_f.readlines()
    for num in range(len(black_list)):
        if name == black_list[num].strip():
            print("您已被加入黑名单！")
            # flag_password = 0
            l_f.close()

    # 登录密码判断
    times = 0
    while times < 3:  # and (flag_password == 1):
        password = input("密码：")
        if password == dic_users[name]:
            # flag_password = 0  若密码正确 则return 1,函数结束，不需要flag_password标志来退出了
            print("欢迎登陆，%s！" % name)
            return 1
        else:
            times += 1
            print("用户名或密码错误，请重新输入!")

    # 锁定判断操作
    if times == 3:
        print("您的账户已被锁定！")
        l_f = open("03_black-names", "a")
        l_f.write("".join([name, "\n"]))
        l_f.close()
    else:
        l_f.close()


def if_login(auth):
    def en(func):
        def inner():
            global flag
            if flag == 0:
                if auth == "WeChat":
                    f = open("03_WeChat-users", "r")
                    str_users = f.readline()
                    dic_users = eval(str_users)
                    f.close()
                elif auth == "JD":
                    f = open("03_JD-users", "r")
                    str_users = f.readline()
                    dic_users = eval(str_users)
                    f.close()
                else:
                    dic_users = {}
                if login(dic_users) == 1:
                    flag = 1
                    func()
            else:
                func()
        return inner
    return en


@if_login("WeChat")
def home():
    print("现在展示的是home 界面，可继续浏览其他界面！")


@if_login("JD")
def finance():
    print("现在展示的是finance 界面，可继续浏览其他界面！")


@if_login("JD")
def book():
    print("现在展示的是book 界面，可继续浏览其他界面！")


dic_jm = {1: {"home": home}, 2: {"finance": finance}, 3: {"book": book}}
while True:
    for i, v in dic_jm.items():
        print(i, list(v.keys())[0])
    key = input("输入要进入的界面序号：")
    if key == "q":
        break
    else:
        key = int(key)
        list(dic_jm[key].values())[0]()
flag = 0            # 退出登录，登录标志重新置0
print("已退出，谢谢光临！")


# 2020/8/6 17:41 完成基本功能
# 2020/8/6 18:31 调用修改之前写的登录函数以实现成功调用
