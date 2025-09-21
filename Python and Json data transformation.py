import json
# 准备符合json格式的python数据
data = [{"name":"admin", "age":18}, {"name":"张三", "age":20}]

# python数据转json数据
data = json.dumps(data, ensure_ascii=False)# 逗号后解决中文问题(编码问题)
print(type(data),data)
d = {"name":"帅哥", "age":18}
d = json.dumps(d, ensure_ascii=False)
print(type(d), d)

print()

# json数据转python数据
data = json.loads(data)
s = '[{"name":"admin", "age":18}, {"name":"root", "age":16},{"name":"张三", "age":20}]'
s = json.loads(s)
print(type(s), s)
s = '{"name":"admin", "age":18}'
s = json.loads(s)
print(type(s), s)
