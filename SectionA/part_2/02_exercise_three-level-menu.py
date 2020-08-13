# Author 张楚潼
# 2020/7/27 19:38

China = {
    "北京": {
         "东城区": {},
         "西城区": {},
         "崇文区": {},
         "宣武区": {},
         "朝阳区": {},
         "丰台区": {},
         "石景山区": {},
         "海淀区": {},
         "门头沟区": {},
         "房山区": {},
         "通州区": {},
         "顺义区": {},
         "昌平区": {},
         "大兴区": {},
         "平谷区": {},
         "怀柔区": {},
         "密云县": {},
         "延庆县": {}},
    "山西": {
        "太原":
            {'小店区': {},
             '迎泽区': {},
             '杏花岭区': {},
             '尖草坪区': {},
             '万柏林区': {},
             '晋源区': {}, '清徐县': {}, '阳曲县': {}, '娄烦县': {}, '古交市': {}},
        "大同":
            {'城区': {},
             '矿区': {},
             '南郊区': {},
             '新荣区': {},
             '阳高县': {},
             '天镇县': {}, '广灵县': {}, '灵丘县': {}, '浑源县': {}, '左云县': {}, '大同县': {}},
        "晋城":
            {'城区': {},
             '沁水县': {}, '阳城县': {}, '陵川县': {}, '泽州县': {}, '高平市': {}},
        "晋中":
            {'榆次市': {},
             '介休市': {},
             '榆社县': {}, '左权县': {}, '和顺县': {}, '昔阳县': {}, '寿阳县': {}, '太谷县': {}, '祁县': {}, '平遥县': {}, '灵石县': {}}},
    "山东": {},
    "陕西": {},
    "湖南": {},
    "湖北": {}
    }

quit_flag = False
while True:
    for key in China:
        print(key)
    choise = input("请输入要查询的省：").strip()
    if choise in China:
        while not quit_flag:
            for key2 in China[choise]:
                print(key2)
            choise2 = input("请输入要查询的地级市：").strip()
            if choise2 in China[choise]:
                while not quit_flag:
                    for key3 in China[choise][choise2]:
                        print(key3)
                    choise3 = input("请输入要查询的县级市：").strip()
                    if choise3 in China[choise][choise2]:
                        while not quit_flag:
                            for key4 in China[choise][choise2][choise3]:
                                print(key4)
                            choise4 = input("请输入要查询的地点：").strip()
                            print("最后一级")
                    elif choise3 == "q":
                        quit_flag = True
                    else:
                        break
            elif choise2 == "q":
                quit_flag = True
            else:
                break
    elif choise == "q":
        quit_flag = True
    else:
        break

# 2020/7/28 0:30 现阶段思路只完成了基本查询功能
# 2020/7/28 10:12 实现了要求,缺点：能查询层数取决于写的while层数，重复量大
