# 匿名函数只能临时使用一次，所以用于使用一次的场景
# 跟在函数作为参数传递里的函数用法相同。只是lambda定义的函数是匿名的，无法二次使用
# 可以不用写return（它是默认的）
# 语法：lambda 传入参数: 函数体(一行代码)。只能写一行，无法写多行代码
def test_func(computer):
    result = computer(1, 2)
    print(result)
test_func(lambda x, y: x + y)
# 可以优化代码，非常方便
