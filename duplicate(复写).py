# 复写会更改
class Phone:
    IMEI = None
    producer = "IT"

    def call_by_5g(self):
        print("父类5g通话")
class MyPhone(Phone):
    producer = "帅哥"
    def call_by_5g(self):
        # 方式一调用父类成员
        """
        print(f"父类的品牌{Phone.producer}")
        Phone.call_by_5g(self)
        """
        # 方式二调用父类成员
        print(f"父类的品牌是{super().producer}")
        super().call_by_5g()
        print("子类的5sg通话")
        print("谁人不识我？")
phone = MyPhone()
phone.call_by_5g()
print(phone.producer)