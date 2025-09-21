# 这是一种计算逻辑的传递，而不是数据的传递
# 任何逻辑都可以自定义作为函数传入
def test_func(computer):
    result = computer(1, 2)
    print(result)
def computer(x, y):
    return x + y
test_func(computer)