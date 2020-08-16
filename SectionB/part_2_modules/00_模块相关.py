# Author 张楚潼
# 2020/8/13 21:38
# 导入模块操作后：通过搜索路径找到该模块，解释器将该模块的所有代码加载完赋给这个变量（模块名）★
# import calfuncs  # 最好不要用这种导入方式 以防那里的函数和本文件里的函数由于重名而发生混乱★
# ret = calfuncs.step_operation("-2/-5")
# print(ret)   # 0.4


# from calfuncs import step_operation as so # 用啥函数就写出来
# ret = so("-2/-5")
# print(ret)  # 0.4

# # 模块是函数的集合，包是模块的集合（实现按目录组织模块）

# import 模块包.func1             # 这样导入包里的模块不对
# func1.func1()  # name 'func1' is not defined

# from 模块包 import func1  # 这样可以
# func1.func1()  # runned func1!

# import 模块包.模块包2.func2       #  name 'func2' is not defined
# from 模块包.模块包2 import func2  # 这样可以★★
# func2.func2()  # runned func2!

# from 模块包.模块包2 import func2.func2  # 不能这样导入模块里的方法
# func2.func2()  # runned func2!
# from 模块包.模块包2.func2 import func2  # 这样可以★★
# func2.func2()  # runned func2!

# import 模块包2  # No module named '模块包2' 因为这个包和当前文件不在同一级
# import 模块包   # 现在执行的是模块包下的__init__.py。哈哈哈
# 导入包就是执行该包下的__init__.py文件★★
