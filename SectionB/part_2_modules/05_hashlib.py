# Author 张楚潼
# 2020/8/10 19:41
import hashlib as h
# # 用于加密相关的操作

m = h.md5()   # <md5 HASH object @ 0x000001DCC22E7930>

m.update("abc".encode("utf-8"))  # python3 里字符串默认是unicode 编码
print(m.hexdigest())  # 十六进制表达 900150983cd24fb0d6963f7d28e17f72
m.update("efg".encode("utf-8"))
print(m.hexdigest())  # fbd7809b1f99a5b790068736a1c62cf0         # 连续两次的m.update 生成的是两个字符串拼接结果的密文

m2 = h.md5()
m2.update("abcefg".encode("utf-8"))
print(m.hexdigest())  # fbd7809b1f99a5b790068736a1c62cf0

n = h.sha256()
n.update("abc".encode("utf-8"))
print(n.hexdigest())   # ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
