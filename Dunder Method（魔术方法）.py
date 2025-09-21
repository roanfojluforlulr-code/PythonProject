# 构造方法
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
student = Student("Mark", 17)
print(student)
print(str(student))

print()
# 魔术方法
# 字符串方法
class Student_1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    #def __str__(self):
    def __str__(self):
        return f"Student_1类对象，name={self.name}, age={self.age}"

student = Student_1("Mark", 17)
print(student)
print(str(student))

print()

# 因为直接比较大小，会报错
# 所以指定比较
# 小于/大于符号比较法
class Student_2:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

stu_1 = Student_2("M", 14)
stu_2 = Student_2("K", 15)

print(stu_1 < stu_2)
print(stu_1 > stu_2)

print()

# 小于等于或大于等于比较法
class Student_3:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

    def __le__(self, other):
        return self.age <= other.age

stu_1 = Student_3("M", 6)
stu_2 = Student_3("K", 15)
stu_3 = Student_3("L", 15)

print(stu_1 <= stu_2)
print(stu_1 >= stu_2)
print(stu_2 >= stu_3)

print()

# 运算符比较方法
# 不使用这种方法，会比较内存地址
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __eq__(self, other):
        return self.age == other.age

stu_1 = Student("Mark", 17)
stu_2 = Student("Kevin", 17)

print(stu_1 == stu_2)