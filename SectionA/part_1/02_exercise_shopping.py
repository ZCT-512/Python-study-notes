# Author 张楚潼
# 2020/7/26

#    购物车程序
# 输入工资 salary = 5000
# 输出商品清单：
# 1. 名称 价格
# 2.
# 3.
#
# 顾客选择商品序号
# >>>1
#     余额不足，差多少
# >>>2
#     商品已加入购物车，当前余额为多少
# >>>quit
#     您已购买以下商品：
# 商品1 价格
# 商品2 价格
#
# 你的余额为：多少
# 欢迎下次光临

salary = int(input("请输入您拥有的金额："))
# 看basket的注释
# 由于使用的append方法将goods中的每个元素（应该是一个有两个参数的列表 商品名和单价）赋给basket，但由于basket的元素是有三个量的列表，故将goods的每个元素添加了一个基数量1
goods = [("a", 1200, 1),
         ("b", 750, 1),
         ("c", 36, 1),
         ("d", 460, 1),
         ("e", 5000, 1),
         ("f", 2300, 1),
         ("g", 380, 1),
         ("h", 100, 1)]
# basket的每一个元素是一个有三个参数的列表，分别为 商品名，单价，数量
basket = []

# 输出商品清单：
for num in range(len(goods)):
    print("%d.%s:%6.1d元" % (1+num, goods[num][0], goods[num][1]))

# 购物开始
# x为购买商品种类数
kinds_of_goods = 0
while 1:
    select = input("请输入想要购买的商品标号[退出：quit]：")
    if select.isdigit():
        select = int(select)
        if (select > 0) and (select <= len(goods)):
            if goods[select - 1][1] <= salary:
                salary -= goods[select - 1][1]
                if list(goods[select - 1]) in basket:
                    # 若已经购买过该商品，则数量加1
                    basket[basket.index(list(goods[select - 1]))][2] += 1
                else:
                    basket.append(list(goods[select - 1]))
                    # 每购买一种新商品时，x要加1
                    kinds_of_goods += 1
                    basket[kinds_of_goods - 1][2] = 1
                print("%s 已加入您的购物车，当前余额为 %d 元。" % (goods[select - 1][0], salary))
            else:
                print("当前余额不足，还差 %d 元才可购买此商品！" % (goods[select - 1][1] - salary))
        else:
            print("商品编号不存在！")
            break

    elif select == "quit":
        # 退出并输出购物车清单：
        print("-----您已购买以下商品------\n序号 名称   单价   数量")
        for num in range(len(basket)):
            print(" %d.  %s:" % (1+num, basket[num][0]), "%5.2d元" % basket[num][1], "%d个".rjust(5) % basket[num][2])
        print("------------------------")
        print("您的余额为 %d 元。\n" % salary, "欢迎下次光临!")
        break
    else:
        print("输入无效，若要退出购物，请输入 quit。")
        break

# 2020/7/26  22:45 修改1：注意商品种类数x的引入，在进行购买多种同种商品加数量时，x-1作为basket内的索引值
# 2020/7/26  23:00 修改2：注明了goods列表的元素中基数1添加原因
# 2020/7/27  10:56 修改3：修改了相同商品不一起买就不能累计数量的问题
# 2020/7/27  12:11 修改4：将打印清单格式化输出
