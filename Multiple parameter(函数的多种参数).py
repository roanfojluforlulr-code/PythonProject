# 参数种类分位置参数、关键字参数、缺省参数、不定长参数
def user_info(name, age, gender):
    print(f"您的名字是{name}， 年龄是{age}， 性别是{gender}")

# 位置参数：通过参数位置来传递参数 顺序必须一致
user_info('Mark', 16, '男')

# 关键字参数：通过：“键对值”来传递参数
# 更清晰、易使用，无参数顺序要求
# 以下三种都可以
user_info(name='Mark', age=16, gender='男')
user_info(age=16, gender='男', name='Mark')
user_info('Mark', age=16, gender='男') # 使用位置参数要放关键字参数的前面，关键字参数无顺序

# 缺省参数（默认参数）
# 在定义和调用时，位置参数必须在其之前
# 没传参时，使用默认参数值
# 设置默认值统一在最后有
def user_info(name, age, gender='男'):
    print(f"您的名字是{name}， 年龄是{age}， 性别是{gender}")
user_info('Tom', 20)
user_info("Rose", 18, '女')

# 不定长参数（可变参数），分两类：位置传递和关键字传递
# 用于不确定调用时会传递多少个参数

# 位置传递
# 所有参数被args变量收集，并将传进参数的位置合并为一个元组，args是元组类型
def user_info(*args): # *为无限的意思
    print(args)
user_info('Tom')
user_info('Tom', 18)

# 关键字传递
# 参数是“键=值形式，所有“键=值”的都会被kwargs（key-word），组成字典
def user_info(**kwargs):
    print(kwargs)
user_info(name='Tom', age=18, id=110)