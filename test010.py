for i in range(1,10):
    print("asdfasf", end=' ')
    continue
    print("a")
print()

for i in range(1,6):
    print("语句一",end=' ')
    for j in range(1,6):
        print("语句二", end=' ')
        continue
        print("语句三")
    print("语句四 ")

for i in range(1, 101):
    print("语句一")
    break
    print("语句二")

print("语句四")

for i in range(1, 6):
    print("语句一", end=' ')
    for j in range(1, 6):
        print("语句二", end=' ')
        break
        print("语句三")
    print("语句四")
