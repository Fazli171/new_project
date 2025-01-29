class Money:
    def __init__(self, emaunt: int):

        self._emaunt = emaunt

    @property
    def emaunts(self):
        return f"{self._emaunt}"

    @emaunts.setter
    def emaunts(self, new_emaunt):
        self._emaunt = new_emaunt
s = Money(2000)
print(s.emaunts)
s.emaunts = 300
print(s.emaunts)

class Car :
    car_name = 'BMW'
    def __init__(self, speed, price, color):
        self.speed = speed
        self.price = price
        self.color = color

    @classmethod
    def new_car_name(cls, new_car_name):
        cls.car_name = new_car_name

    def __str__(self):
        return f"car name = {self.car_name} tezligi = {self.speed} rangi = {self.color} narxi = {self.price}"
    @staticmethod
    def car(name):
        return f'{name} ajoyi moshina {Car.car_name}'
    
d = Car(200, 10000, 'red')
print(d)
print(d.car('bmw'))

    

    

        