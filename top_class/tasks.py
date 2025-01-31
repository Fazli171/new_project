from random import sample
class Loptop:

    def __init__(self, brend: str, model: str, price: int, ):
        self.brend = brend
        self.model = model
        self.price = price

    def get_brend(self):
        return self.brend
    
    def get_model(self):
        return self.model
    
    def get_price(self):
        return self.price
    
    def set_price(self, new_price):
        self.price = new_price

    def apply_discount(self,discount):
        self.price -= (self.price * discount) / 100
        return f"sizga {discount}% chegirma bilan {self.price} nrax belgilandi"
    
    def __str__(self):
        return f"nautbook brendi {self.brend} modeli {self.model} narxi  {self.price}"
    
s = Loptop("acer", "cori 3", 700)
print(s)
print(s.apply_discount(10))


class MathOperations:

    def __init__(self, fan_nomi):
        self.fan_nomi = fan_nomi

    @staticmethod
    def add(a , b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    def power(a, b):
        return a ** b
    
print(MathOperations.add(5, 3))
print(MathOperations.multiply(4, 6))
print(MathOperations.power(2, 3))


class Vhisle:
    def __init__(self, brend: str, speed: int):
        self.brend = brend
        self.speed = speed

    def show_info(self):
        return f"Brend : {self.brend} tezligi : {self.speed} km/h "

class Car(Vhisle):
    def __init__(self, brend, speed, doors):
        super().__init__(brend, speed)
        self.doors = doors

    def show_info(self):
        return super().show_info() + f" eshiklari esa {self.doors} ta "

car = Car("chevrolet", 200, 4)
print(car.show_info())


class User:
    def __init__(self):
        self.__password = ""
        self.shrift = ""

    def set_password(self, new_password):
        self.__password = new_password
        self.__encrypt_password()

    def get_password(self):
        return self.__password

    def __encrypt_password(self):
        self.shrift = "".join(sample(self.__password, len(self.__password)))

    def show_encrypted_password(self):
        return self.shrift

user1 = User()
user1.set_password("secret123")
print(user1.get_password())            # secret123
print(user1.show_encrypted_password()) # Masalan: "t3e1srce2"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist()
playlist.add_song("Song 1")
playlist.add_song("Song 2")

print(len(playlist))  # 2



