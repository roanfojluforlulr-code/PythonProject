str1 = "itheima"
str2 = "itcast"
str3 = "python"

count = 0

for i in str1:
    count += 1
print(f"str1的长度为{count}")

def my_len(data):
    count = 0
    for i in data:
        count += 1
    print(f"字符串{data}的长度为{count}")

my_len(str1)
my_len(str2)
my_len(str3)


def say_hi():
    print("Hi")

say_hi()

def say_hello():
    print("Hello")

say_hello()
