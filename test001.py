# 注释

print(type("shfdjas"))

string_type = type("sfj;klas")
print(string_type)

name = "sfsa"
string_name = type(name)
print(string_name)


name = str(11)
print(type(name), name)

age = int("11")
print(type(age),age)

name = "\"你以为\""
print(name)

name = "你"
print("我套你猴子:"+ name+",你以为")  # 只能接字符串
print("wwww "+ name + " jfjj")

name = "你"
jjj = 666
iii = 888
aaa = 6.66
your_name = "jjj%s,ssss%s" % (name,name)
print(your_name)
your_name = "哈哈哈%s，你以为%s，我以为%s, 他以为%.2f" % (name, jjj, iii, aaa)
print(your_name) # 可以接不同类型：%d整数 %s字符串 %宽度（数字）.小数点精度 f浮点数


name = 18
name_1 = 18.8

print(f"你以为我是{name}，其实我是{name_1} ")

print("1 * 100的结果是： %d" % (1 * 100) )
print(f"1*100的结果是 {1*100}") # f为固定格式
print("字符串在python中为： %s" % type("字符串"))

complex = 4 + 3j







