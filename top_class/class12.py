from random import sample
class Car:

    def __init__(self, car_name, car_number):
        self.car_name = car_name
        self.car_number = car_number

    def getName(self):
        return self.car_name

    def getNumber(self):
        return self.car_number

    def setNumber(self, new_number):
        self.car_number = new_number
        return self.car_number
    
    def __str__(self):
        return f"{self.car_name} {self.car_number}"
cars_name = ['Tiko', 'GentrA', 'Cobalt', 'nexia']
cars_number = ['10A324GD', '20S091Sl', '30E232SL','01W432HK']

ran_names = sample(cars_name,k=len(cars_name))
ran_numbers = sample(cars_number,k=len(cars_number))

cars = [Car(name, number) for name, number in zip(ran_names,ran_numbers)]

with open ('file.txt', 'w') as file:
    for i, car in enumerate(cars, 1):
        file.write(f'{i} {car}\n' )










    # with open('file.txt', 'w') as file:











# lis = [['tiko', '01A123VB']
#        ['matiz', '30D932NM']
#        ['Nexia_2', '30N946LA']
#        ["Gerntra", '01L390DG']
#        [ 'Captiva', "10K235OK"]
#        ["BYD", '20K492HK']
#        ['BMW', '25F298LK']]
