# 追加操作与写的操作一样不过要将'w'模式变成'a'模式
# 不存在将创建文件； 存在则在最后追加写入文件
f = open('C:/Pycharm/练习文本004.txt', 'a')
f.write("开始")
f.flush()
f.close()

f = open('C:/Pycharm/练习文本004.txt', 'a')
f.write("\n追加")
f.close()