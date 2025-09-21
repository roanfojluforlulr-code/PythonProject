def test(a, b):
    print(a + b)
# 函数内部会执行，调用module时不会用
if __name__ == '__main__':
    test(2, 3)