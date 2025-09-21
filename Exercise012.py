def check(x):
    if x <= 37.5:
        print(f"您的体温正常，为{x}度")
    else:
        print(f"您的体温不正常，为{x}度")

x = float(input("请配合输入你的体温："))
check(x)