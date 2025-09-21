def print_file_info(file_name):
    """
    将给定内容输出到控制台中
    :param file_name: 即将被读取的路径
    :return: None
    """
    f = None
    try:
        f = open(file_name, 'r', encoding="UTF-8")
        content = f.read()
        print(content)
    except Exception as e:
        print(e)
    finally:
        if f:
            f.close()
def append_to_file(file_name, data):
    """
    将指定的数据追加到指定的文件中
    :param file_name: 文件路径
    :param data: 数据
    :return: None
    """
    f = open(file_name, 'a', encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()

if __name__ == '__main__':
    print_file_info("C:/Pycharm/bill.txt")
    append_to_file("C:/Pycharm/test_append.txt", "Mark")
