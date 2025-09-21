# 跟变量的一样， 都是提示性的
# 形参: 类型
#  ->返回值类型
def add(x: int, y: int):
    return x + y
print(add(2,5))

def func(data: list) -> list:
    return data
print(func(1))