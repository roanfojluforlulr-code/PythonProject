class Phone:
    IMEI = None
    prooducer = "我先"

    def call_by_5g(self):
        print("5g通话")
class NFCReader:
    nfc_type = "第五代"
    producer = "Mark"

    def read_card(self):
        print("读取NFC卡")

    def write_card(self):
        print("写入NFC卡")
class Remotecontrol:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启")
class MyPhone(Phone, NFCReader, Remotecontrol):# 如果有相同的成员，谁先来的(从左往右)，谁先继承谁优先
    pass# pass表示(空),用来补充语法
phone = MyPhone()
phone.call_by_5g()
phone.read_card()
phone.write_card()
phone.control()
print(phone.prooducer)
