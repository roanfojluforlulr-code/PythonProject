import random, json
# 语法1: 变量: 类型
# 语法2: #type: 类型

var_1: int = 10
var_2: float = 3.1415926
var_3: bool = True
var_4: str = "帅哥"
class Student:
    pass
stu: Student = Student()

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"niyiwei": 666}
my_str: str = "niyiwei"

my_list: list[int] = [1, 2, 3]
my_tuple: tuple[str, int, bool] = ("n", 2, True)
my_set: set[int] = {1, 2, 3}
my_dict: dict[str, int] = {"niyiwei": 666}
# 元组详细注解需将每一个元素都标记出来
# 字典详细注解第一个是key，第二个是value

var_5 = random.randint(1, 5) #type: int
var_6 = (json.loads('{"name": "zhang"}')) #type: dict[str, str]
def func():
    return 10
var_7 = func() #type: int
# 限制性
# 他就是个备注不会影响
var_8: int = "jsajf"