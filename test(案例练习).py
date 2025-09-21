f_1 = open("C:/Pycharm/bill.txt", 'r', encoding="UTF-8")
f_2 = open("C:/Pycharm/bill.txt.bak", 'w', encoding="UTF-8")
for line in f_1:
    #line = line.strip()
    #if line.split(",")[-1] == "测试":
    if line.count("测试") == True:
        continue
    f_2.write(line)
    #f_2.write("\n")
f_1.close()
f_2.close()
