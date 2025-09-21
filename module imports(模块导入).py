# 模块导入一般写在开头位置， 通过"."来确定层级关系
# 模块是一个python文件(以.py结尾)，能定义函数、类和变量
# 相当于一个工具包
"""
语法：
[from 模块名] import [模块|类|变量|函数|*] [as 别名]
"""
# 用import导入time的sleep功能(函数)
import time
print("开始等待5s")
time.sleep(5)
print("等待完成")
# from 模块名 import功能名--（具体）
from time import sleep
print("开始等待1s")
sleep(1)
print("等待完成")
# from 模块名 import *
# 用 * 导入time所有功能
from time import*
print("等待2s")
sleep(2)
print("等待完成")
# as别名
# 模块别名
import time as t
t.sleep(1)
print("还没完")
# 功能别名
from time import sleep as t
t(2)
print("结束了")