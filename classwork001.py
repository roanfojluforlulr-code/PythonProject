#1
print("第一个程序")
print()

MyAge = 3 # integer
MyName = "Mark" # string
MyGender = True # bool
MyHeight = 190.98 # float
print(MyAge, MyName, MyGender, MyHeight)

#2
print()
print("第二个程序")
print()

number = int("123")
value = str(123)
print(number, value, type(number), type(value))

#3
print()
print("第三个程序")
print()

print(bool(0), bool((""))) #others are True

#4
print()
print("第四个程序")
print()

length = int(input("Please enter the length: "))
width = int(input("Please enter the width: "))
area = length * width
print(area)

#5
print()
print("第五个程序")
print()

print("My","Name",sep="&")

#6
print()
print("第六个程序")
print()

number_1 = int(input("Please enter the first number: "))
number_2 = int(input("Please enter the second number: "))
print(number_1 + number_2)
print(number_1 * number_2)

#7
print()
print("第七个程序")
print()

print(33 // 7)
print(20-10)
print(100/5)
print(33%7)

#8
print()
print("第八个程序")
print()

number_3 = int(input("Please enter a number: "))
if number_3 == 0:
    print("Positive")
else:
    print("Negative")

#9
print()
print("第九个程序")
print()

num = 10
guess_number = int(input(("Please enter a number: ")))
if guess_number == num:
    print("That's right")
else:
    print("Incorrect")

#10
print()
print("第十个程序")
print()

number_4 = int(input("Please enter the first number: "))
number_5 = int(input("Please enter the second number: "))

if number_4 <= number_5:
    print(number_4)
else:
    print(number_5)

#11
print()
print("第十一个程序")
print()

user_input = str(input("Please enter a string: "))
if user_input =="A":
    print(user_input)
elif user_input == "B":
    print(user_input)
elif user_input == "C":
    print(user_input)
else:
    print("Invalid input")

#12
print()
print("第十二个程序")
print()

number_6 = int(input("Please enter the first number: "))
print("Please choose one symbol: + _ * /: ")
symbol = input()
number_7 = int(input("Please enter the second number: "))

if symbol =="+":
    print(number_6 + number_7)
elif symbol == "-":
    print(number_6 - number_7)
elif symbol == "*":
    print(number_6 * number_7)
elif symbol == "/":
    print(number_6 / number_7)
else:
    print("Incorrect input")
#13
print()
print("第十三个程序")
print()

for i in range(1,10):
    for j in range(1,i+1):
        print(i,"*",j,"=",i * j,"\t",end="")
    print()

#14
print()
print("第十四个程序")
print()

total = 0
for num in range(1,101):
    total += num
print(total)

#15
print()
print("第十五个程序")
print()

for i in range(1, 101):
    if i % 3 ==0:
        print(i," ", end="")

#16
print()
print("第十六个程序")
print()

for i in range(1,51):
    if i % 5 == 0:
        if i % 2 == 0:
            break
        print(i)

#17
print()
print("第十七个程序")
print()

total = 1
sum = int(input("Please enter a number: "))
for i in range(1, sum+1):
    total *= i
print(total)

#18
print()
print("第十八个程序")
print()

sum = 0
for i in range(1, 101):
    if i % 10 != 3:
        sum += i
print(sum)