# open(name,mode,encoding)函数可以打开或创建一个新文件.encoding使用UTF-8

# mode的三种基础的访问模式：
# r:只读
# w:写入（如果文件已存在，打开并清除原有内容；不存在则创建新文件）
# a:追加（如果文件已存在，追加新内容；不存在则创建新文件并写入）

# 示例:
# f = open("python.txt", 'r', encoding="UFT-8")
# 注意: encoding 的顺序不是第三位，所以不能用位置参数，用关键字参数指定
# 打开文件 关闭文件: f.close
f = open("C:/Pycharm/练习文本001.txt", "r", encoding="UTF-8")
print(type(f))
# 读操作的相关方法
# 文件对象.read(num) num表示从文件中读取的数据的长度（以字节为单位），如果没有num，表示全读
print(f.read(10))
# 读全部
print(f.read())

print()

f.close()
f = open("C:/Pycharm/练习文本001.txt", 'r', encoding="UTF-8")

# readLines()按照行的方式将文件中的内容进行一次性读取，每一行的数据作为一个元素，存放在列表中
lines = f.readlines()
print(type(lines), lines)

f.close()
f = open("C:/Pycharm/练习文本001.txt", "r", encoding="UTF-8")

# readline() 表示一次只读一行
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()

print(line1)
print(line2)
print(line3)

f.close()
f = open("C:/Pycharm/练习文本001.txt", "r", encoding="UTF-8")

# for循环读取文件每一行
for line in f:
    print(f"每一行的内容是：{line}")

f.close()
print()
f = open("C:/Pycharm/练习文本001.txt", "r", encoding="UTF-8")

# withOpen可以在操作完成后自动关闭文件
with open("C:/Pycharm/练习文本001.txt", "r", encoding="UTF-8") as f:
    for line in f:
        print(f"每一户:{line}")

# 练习

# 方法一
with open("C:/Pycharm/练习文本002.txt", 'r') as f:
    print(f.read().count("itheima"))

f = open("C:/Pycharm/练习文本002.txt", "r", encoding="UTF-8")

# 方法二
count = 0
for line in f:
    line  = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count += 1
print(count)
f.close()