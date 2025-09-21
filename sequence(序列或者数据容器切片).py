# 序列[头：尾：步长]：有（列表、元组、字符串），留空表示从头开始到尾结束，步长默认是1

# 列表:
my_list = [0, 1, 2, 3, 4, 5, 6]
result_1 = my_list[1:4]
print(result_1)
# 元组:
my_tuple = (0, 1, 2, 3, 4, 5, 6)
result_2 = my_tuple[:]
print(result_2)
# 字符串:
my_str = "0 1 2 3 4 5 6"
result_3 = my_str[::2]
print(result_3)
result_4 = my_str[::-1]
print(result_4)

# 练习
# 普通用法
my_str = "万过月薪，员序程马黑来，nohtyp学"
result1 = my_str[9:4:-1] # 或者[::-1][9:14]、[5:10][::-1]。
print(result1)
# 重要用法
result2 = my_str.split("，")[1] .replace("来", "")[::-1]
print(result2)
