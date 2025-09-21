num = 180

def test_A():
    print(num)
def test_B():
    num = 900
    print(num)
def test_C():
    # global 声明全局变量
    global num
    num = 910
    print(num)

test_A()
test_B()
test_C()
print(num)