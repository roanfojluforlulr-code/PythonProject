# 导入模块
import my_module_1
my_module_1.test(10, 20)
# 导入不同模块的相同功能
from my_module_1 import test
from my_module_2 import test
test(1, 2)