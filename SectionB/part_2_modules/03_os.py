# Author 张楚潼
# 2020/8/10 12:40
import os, time
# print(os.getcwd())  # 打印当前文件所在路径 D:\pyProjects\fullstack\SectionB\part_2_modules
# print(os.chdir("path"))  # 更改当前文件所在路径为指定路径
# print(os.curdir)  # .
# print(os.pardir)  # ..

# os.makedirs("first\\second\\third")   # 默认在当前目录下生成多层文件夹， 当文件已存在时，无法创建该文件
# os.removedirs("first\\second\\third")  # 只能删除空文件夹

# os.mkdir("a")            # 生成单级目录
# os.mkdir("first\\b")     # 要保证b前的目录存在
# os.rmdir("a\\b")          # 只删除最后一级

# print(os.listdir("D:\\课件资料\\中外教育史\\"))  # 列出指定目录下的所有文件和子目录，包括隐藏文件，并以列表方式打印

# os.remove("text.py")  # 只能删文件，不能删文件夹
# os.rename("first", "abc")  # 重命名文件或文件夹

# os_stat_result = os.stat(".\\01_time.py")  # 获取文件/目录信息
# print(os_stat_result.st_size)   # 1201  文件大小

# print(os_stat_result.st_atime)  # 上次访问时间 时间戳形式 1597054450.2217684
# print(time.ctime(os_stat_result.st_atime))  # Mon Aug 10 18:14:10 2020

# print(os.sep)   # win下 "\"  (Linux下为"/" )
# os.linesep    # 输出当前平台使用的行终止符 win下 "\r\n"
# print(os.pathsep)  # 输出用于分割文件路径的字符串 win下 ";"
# print(os.system("dir"))
# print(os.environ["PATH"])  # 获取系统环境变量  字典形式


# print(os.path.abspath("01_time.py"))  # 返回path规范化的绝对路径   D:\pyProjects\fullstack\SectionB\part_2_modules\01_time.py
# print(os.path.split(r"D:\pyProjects\fullstack\SectionB\part_2_modules\01_time.py")) # 将path分割成目录和文件名二元组返回
# ('D:\\pyProjects\\fullstack\\SectionB\\part_2_modules', '01_time.py')

# print(os.path.dirname(r"D:\pyProjects\fullstack\SectionB\part_2_modules\01_time.py"))  # 返回path的目录。其实就是os.path.split(path)的第一个元素
# D:\pyProjects\fullstack\SectionB\part_2_modules

# os.path.basename(path)  # 返回path最后的文件名。如何path以／或\结尾，那么就会返回空值。即os.path.split(path)的第二个元素
# os.path.exists(path)  # 如果path存在，返回True；如果path不存在，返回False
# print(os.path.isabs(r"D:\pyProjects\fullstack\SectionB\part_2_modules\01_time.py"))  # 如果path是绝对路径，返回True
# os.path.isfile(path)  # 如果path是一个存在的文件，返回True。否则返回False
# os.path.isdir(path)  # 如果path是一个存在的目录，则返回True。否则返回False
# os.path.join(path1[, path2[, ...]])  #将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
# os.path.getatime(path)  # 返回path所指向的文件或者目录的最后存取时间
# os.path.getmtime(path)  # 返回path所指向的文件或者目录的最后修改时间
