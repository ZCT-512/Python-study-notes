# Author 张楚潼
# 2020/8/11 11:10
import configparser as cp
# # 用于生成和修改常见配置文档
# # 各种创建，添加字典的方法
config = cp.ConfigParser()  # 创建ConfigParser对象

config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Host Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'

with open("example.ini", 'w') as configfile:  # 写入操作 ，'DEFAULT'自动放在文件第一个
   config.write(configfile)

config.read("example.ini")  # 读取
# print(config.sections())    # ['bitbucket.org', 'topsecret.server.com'] 默认不输出'DEFAULT'

# print(config.defaults())  # 以字典形式输出'DEFAULT'下的内容
# print('bitbucket.org' in config)  # True


# for i in config:
#     print(i)
#
# # DEFAULT
# # bitbucket.org
# # topsecret.server.com

# for i in config["bitbucket.org"]:    # 不论输出哪个section下的内容，同时也会将“DEFAULT”下的一起输出
#     print(i)
#
# # user
# # serveraliveinterval
# # compression
# # compressionlevel
# # forwardx11


# # 删除块
config.remove_section("bitbucket.org")
config.write(open("example2.ini", "w"))
print(config.has_section("bitbucket.org"))  # False

# # 删除键值对
config.remove_option("topsecret.server.com", "forwardx11")
config.write(open("example2.ini", "w"))
print(config.has_option("topsecret.server.com", "forwardx11"))  # True 确实删了，但“DEFAULT”下也有forwardx11

# # 修改
config.set("topsecret.server.com", "host port", "50000")
config.write(open("example3.ini", "w"))  # 可以放到原来的文件下，不过是覆盖
