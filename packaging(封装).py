# 私有成员变量及方法都以__开头
class Phone:
    IMEI = None # 序列号
    producer = None # 厂商
    __current_voltage = 0 # 当前电压(私有成员变量)

    # 私有成员方法
    def __keep_single_core(self):
        print("让CPU以单核形式运行来省电")

    ## 私有成员无法被类对象使用， 但可以被其他成员使用
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            print("5g通话已开启")
        else:
            self.__keep_single_core()
            print("电量不足,无法使用5g通话,已切换为单核模式进行省电")

# 私有方法无法直接被类对象使用
"""
phone = Phone()
phone.__keep_single_core()
"""

# 私有变量无法赋值也无法取值
"""
phone = Phone()
phone.__current_voltage = 33
print(phone.__current_voltage)
"""

phone = Phone()
phone.call_by_5g()

print()

# 练习
class Phone:
    __is_5g_enable = True
    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g关闭,使用4g网络")
    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")

phone = Phone()
phone.call_by_5g()