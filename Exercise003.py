print("Check if you are an adult")

age = int(input("Tell me your age:"))

if age >= 18:
    print("You are an adult")
else:
    print("you are a kid")

print("Have a nice day")

a = 5

if  int(input("请猜一个数字：")) == a:
    print("回答正确")
elif int(input("再猜： ")) == a:
    print("回答正确")
elif int(input("最后一次机会：")) ==a:
    print("回答正确")
else:
    print("回答错误")