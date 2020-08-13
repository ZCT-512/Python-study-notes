# Author 张楚潼
# 2020/7/28 0:01
# 我找了一个 省市县区的excel 表
China = {
    "北京":
        {"东城区": {},
         "延庆县": {}},
    "山西": {
        "太原":
            {'小店区': {}, '迎泽区': {}, '杏花岭区': {}, '尖草坪区': {}, '万柏林区': {}, '晋源区': {}},
        "大同":
            {'城区': {}, '矿区': {}, '南郊区': {}, '新荣区': {}, '阳高县': {}, '天镇县': {}},
        "晋城":
            {'城区': {}, '沁水县': {}, '阳城县': {}, '陵川县': {}, '泽州县': {}, '高平市': {}},
        "晋中":
            {'榆次市': {}, '介休市': {}, '榆社县': {}}},
    "山东": {},
    "陕西": {},
    "湖南": {},
    "湖北": {}
    }


exit_flag = False
current_layer = China
layers = [China]

# current_layer 存放当前要打印的一个字典（打印的是它的键）
# layers列表：用于存放每次选择后的下级字典（列表中后一个元素（字典类型），是前一个元素（字典类型）某一键的值（字典类型））

while not exit_flag:
    for k in current_layer:
        print(k)
    choice = input(">>:")
    if choice == "b":
        current_layer = layers.pop()

    # 若输入其他字符 则重新打印刚刚显示的信息并选择
    elif choice not in current_layer:
        continue
    else:
        # 在进入下一层之前，先将其存到layers列表最后
        layers.append(current_layer)
        # 更新current_layer，进入下一层
        current_layer = current_layer[choice]
