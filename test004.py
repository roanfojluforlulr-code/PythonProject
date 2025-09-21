11#根据入职时间，年龄和级别判断是否符合领取礼物的条件

age = int(input("Tell me your age:"))
year = int(input("The year you stay in company is:"))
level = int(input("Your level is:"))

if age >= 18:
    print("你为成年人")
    if age <= 30:
        print("你的年龄达标了")
        if year >= 2:
            print("你可以领取礼物")
        elif level >= 3:
            print("年龄和级别达标，可以领取礼物")
        else:
            print("入职时间和级别不达标")
    else:
        print("你的年龄太大")
else:
    print("你为未成年人")