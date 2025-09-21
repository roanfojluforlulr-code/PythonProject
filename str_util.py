def str_reverse(s):
    '''
    反转字符串
    :param s:
    :return:字符串
    '''
    return s[::-1]
    # print(s[::-1][0:len(s)])

def substr(s, x, y):
    """
    对给定下标进行字符串切片
    :param s: 字符串
    :param x: 开始下标
    :param y: 结束下标
    :return: 切完的字符串
    """
    return s[x:y]

if __name__ == '__main__':
    print(str_reverse("10002"))
    print(substr("12345", 1, 3))