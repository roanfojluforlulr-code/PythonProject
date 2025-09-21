def say_hi():
    print("hi")

result = say_hi()

print(result)
print(type(result))

def say_hello():
    print("Hello")
    return None

result = say_hello()

print(result )

def check_age(age):
    if age >= 18:
        return "Success"
    else:
        return None

result = check_age(16)
if not result:
    print("未成年禁止进入")
else:
    print("请进")

name = None
print(name)