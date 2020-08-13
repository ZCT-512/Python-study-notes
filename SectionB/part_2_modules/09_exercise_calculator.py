# Author 张楚潼
# 2020/8/12 13:12
import re


# # 计算二元运算式
def step_operation(short_str):
    """
    函数用来计算二元运算式，即a(+-*/)b，这个最底层的运算。
    输入和返回值均为字符串类型。
    a b 均可正可负，一共2*4*2=16种组合， 即支持"-1.2+-5.6", "-1.2--5.6", "-1.2*-5.6", "-1.2/-5.6 这些输入。
    """
    # 先处理 +-, --, *-, /- 四种情况
    if re.findall("\\+-", short_str) == ["+-"]:
        short_str = re.sub("\\+-", "-", short_str)
    elif re.findall("--", short_str) == ["--"]:
        short_str = re.sub("--", "+", short_str)
    elif re.findall("\\*-", short_str) == ["*-"]:   # *- 情况又分a为+，a为- 两种
        if re.findall("^-", short_str) == ["-"]:
            short_str = re.sub("-", "", short_str)
        else:
            short_str = re.sub("-", "", short_str)
            short_str = "".join(["-", short_str])
    elif re.findall("/-", short_str) == ["/-"]:     # /- 情况又分a为+，a为- 两种
        if re.findall("^-", short_str) == ["-"]:
            short_str = re.sub("-", "", short_str)
        else:
            short_str = re.sub("-", "", short_str)
            short_str = "".join(["-", short_str])
    else:
        pass

    one_of_four = re.findall("[*+/]", short_str)    # 可解决6种情况 -5+3 -8*6 -9/7  5+3  8*6  9/7

    if one_of_four == ["*"]:
        multiplication_list = re.split("\\*", short_str)
        return str(float(multiplication_list[0]) * float(multiplication_list[1]))
    elif one_of_four == ["/"]:
        division_list = re.split("/", short_str)
        return str(float(division_list[0]) / float(division_list[1]))
    elif one_of_four == ["+"]:
        plus_list = re.split("\\+", short_str)
        return str(float(plus_list[0]) + float(plus_list[1]))
    # 另外两种情况 -2-5   2-5
    elif re.findall("-", short_str) == ["-"]:
        subtract_list = re.split("-", short_str)  # 2-5 --> ["2", "5"]
        return str(float(subtract_list[0]) - float(subtract_list[1]))
    elif re.findall("-", short_str) == ["-", "-"]:
        subtract_list = re.split("-", short_str)  # -2-5 --> ["", "2", "5"]
        return "".join(["-", str(float(subtract_list[1]) + float(subtract_list[2]))])
    else:
        print("暂不支持此种运算！")


# # 乘除法运算
def multiplication_division_operation(long_str):
    while "*" in long_str or "/" in long_str:  # 这个条件和下一行的都可以
        step_part = re.search("-?\\d+\\.?\\d*[/*]-?\\d+\\.?\\d*", long_str).group()  # 注意匹配二元运算式的方法
        long_str = re.sub("-?\\d+\\.?\\d*[/*]-?\\d+\\.?\\d*", step_operation(step_part), long_str, 1)  # 一次只替换一个二元运算式
    return long_str


# # 加减法运算
def plus_subtract_operation(long_str):
    # while "+" in long_str or "-" in long_str:  这个条件不可以用了
    while len(re.findall("-?\\d+\\.?\\d*[+\\-]-?\\d+\\.?\\d*", long_str)) != 0:
        step_part = re.search("-?\\d+\\.?\\d*[+\\-]-?\\d+\\.?\\d*", long_str).group()  # 注意匹配二元运算式的方法
        long_str = re.sub("-?\\d+\\.?\\d*[+\\-]-?\\d+\\.?\\d*", step_operation(step_part), long_str, 1)  # 一次只替换一个二元运算式
    return long_str


# # 运算函数（先乘除，后加减）
def resolution(formula):
    formula = multiplication_division_operation(formula)
    formula = plus_subtract_operation(formula)
    return formula


# # 检查哈合法性函数
def check_legitimacy(s):

    return s


# # 使规范化函数
def standardize(s):
    s = re.sub("\\s", "", s)     # 去空格
    s = "".join(["(", s, ")"])   # 最外层加括号
    return s


# # 输入要计算的表达式
expression = input("请输入要计算的式子：")

# # 检查哈合法性，若出现空格不成对、空括号、非法字符（字母，$ # @...）、非法表示(**,//,***等)
# expression = check_legitimacy(expression)

# # 规范化：去空格，化简++ -+ *+ /+，并输出“正数不需要加+号”, 不论原式最外面是否有括号，再整体加一个括号。。。
expression = standardize(expression)


while len(re.findall("-?\\d+\\.?\\d*[+\\-*/]-?\\d+\\.?\\d*", expression)) != 0:
    # # 取得第一个最里面一层多元运算式（  带一对括号，比如(8/2+7*56)  ）
    ret = re.search("\\([^()]+\\)", expression).group()

    # # 去掉括号，得到 8/2+7*56 这样的形式
    m = re.findall("[^(].+[^)]", ret)[0]

    # # 将其计算并替换
    expression = re.sub("\\([^()]+\\)", resolution(m), expression, 1)  # 一次只替换一个二元运算式
    # print(expression)  # 一括号,一步骤
if len(re.findall("^\\(-?\\d+\\.?\\d*\\)$", expression)) == 1:
    expression = expression.replace("(", " ")
    print(expression.replace(")", " "))
else:
    print(expression)
# # 2020/8/12 22:27 完成基本功能，支持加减乘除四则混合运算，支持浮点数输入 待添加1：负数输入计算问题
# # 2020/8/13 00:50 解决了负号的计算问题 待修改2：关于多元算式的结束条件（还是负号的问题！）
# # 2020/8/13 10:11 解决了待修改2 完成了要求 可增加1：更多的运算方式 比如幂运算 **, 可增加2：合法性检查，规范化函数
