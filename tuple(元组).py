# 元组不可修改
# 在元组中只能用index(), count(), len(元组)这三种方法
t1 = (1, "Hello", True)
t2 = ()
t3 = tuple()
def print_func(tn):
    print(type(tn), tn)

print_func(t1)
print_func(t2)
print_func(t3)

print()

# 定义元组单个元素需要加逗号，否则为字符串类型
t4 = ('hello')
print_func(t4)
t4 = ('hello', )
print_func(t4)

t5 = ((1, 2, 3), (4, 5, 6))
print_func(t5 )
# 以索引输出：
print(t5[1][2])
# == t5[-1][-1]

print()

t6 = (1, 2, 3)
# 查找
print(t6.index(2))

# 统计出现次数
print(t6.count(1))

# 统计元素个数
print(len(t6))

print()

t7 = (6456, 45634, "jjjj", True)

# 循环遍历元组
# while:
index = 0
while index < len(t7):
    print(t7[index], end=' ')
    index += 1

print()

# for:
for index in t7:
    print(index, end=' ')

print()
print()

# 元组不可修改，但元组内列表可以修改
t8 = (1, 2, ['you', 'me'])
t8[2][1] = "you"
print(t8)

print()

# 练习
person = ('蔡徐坤', 18, ['唱', '跳', "rap", '篮球'])
print(person.index(18))
print(person[0])
del person[2][2]
person[2].append('coding')
print(person)