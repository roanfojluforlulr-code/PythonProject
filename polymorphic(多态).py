# 常用于继承关系
# 以父类做声明
# 以子类做实际工作
# 用以获得同意行为，不同状态
# 如代码所示，用父类确定有哪些方法,用子类实现。这种写法即为抽象类
# 方法体是空实现的(pass) 成为抽象方法
# 例一:
class Animal:
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        print("汪汪汪")
class Cat(Animal):
    def speak(self):
        print("喵喵喵")

dog = Dog()
cat = Cat()

def make_noise(animal: Animal):
    animal.speak()

make_noise(dog)
make_noise(cat)
# 例二:
class AC():
    def cool_wind(self):
        """制冷"""
        pass
    def hot_wind(self):
        """制热"""
        pass
    def swing_l_r(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调核心制冷科技")
    def hot_wind(self):
        print("美的空调电热丝加热")
    def swing_l_r(self):
        print("美的空调无风感左右摆风")

class GREE_AC(AC):
    def cool_wind(self):
        print("格力空调变频省电制冷")
    def hot_wind(self):
        print("格力空调电热丝加热")
    def swing_l_r(self):
        print("格力空调静音左右摆风")

def make_coll(ac: AC):
    ac.cool_wind()

midea_ac = Midea_AC()
gree_ac = GREE_AC()
make_coll(midea_ac)
make_coll(gree_ac)