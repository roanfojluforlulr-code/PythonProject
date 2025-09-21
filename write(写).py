"""
打开文件： f = open('python.txt', 'w')
文件写入： f.write('hello world')
内容刷新： f.flush()
"""

# 直接调用write,内容并未写入文件，而会积攒在缓冲区中
# 当调用flush的时候，内容会真正地写入文件
# 避免频繁的操作硬盘，导致效率下降（攒一起，一次性写入磁盘）
f = open('C:/Pycharm/练习文本003.txt', 'w')
f.write("Hello")
f.flush()
f.close() # close内置了flush功能
# 当文件存在时，覆盖内容
f = open('C:/Pycharm/练习文本003.txt', 'w')
f.write("这才是我")
f.close()