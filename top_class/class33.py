from random import choice, sample


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


p1 = Person("Ali", "Aliyev")
p2 = Person("Mahmud", "Mavlonov")
p3 = Person("Bobur", "ANarov")
p = [p1, p2, p3]

for i in p:
    print(i)
class Home:
    def __init__(self, homeNumber, homeAdres, awer:Person):
        self.homeNumber = homeNumber
        self.homeAdres = homeAdres
        self.awer = awer

    def __str__(self):
        return f"manzil {self.homeAdres} nomeri {self.homeNumber} egasi {self.awer}"


h1 = Home(2, 'choshtepa 2' ,sample(p, k=1)[0])
print(h1)
h2 = Home(4, "o'zar kocha 4", sample(p ,k=1)[0])
print(h2)
h3 = Home(5, "bobur ko'cha 5", sample(p ,k=1)[0])
print(h3)
