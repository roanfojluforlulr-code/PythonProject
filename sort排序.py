# 依据列表第二个元素进行排序
my_list = [["a", 33], ["b", 55], ["c", 11]]
# 定义排序方法
# 方式一
def choose_sort_key(element):
    return element[1]
my_list.sort(key=choose_sort_key, reverse=True)
print(my_list)
# 方式二
my_list = [["a", 33], ["b", 55], ["c", 11]]
my_list.sort(key=lambda element: element[1], reverse=True)
print(my_list)