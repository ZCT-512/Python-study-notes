# Author 张楚潼
# 2020/8/10 23:05
import logging as lg
# # 日志模块  5个级别由高到低 critical > error > warning > info > debug
# log.debug("debug message!")        # 默认设置下debug info 级别不够输出
# log.info("info message!")          # 默认设置下debug info 级别不够输出
# log.warning("warning message!")    # WARNING:root:warning message! 默认设置下从warning级别输出
# log.error("error message!")        # ERROR:root:error message!
# log.critical("critical message!")  # CRITICAL:root:critical message!

# lg.basicConfig(level=lg.DEBUG,  # 指定输出级别
#                format="%(asctime)s %(filename)s [lines:%(lineno)d] %(levelname)s %(message)s",
#                datefmt="%Y/%m/%d %H:%M:%S",
#                filename="06_log.log",  # 添加日志绝对路径 若没有该参数，默认输出在屏幕上
#                filemode="a")  # 默认是追加 "a"

# lg.debug("debug message!")         # 2020/08/11 00:17:45 06_logging.py [lines:17] DEBUG debug message!
# lg.info("info message!")           # 2020/08/11 00:17:45 06_logging.py [lines:18] INFO info message!
# lg.warning("warning message!")
# lg.error("error message!")
# lg.critical("critical message!")

""""******************************Logger******************************"""

logger = lg.getLogger()  # 创建建一个Logger对象 用于写入日志文件
fh = lg.FileHandler("06_logrer.log")  # mode默认是 "a"

ch = lg.StreamHandler()  # 创建建一个Handler对象 用于输出到控制台（屏幕）

# # 给定输出格式
formatter = lg.Formatter("%(asctime)s %(filename)s [lines:%(lineno)d] %(levelname)s %(message)s")

# # 给对象指定格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)


# # 指定logger的输出形式（两种都创建的话：）
logger.addHandler(fh)
logger.addHandler(ch)

logger.setLevel(lg.DEBUG)        # 修改输出级别

logger.debug("debug message!")   # 默认还是从warning级别输出
logger.info("info message!")
logger.warning("info message!")  # 2020-08-11 10:39:35,267 06_logging.py [lines:43] WARNING info message!
logger.error("error message!")
logger.critical("critical message!")

""""******************************Logger******************************"""
