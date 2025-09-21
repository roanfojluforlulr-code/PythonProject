# 方式二
"""
from 包名 import*
模块名.目标
"""
# 跟模块一样，只针对import*。手动导入可以
from My_package import * # 手动导入: my_module_1,my_module_2

my_module_1.info_print_1()
# my_module_2.info_print_2() 不在__all__里