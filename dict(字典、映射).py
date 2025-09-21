# 字典 {key: value}
# 每一份数据是KeyValue键值对
# key不可以重复， value可以重复
# 不可以使用下标索引，通过key检索value, 可以修改， 不能用while循环
# key不能为字典，其他都行，value都行
my_dict_1 = {"周杰伦": 9, "林俊杰": 99, "蔡徐坤": 999}
my_dict_2 = {}
my_dict_3 = dict()
def print_func(dn):
    print(type(dn), dn)

print_func(my_dict_1)
print_func(my_dict_2)
print_func(my_dict_3)

print()

# 定义重复key的字典
my_dict_4 = {"H": 9, "H": 8, "Y": 7}
print(my_dict_4)
# 基于key获得value
my_dict_5 = {"周杰伦": 99, "蔡徐坤": 99, "我": 100}
score = my_dict_5["我"]
print(score)

# 定义嵌套字典
stu_score_dict = {
    "周杰伦": {
        "语文": 88,
        "数学": 88,
        "英语": 99
    }, "蔡徐坤": {
        "语文": 0,
        "数学": 99,
        "英语": 99
    }, "林俊杰": {
        "语文": 99,
        "数学": 100,
        "英语": 100
    }
}
print(stu_score_dict)

# 从字典嵌套获取数据
score = stu_score_dict["林俊杰"]["数学"]
print(score)

# 新增元素
stu_score = {
    "王力宏": 88,
    "蔡徐坤": 80,
    "林俊杰": 99
}
stu_score['你'] = 100
print(stu_score)
# 更新元素
stu_score = {
    '我': 55,
    '你' : 100,
    '王力宏': 99
}
stu_score["我"] = 88 ,
print(stu_score )
# 删除元素
value = stu_score.pop("王力宏")
print(value)
print(stu_score)
# 获取全部的key
keys = stu_score.keys()
print(keys)
# 遍历字典
# 方式一
for key in keys:
    print(key)
    print(stu_score[key])
# 方式二
for key in stu_score:
    print(key)
    print(stu_score[key])
# 统计字典内元素数量
print(len(stu_score))
# 清空
stu_score.clear()
print(stu_score)

print()

# 练习
Factory_employee_information = {
    "王力宏": {
        "部门": '科技部',
        '工资': 3000,
        '级别': 1
    },
    '我': {
        '部门': '市场部',
        '工资': 5000,
        '级别': 2
    },
    '林俊杰': {
        '部门': '市场部',
        '工资': 5000,
        '级别': 3
    },
    "张学友": {
        '部门': '科技部',
        '工资': 4000,
        '级别': 1
    },
    "刘德华": {
        '部门': '市场部',
        '工资': 6000,
        '级别': 2
    }
}
print(Factory_employee_information)

for key in Factory_employee_information:
    if Factory_employee_information[key]['级别'] == 1:
        Factory_employee_information[key]["工资"] += 1000
        Factory_employee_information[key]['级别'] += 1
print(Factory_employee_information)