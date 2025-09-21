# 列表：!!!<列表从零开始>

my_list = ["Happy", "New", "Year", 666, True]
print(my_list)
print(type(my_list))

print()

# 嵌套列表
my_list = [[1, 2, 3], [4, 5, 6]]
print(my_list)
print(type(my_list))
print(my_list[-1][-1])

print()

# 常用操作

# 获取下标
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)
# 更改
my_list[0] = 100
print(my_list)
# 插入
my_list.insert(1, 444 )
print(my_list)
# 追加(一个）
my_list.append("end")
print(my_list)
# 追加（一批）
my_list2 = ([9999999999, 9])
my_list.extend(my_list2)
print(my_list)
# 删除1
del my_list[6]
print(my_list)
# 删除2(取出[不放回])
element = my_list.pop(5)
print(my_list, element)
# 删除3（指定元素[删除从前往后第一个元素且只能删一个]）
my_list.remove(3)
print(my_list)
# 清除列表
my_list.clear()
print(my_list)
# 统计列表内指定元素的数量
my_list = [1, 1, 1, 2, 3]
num = my_list.count(1)
print(num)
# 统计总共有多少个元素
print(len(my_list))

print()

# 列表常用练习
list = [21, 25, 21, 23, 22, 20]
list.append(31)
list.extend([29, 33, 30])
element_1 = list.pop(0)
element_2 = list.pop(-1)
index = list.index(31)
print(list)
print(element_1, element_2, index)

print()

# 列表遍历
# 一: while 循环遍历
def list_while_func():

    my_list = [6, 6.6, "hh"]

    index = 0
    while index < len(my_list):
        print(my_list[index], end=' ')
        index += 1

list_while_func()

print()

# 二： for 循环遍历
def list_for_func():
    my_list = [0, 1, 2, 3]
    for index in my_list:
        print(index, end=' ')

list_for_func()

print()
print()

# 循环遍历练习
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Evennum = []

# while:
index = 0

while index < len(list):

    if list[index] % 2 == 0:
        Evennum.append(list[index])
    index += 1

print(Evennum)

list.clear()

# for:
for index in list:
    if index % 2 == 0:
        Evennum.append(index)

print(Evennum)
