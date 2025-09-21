import random
num = random.randint(1, 100)
flag = True
count = 0

while flag:
    num_guess = int(input("请在1-100中输入你所猜测的数据："))
    count += 1
    if num_guess == num:
        print("猜中了")
        flag = False
    else:
        if num_guess > num:
            print("大了")
        else:
            print("小了")

print(f"你总共猜测了{count}次")