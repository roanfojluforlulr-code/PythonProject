money = 0
name = None

name = input("请输入你的姓名：")
# 查询函数
def query(show_header):
    if show_header:
         print("---查询余额---")
    print(f"您好{name}，你的余额剩余{money}元")
# 存款函数
def saving(num):
    global money
    money += num
    print("---存款---")
    print(f"您好{name}，您存款{num}元成功")
    query(None)
# 取款函数
def get_money(num):
    global money
    money -= num
    print("---取款---")
    print(f"您好{name}，您取款{num}元成功")
    query(False)

# 主菜单函数
def main():
    print("---主菜单---")
    print(f" 您好{name},欢迎来到ATM机。请选择你的操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return int(input("请输入你的选择："))
# 开始
while True:
    keyboard_input = main()
    if keyboard_input == 1:
        query(True)
        continue
    elif keyboard_input == 2:
        num = int(input("请输入您要存款的金额:"))
        saving(num)
        continue
    elif keyboard_input == 3:
        num = int(input("请输入您要取款的金额："))
        get_money(num)
        continue
    else:
        print("程序退出")
        break
