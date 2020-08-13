# Author 张楚潼
# 2020/8/9 23:40
import time, datetime
# print(time.time())  # 1596988214.6833982   时间戳 从1970/1/1到此一共经历多少秒
# time.sleep(3)
# print(time.perf_counter())
# print(time.gmtime())  # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=10, tm_hour=2, tm_min=18, tm_sec=36,
# # tm_wday=0, tm_yday=223, tm_isdst=0)  英国格林尼治时间 结构化时间（元组形式）
# print(time.localtime())  # time.struct_time(tm_year=2020, tm_mon=8, tm_mday=10, tm_hour=10, tm_min=27, tm_sec=35,
# tm_wday=0, tm_yday=223, tm_isdst=0)   结构化时间（元组形式）
# struct_time = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))   # 2020-08-10 10:46:29    字符串时间

# print(time.strptime("2020-08-10 10:46:29", "%Y-%m-%d %H:%M:%S"))  # 从字符串时间 -> 结构化时间
# a = time.strptime("2020-08-10 10:46:29", "%Y-%m-%d %H:%M:%S")
# print(a.tm_year)
# print(a.tm_mon)
# print(a.tm_mday)

# print(time.ctime())     # Mon Aug 10 11:07:09 2020
# print(time.ctime(3600)) # Thu Jan  1 09:00:00 1970

# print(time.mktime(a))     # 1597027589.0

print((datetime.datetime.now()))  # 2020-08-10 11:16:57.248055
