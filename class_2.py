class clock:
    id = None #序列号
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)

clock1 = clock()
clock2 = clock()

clock1.id = "00302"
clock1.price = 9.9
print(f"闹钟ID：{clock1.id}, 价格: {clock1.price}")
clock1.ring()

clock2.id = "00303"
clock2.price = 19.9
print(f"闹钟ID：{clock2.id}, 价格: {clock2.price}")
clock2.ring()