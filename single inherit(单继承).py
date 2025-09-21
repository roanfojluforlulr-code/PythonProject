# 语法
# class 类名(父类名):
# 内容体
class Phone:
    IMEI = None
    prooducer = "Mark"
    def call_by_4g(self):
        print("4g通话")

class phone2024(Phone):
    face_id = True
    def call_by_5g(self):
        print("2024最新5g通话")

phone = phone2024()
print(phone.prooducer)
phone.call_by_4g()
phone.call_by_5g()