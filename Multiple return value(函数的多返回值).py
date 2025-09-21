def test_return():
    return 1, "Hello", True
    # return 2 不会被执行
x, y, z,  = test_return()
print(x)
print(y)
print(z)
