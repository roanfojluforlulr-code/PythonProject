import random
num = random.randint(1,10)
guess_num = int(input("请在1-10中间猜测一个数字："))

if guess_num == num:
    print("一次正确")
else:
    if(guess_num > num):
        print("大了")
        guess_num = int(input("再猜一次"))
        if(guess_num > num):
            print("大了")
            guess_num = int(input("最后一次："))
            if(guess_num > num):
                print("大了")
            elif(guess_num == num):
                print("最后一次正确")
            else:
                print("小了")
        elif(guess_num == num):
            print("第二次正确")
        else:
            print("小了")
            guess_num = int(input("最后一次"))
            if(guess_num > num):
                print("大了")
            elif(guess_num == num):
                print("最后一次正确")
            else:
                print("小了")

    else:
        print("小了")
        guess_num = int(input("再猜一次："))
        if(guess_num > num):
            print("大了")
            guess_num = int(input("最后一次："))
            if(guess_num > num):
                print("大了")
            elif(guess_num == num):
                print("最后一次正确")
            else:
                print("小了")
        elif(guess_num == num):
            print("第二次正确")
        else:
            print("小了")
            guess_num = int(input("最后一次"))
            if(guess_num > num):
                print("大了")
            elif(guess_num == num):
                print("最后一次正确")
            else:
                print("小了")



