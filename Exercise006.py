# 输出不换行
print("Hello", end='')
print("world", end='')
print()
# 制表符
print("Hello\tworld")
print("Itheima\tbest")

# 九九乘法表

i = 1
while i <= 9:
    j=1
    while j <= i:
        print(f"{j} * {i} = {j*i}\t", end='' )
        j+=1
    print(" ")
    i += 1
