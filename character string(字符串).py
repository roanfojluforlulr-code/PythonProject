# 字符串跟元组一样不可修改且只可以存储字符串
# 字符串大小比较看ASCII码表值
my_str = "Mark and friend"
print(my_str[0])
print(my_str[-1])
print()

# index方法
value_1 = my_str.index("and")
print(value_1)
# 字符串的替换
value_2 = my_str.replace("friend", "friends")
print(value_2)
# 字符串的分割(切分)
value_3 = value_2.split(" ")
print(value_3)
print(type(value_3))
# 字符串的规整操作(01.空格)
my_str = " Hello Everyone, good afternoon! "
print(my_str.strip())
# 字符串的规整操作（02.字符串）
my_str = "123Hello Everyone!321"
print(my_str.strip("123"))
# 统计某字符串出现次数
print(my_str.count("e"))
# 统计字符串的长度
print(len(my_str))
"""
循环遍历跟列表、元组一样（while、for）
"""

print()

# 练习
string = "itheima itcast boxuegu"
print(string.count("it"))
print(string.replace(" ", "|"))
print(string.split("|"))