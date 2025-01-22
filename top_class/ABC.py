from abc import ABC, abstractmethod
from random import randint


class Post(ABC):
    def __init__(self, title, cantent):
        self.title = title
        self.cantent = cantent

    @abstractmethod
    def create(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class KunUzPost(Post):

    def create(self):
        print(f"kun yangiliklari {self.title} haqida {
              self.cantent} kabi malumotlar berildi")

    def update(self, editing):
        print(f"{self.title} posti {editing} ga o'zgartirildi")

    def delete(self):
        print(f"{self.title} posti o'chirildi")


class DaryoPost(Post):

    def create(self):
        print(f"kun yangiliklari {self.title} haqida {
              self.cantent} kabi malumotlar berildi")

    def update(self, editing):
        print(f"{self.title} posti {editing} ga o'zgartirildi")

    def delete(self):
        print(f"{self.title} posti o'chirildi")


class TerabaytPost(Post):

    def create(self):
        print(f"kun yangiliklari {self.title} haqida {
              self.cantent} kabi malumotlar berildi")

    def update(self, editing):
        print(f"{self.title} posti {editing} ga o'zgartirildi")

    def delete(self):
        print(f"{self.title} posti o'chirildi")


class Transaction(ABC):

    def __init__(self, card: str, phone_num: str, amount: float = 1000):
        self.amount = amount
        self.card = card
        self.phone_num = phone_num

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def end(self):
        pass

    @abstractmethod
    def verify(self):
        pass

    @abstractmethod
    def proceed(self):
        pass

    @abstractmethod
    def cancel(self):
        pass


class AloqaBank(Transaction):

    def start(self):
        return f"{self.card} karta raqamiga o'tkazma boshlandi."

    def end(self):
        return "O'tkazma summasini kiriting. "

    def verify(self):
        if self.amount >= 1000:
            return f"O'tkazma miqdori tasdiqlandi: {self.amount} so'm."
        else:
            return "Eng kam o'tkazma miqdori 1000 so'mdan yuqori bo'lishi kerak."

    def proceed(self):
        cod = randint(1111, 9999)
        print(cod)
        try:
            answer = int(input("SMS orqali yuborilgan kodni kiriting: "))
            if answer == cod:
                return "O'tkazma muvaffaqiyatli yakunlandi."
            else:
                return "Kod xato. Tranzaksiya bekor qilindi."
        except ValueError:
            return "Noto'g'ri formatdagi kod kiritildi. Tranzaksiya bekor qilindi."

    def cancel(self):
        return "Tranzaksiya bekor qilindi."


s = AloqaBank("9860170103486743", "+998976131698", 1000)

print(s.start())
print(s.end())
print(s.verify())
print(s.proceed())
print(s.cancel())


class IpakYoli(Transaction):

    def start(self):
        return f"{self.card} karta raqamiga o'tkazma boshlandi."

    def end(self):
        return "O'tkazma summasini kiriting."

    def verify(self):
        if self.amount >= 1000:
            return f"O'tkazma miqdori tasdiqlandi: {self.amount} so'm."
        else:
            return "Eng kam o'tkazma miqdori 1000 so'mdan yuqori bo'lishi kerak."

    def proceed(self):
        cod = randint(1111, 9999)
        print(cod)
        try:
            answer = int(input("SMS orqali yuborilgan kodni kiriting: "))
            if answer == cod:
                return "O'tkazma muvaffaqiyatli yakunlandi."
            else:
                return "Kod xato. Tranzaksiya bekor qilindi."
        except ValueError:
            return "Noto'g'ri formatdagi kod kiritildi. Tranzaksiya bekor qilindi."

    def cancel(self):
        return "Tranzaksiya bekor qilindi."


s = IpakYoli("9860170103486743", 10000, "+998976131698")


class KDB(Transaction):

    def start(self):
        return f"{self.card} karta raqamiga o'tkazma boshlandi."

    def end(self):
        return "O'tkazma summasini kiriting. "

    def verify(self):
        if self.amount >= 1000:
            return f"O'tkazma miqdori tasdiqlandi: {self.amount} so'm."
        else:
            return "Eng kam o'tkazma miqdori 1000 so'mdan yuqori bo'lishi kerak."

    def proceed(self):
        cod = randint(1111, 9999)
        print(cod)
        try:
            answer = int(input("SMS orqali yuborilgan kodni kiriting: "))
            if answer == cod:
                return "O'tkazma muvaffaqiyatli yakunlandi."
            else:
                return "Kod xato. Tranzaksiya bekor qilindi."
        except ValueError:
            return "Noto'g'ri formatdagi kod kiritildi. Tranzaksiya bekor qilindi."

    def cancel(self):
        return "Tranzaksiya bekor qilindi."


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def peremetr(self):
        pass


class Triangle(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.a + self.b + self.c
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def peremetr(self):
        return self.a + self.b + self.c


d = Triangle(3, 5, 7)

print(d.area())
print(d.peremetr())


class Vehicle(ABC):
    def __init__(self, model):
        self.model = model
        self.condition = False
        self.light_h = False
    @abstractmethod
    def startEngine(self, ):
        pass
    @abstractmethod
    def stopEngine(self):
        pass
    @abstractmethod
    def lightOn(self):
        pass
    @abstractmethod
    def lightOf(self):
        pass

class Car(Vehicle):

    def startEngine(self):
        if not self.condition :
            self.condition = True
            return f"{self.model} yurgazildi"
        else:
            return f"{self.model} allaqachon yurgazilgan."

    def lightOn(self):
        if not self.light_h :
            self.light_h = True
            return f"{self.model} chiroqlari yoqildi"
        else :
            return f"{self.model} chiroqlari yoqiq holatda"
        
    def stopEngine(self):
        if self.condition :
            self.condition = False
            return f"{self.model} O'chirildi"
        else:
            return f"{self.model} o'chiq holatda"
        
    def lightOf(self):
        if self.light_h:
            self.light_h = False
            return f"{self.model} chiroqAri o'chirildi"
        else:
            return f"{self.model} chiroqlari o'chiq holatda"

f = Car('gentra') 
print(f.startEngine())
print(f.stopEngine())
print(f.lightOn()) 
print(f.lightOf())    

class Bus(Vehicle):

    def startEngine(self):
        if not self.condition :
            self.condition = True
            return f"{self.model} yurgazildi"
        else:
            return f"{self.model} allaqachon yurgazilgan."

    def lightOn(self):
        if not self.light_h :
            self.light_h = True
            return f"{self.model} chiroqlari yoqildi"
        else :
            return f"{self.model} chiroqlari yoqiq holatda"
        
    def stopEngine(self):
        if self.condition :
            self.condition = False
            return f"{self.model} O'chirildi"
        else:
            return f"{self.model} o'chiq holatda"
        
    def lightOf(self):
        if self.light_h:
            self.light_h = False
            return f"{self.model} chiroqAri o'chirildi"
        else:
            return f"{self.model} chiroqlari o'chiq holatda"


class Truck(Vehicle):

    def startEngine(self):
        if not self.condition :
            self.condition = True
            return f"{self.model} yurgazildi"
        else:
            return f"{self.model} allaqachon yurgazilgan."

    def lightOn(self):
        if not self.light_h :
            self.light_h = True
            return f"{self.model} chiroqlari yoqildi"
        else :
            return f"{self.model} chiroqlari yoqiq holatda"
        
    def stopEngine(self):
        if self.condition :
            self.condition = False
            return f"{self.model} O'chirildi"
        else:
            return f"{self.model} o'chiq holatda"
        
    def lightOf(self):
        if self.light_h:
            self.light_h = False
            return f"{self.model} chiroqAri o'chirildi"
        else:
            return f"{self.model} chiroqlari o'chiq holatda"      
            
        
ac = Car('gentra') 
print(ac.startEngine())
print(ac.stopEngine())
print(ac.lightOn()) 
print(ac.lightOf()) 
    

