# 异常的案例
# f = open("C:/abc.txt", 'r')

# 异常处理(捕获异常)
# 提前准备，当有真异常会有后续手段
"""
基本语法：(也可以认为是捕获所有异常，因为未规定类型)
try:
    可能发生错误的代码
except[异常 as 别名]:
    如果出现异常，执行的代码
"""
try:
    f = open("C:/Pycharm/测试001.txt", 'r')
except:
    print("开始执行")
    f = open("C:/Pycharm/测试001.txt", 'w')
f.close()

# 捕获指定的异常
try:
    print(name)
except NameError as a:
    print("变量未定义异常")
    print(a)

print()

# 捕获多个异常
try:
    # print(name)
    print(1/0)
except (NameError, ZeroDivisionError) as e:
    print("未定义或除以0错误")
    print(e)

print()

# *捕获所有异常（跟基本语法作用一样）
try:
    # print(1/0)
    print(1)
except Exception as e:
    print("出现异常")
else:
    print("无异常 ")

print()

# 异常的finally(无论有无异常的执行)
try:
    f = open("C:/Pycharm/测试002.txt", 'r')
except Exception as e:
    f = open("C:/Pycharm/测试002.txt", 'w')
else:
    print("无异常")
finally:
    f.close()

# 异常具有传递性
# 当func01发生异常时，并且当没有捕获到这个异常时;
# 会传递到func02中，当func02也没有捕获到这个异常时;
# main()函数会捕获这个异常
# 当所有函数都没有捕获到异常时，报错
def func01():
    print("01开始")
    1/0
    print("01结束")
def func02():
    print("02开始")
    func01()
    print("02结束")
def main():
    try:
        func02()
    except Exception as e:
        print(e)
main()