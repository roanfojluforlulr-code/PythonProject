class Student:
    name = None
    gender = None
    nationality = None # 国籍
    native_place = None # 籍贯
    age = None
    # 传参时不管self
    def say_hi(self):
        print(f"大家好我是{self.name}")
    def sat_hi2(self, msg):
        print(f"大家好我是{self.name},{msg}")

# 可以创建多个对象
stu_1 = Student()
stu_2 = Student()

stu_1.name = "Mark"
stu_1.gender = "男"
print(stu_1.name, stu_1.gender)
stu_1.say_hi()

stu_2.name = "帅哥"
stu_2.sat_hi2("你以为")
print(stu_2.name)