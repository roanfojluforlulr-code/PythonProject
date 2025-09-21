# 构造方法
# 在创建类对象时会自动执行， 将传入的参数自动传递给__init__方法使用
class Student:
    # 可以不写
    name = None
    age = None
    tel = None
    # 以上
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("对象创作完成")
stu = Student("大帅哥", 31, "13123123213123")
print(stu.name)

print()

# 练习
class Student:
    name = None
    age = None
    address = None
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
my_dict = dict()
for i in range(1,11):
    print(f"当前录入第{i}位学生信息， 总共需录入10位学生信息")
    stu = Student(name = input("请输入学生姓名:"), age = int(input("请输入学生年龄:")), address=input("请输入学生地址:"))
    my_dict[f"第{i}个学生："] = {"姓名":stu.name, "年龄":stu.age, "地址":stu.address}
    print(f"学生{i}信息录入完成， 信息为【学生姓名：{stu.name}, 年龄：{stu.age}, 地址：{stu.address}】")
print(my_dict)