# Author 张楚潼
# 2020/8/11 18:17
import re
# # 正则表达式是用来匹配字符串的
'''************************ findall ************************'''
# ret = re.findall("ab", "ruihgdbvkabebfabioasabs")  # . 完全匹配
# print(ret)   # ['ab', 'ab', 'ab']

# ret = re.findall("w\\w{2}l", "hello world")       # 模糊匹配
# print(ret)   # ['worl']

# ret = re.findall("^he...", "hello world")         # ^ 开头匹配
# print(ret)   # ['hello']

# ret = re.findall("...ld$", "hello world")         # $ 结尾匹配
# print(ret)   # ['world']

# ret = re.findall("ab*", "azxsabbbabbab")         # * 重复匹配（[0, +∞]）
# print(ret)   # ['a', 'abbb', 'abb', 'ab'] a+0个b,到无穷个b,都匹配

# ret = re.findall("ab+", "azxsabbbabbab")         # + 重复匹配（（[1, +∞]）
# print(ret)   # ['abbb', 'abb', 'ab'] a+1个b,到无穷个b,都匹配

# ret = re.findall("ab?", "azxsabbbabbab")         # ? 01重复匹配（（[0, 1]）
# print(ret)   # ['a', 'ab', 'ab', 'ab'] a+0个b,或1个b,只匹配两种情况

# ret = re.findall("ab{1,3}", "abbbbzxsabbbabbab")         # 指定个数匹配(可以是范围)
# print(ret)   # ['abbb', 'abbb', 'abb', 'ab']
# ret = re.findall("ab{1,3}", "abbbb")         # 指定个数匹配(可以是范围，{1,+∞}用{1,}表示)
# print(ret)   # ['abbb']  重复匹配的三个：贪婪匹配 取最大的一个输出

# ret = re.findall("a[a-z]b", "hello world agb avcb")         # [] 字符集匹配
# print(ret)   # ['agb']  多选一
# ret = re.findall("[acd,]", "hello world, agb")         # 字符集匹配,注意该中括号里是四个字符
# print(ret)   # ['d', ',', 'a']
# # []可以 取消元字符的特殊功能(\ ^ -这三种除外)
# ret = re.findall("a[+*.{}]", "a.ba+ca*da{2a}")         # 字符集匹配
# print(ret)   # ['a.', 'a+', 'a*', 'a{', 'a}']
# # ^放在[]里：取反
# ret = re.findall("[^0-9]", "a1.2b3,4a5+6c")         # 匹配除0-9以外的其他全部字符
# print(ret)   # ['a', '.', 'b', ',', 'a', '+', 'c']
# ret = re.findall("[^,]", "a,bcd")         # 匹配除逗号（,)以外的其他全部字符
# print(ret)   # ['a', 'b', 'c', 'd']

# ret = re.findall(r"(ab)+", "abb")               # ()表示 分组
# print(ret)   # ['ab']

# ret = re.findall("www\\.(\\w+)\\.com", "www.github.com")   # 按规则找，但只输出组里的内容
# print(ret)   # ['github']
# ret = re.findall("www\\.(?:\\w+)\\.com", "www.github.com")   # ?: 可以输出匹配到的全部内容
# print(ret)   # ['www.github.com']

# ret = re.search("(?P<name>[a-zA-Z]{2,3})/(?P<num>\\d{6})", "zct/123456dg/654321")
# print(ret.group())         # zct/123456
# print(ret.group("name"))   # zct
# print(ret.group("num"))    # 123456

# ret = re.findall("a|b", "abcbde")               # | 表示 或
# print(ret)   # ['a', 'b', 'b']

# # \反斜杠
# # 1.反斜杠加普通字符 赋予其特殊意义
# ret = re.findall("1\\d{10}", "zct15303466186zct219862705796")       # \d -> [0-9]
# print(ret)   # ['15303466186', '19862705796']                       # \D -> [^0-9]
# ret = re.findall("\\s.*", "zct15303466186 zct219862705796")         # \s -> [\f\n\r\t\v] 空字符
# print(ret)   # ['15303466186', '19862705796']                       # \S -> [^\f\n\r\t\v]非空字符
# ret = re.findall("\\w{14}", "zct15303466186 zct19862705796")        # \w -> [A-Za-z0-9_]
# print(ret)   # ['zct15303466186', 'zct19862705796']                 # \W -> [^A-Za-z0-9_]
# ret = re.findall("guo\\b", "hi daguo, hello world")        # \b -> 匹配与特殊字符的边界（比如与空格，逗号，$符等的）
# print(ret)     # ['guo']                                   # \B -> 匹配非特殊字符的边界


'''************************* finditer ************************'''
# # 将findall匹配到的结果(一个列表)以迭代器返回
ret = re.finditer("\\d", "1qa2eqw56dq3we")
print(ret)   # <callable_iterator object at 0x0000017245D3A580>
print(next(ret))  # <re.Match object; span=(0, 1), match='1'>
print(next(ret))  # <re.Match object; span=(3, 4), match='2'>
print(next(ret).group())   # 5
print(next(ret).group())   # 6
'''************************* search ************************'''
# # 只找第一个 且返回的是一个对象包括匹配到的范围和内容
# ret = re.search("\\s.*", "zct15303466186 zct19862705796")
# print(ret)   # <re.Match object; span=(14, 29), match=' zct19862705796'>
# print(ret.span())   # (14, 29)
# print(ret.group())  # zct19862705796
# # 相当于：
# # ret = re.search("\\s.*", "zct15303466186 zct19862705796").group()
# # print(ret)

# # \反斜杠
# # 2.反斜杠加元字符 取消其特殊意义
# ret = re.search("^he\\.", "he.llo world").group()
# print(ret)   # he.
# ret = re.search("^he\\+", "he+llo world").group()
# print(ret)   # he+

# ret = re.search("^he\\\\l", r"he\llo world").group()
# print(ret)   # he\l
# ret = re.search("^he\\\\\\\\l", r"he\\llo world").group()
# print(ret)   # he\\l
# # 或者相当于：
# # ret = re.search(r"^he\\l", r"he\llo world").group()
# # print(ret)   # he\l
# # ret = re.search(r"^he\\\\l", r"he\\llo world").group()
# # print(ret)   # he\\l


'''************************* match ************************'''
# # 只匹配开头，且返回的是一个对象，可调用group方法
# ret = re.match("140525.*", "140525194910010000").group()
# print(ret)  # 140525194910010000


'''************************* split ************************'''
# ret = re.split("[sk]", "s123s4k56k7s89")
# print(ret)  # ['', '123', '4', '56', '7', '89']  注意若分割字符前没有内容，则分一个"空"出来


'''************************* sub,subn ************************'''
# ret = re.sub("AV", "BV", "AVAV123456789", 1)  # 次数默认全换
# print(ret)  # BV123456789
# ret = re.sub("1..4", "+-*/qwer", "AV123456789")
# print(ret)  # AV+-*/qwer56789
# ret = re.subn("\\d", "A", "q1w5e6d213", 2)      # 次数默认全换
# print(ret)   # ('qAwAe6d213', 2)      # 会同时将替换的次数输出
'''************************* compile ************************'''
# # 可以将前面集中方法的第一个参数(匹配规则)放到一个对象里,便于多次使用
# p = re.compile("AV.{9}")
# ret = p.findall("AV123456789 BV789456123 AV147258369 BV963852741")
# print(ret)  # ['AV123456789', 'AV147258369']
