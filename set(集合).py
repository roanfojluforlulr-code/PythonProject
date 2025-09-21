# 集合不支持重复，内容无序。
# 集合不支持下标索引，所以集合不是序列, 不支持while循环遍历
# 集合跟列表一样可修改

my_set = {"Hello", 58, 58, 58, 66, 66}
my_empty_set = set()
print(type(my_set), my_set)
print(type(my_empty_set), my_empty_set)
# 添加新元素
my_set.add("python")
print(my_set)
# 移除元素
my_set.remove("Hello")
print(my_set)
# 随机取出一个元素
element = my_set.pop()
print(my_set)
print(element)
# 统计集合元素数量
print(len(my_set))
# 清空集合
my_set.clear()
print(my_set)

print()

# 新用法:

# 取两个集合的差集
# 语法: 集合1.difference(集合2), 功能: 取出集合1和集合2的差集(集合1有的而集合2没有的)
# 取完，原集不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.difference(set2)
print(set1)
print(set2)
print(set3)

print()

# 消除两个集合的差集
# 语法: 集合1.difference_update(集合2)
# 功能: 在集合1内，删除和集合2相同的元素
# 集合1被修改，集合2不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1)
print(set2)

print()

# 2个集合合并
# 语法: 集合1.union(集合2)
# 功能: 将集合1和2组合成新集合
# 原集合不变
set1 = {1, 2, 3}
set2 = {1, 5, 6}
set3 = set1.union(set2)
print(set1)
print(set2)
print(set3)

print()

# for循环遍历
set = {1, 2, 3, 4}
for element in set:
    print(element, end= '  ')

print()
