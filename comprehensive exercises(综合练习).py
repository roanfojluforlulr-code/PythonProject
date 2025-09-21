import My_utils.str_util
from My_utils import file_util
print(My_utils.str_util.str_reverse("987654321"))
print(My_utils.str_util.substr("Mark is handsome", 5, 8))
file_util.print_file_info("C:/Pycharm/test_append.txt")
file_util.append_to_file("C:/Pycharm/test_append.txt", "我说过你是个帅哥")