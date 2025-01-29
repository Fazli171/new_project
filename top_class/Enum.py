from enum import Enum
from datetime import datetime
from typing import List

class Gender(Enum):
    Male = 'male'
    Female = 'female'

    def __str__(self):
        return self.value

class Person :
    def __init__(self, fullName, passpordID):
        self.fullName = fullName.title()
        self.passpordID = passpordID

    def get_Fullname(self):
        return self.fullName
    
    def set_Fullname(self,new_fullName):
        self.fullName = new_fullName

    def passpordID(self):
        return self.passpordID

    def set_passpordID(self, new_passpordID):
        self.passpordID = new_passpordID

    def get_info(self):
        return f"to'liq ismi {self.fullName} paspordId {self.passpordID}"
    
    def __str__(self):
        return self.fullName
    
class Pessenger(Person):
    def __init__(self, fullName : str, passpordID : str, gender :Gender):
        super().__init__(fullName, passpordID)
        self.gender = gender

    def get_gender(self):
        return self.gender

    def get_info(self):
        return super().get_info() + f"\ngender {self.gender}"
    
p1 = Pessenger('Husniddin Abduhalilov', 'DD284739', Gender.Male)
p2 = Pessenger('Asliddin Rasulov', 'DD284743', Gender.Male)
p3 = Pessenger('Ali Aliyev', 'DD284777', Gender.Male)
p4 = Pessenger('Umar Maxmudov', 'DD284788', Gender.Male)
p5 = Pessenger('Saman Berdiev', 'DD284744', Gender.Male)
p6 = Pessenger('Ali Berdiev', 'DD284745', Gender.Male)
p7 = Pessenger('Kamron Beriev', 'DD284746', Gender.Male)
p8 = Pessenger('Rustam Xusanov', 'DD284747', Gender.Male)
p9 = Pessenger('Lola Xamidova', 'DD284748', Gender.Female)
p10 = Pessenger('Oygul Nazarova', 'DD284749', Gender.Female)
p11 = Pessenger('Davron Toshmatov', 'DD284750', Gender.Male)
p12 = Pessenger('Dilshodbek Oripov', 'DD284751', Gender.Male)
p13 = Pessenger('Shoira Shodmonova', 'DD284752', Gender.Female)
p14 = Pessenger('Yulduz Hamroyeva', 'DD284753', Gender.Female)
p15 = Pessenger('Jasur Karimov', 'DD284754', Gender.Male)
p16 = Pessenger('Malika Karimova', 'DD284755', Gender.Female)
p17 = Pessenger('Zafar Ortiqov', 'DD284756', Gender.Male)
p18 = Pessenger('Sarvar Salimov', 'DD284757', Gender.Male)
p19 = Pessenger('Feruza Zokirova', 'DD284758', Gender.Female)
p20 = Pessenger('Gulnora Raximova', 'DD284759', Gender.Female)
p21 = Pessenger('Bekzod Umarov', 'DD284760', Gender.Male)
p22 = Pessenger('Nodir Xolmurodov', 'DD284761', Gender.Male)
p23 = Pessenger('Shoxista Tursunova', 'DD284762', Gender.Female)
p24 = Pessenger('Javohir Abdullayev', 'DD284763', Gender.Male)
p25 = Pessenger('Xurshid Abdurahmonov', 'DD284764', Gender.Male)
p26 = Pessenger('Sabina Karimova', 'DD284765', Gender.Female)
p27 = Pessenger('Madina G\'aniyeva', 'DD284766', Gender.Female)
p28 = Pessenger('Sanjar Bekmurodov', 'DD284767', Gender.Male)
p29 = Pessenger('Kamola Tursunova', 'DD284768', Gender.Female)
p30 = Pessenger('Olim Abdullayev', 'DD284769', Gender.Male)

pessenges = [p1, p2, p3, p4, p5, p5, p7, p8, p9, p10]
pessenges1 = [p11, p12, p13, p14, p15, p16, p17, p18, p19, p20]
pessenges2 = [p21, p22, p23, p24, p25, p26, p27, p28, p29, p30]

class Driver(Person):
    def __init__(self, fullName, passpordID, age):
        super().__init__(fullName, passpordID)
        self.age = age

    def get_age(self):
        return self.age
    
    def get_borth_year(self):
        return datetime.now().year
    
    def get_info(self):
        return super().get_info() + f"/nAge {self.age} \nBorth year {self.get_borth_year()}"

d1 = Driver('fazliddin narzullayev', 'AA1234', 26)
d2 = Driver('husniddin abduhalilov', 'AA1235', 24)
d3 = Driver('javoxir saydullayev', 'AA1236', 28)
    
class Train():
    def __init__(self,TrainId: str, name: str, sped: int, driver: Driver):
        self.name = name
        self.driver = driver
        self.sped = sped
        self.TrainId = TrainId

    def get_name(self):
        return self.name
    
    def get_driver(self):
        return self.driver
    
    def get_sped(self):
        return self.sped
    
    def get_tainid(self):
        return self.TrainId
    
    def __str__(self):
        return f"Train Id {self.TrainId} \nname {self.name} \ndriver {self.driver} \nsped {self.sped}"
    

t1 = Train('YH187','Sharq', 230, d1)
t1 = Train('YH188','Afrasiyob', 230, d2)
t1 = Train('YH189','Andijon', 230, d3)

class Plartform:
    def __init__(self, platformId: str, status: bool):
        self.platformId = platformId
        self.status = status
    
    def __str__(self):
        return f"platform Id {self.platformId} \nstatus {"bo'sh" if self.status else "bo'sh emas"}"
pl = Plartform('w123', True)
pl1 = Plartform('w124', True)
pl2 = Plartform('w125', True)
    
class Trip:
    def __init__(self, from_ , to , train: Train, platform: Plartform, pessengers: List[Pessenger], priceTrip, dateTrip):
        self.from_ = from_
        self.to = to
        self.train = train
        self.platform = platform
        self.pessengers = pessengers
        self.priceTrip = priceTrip
        self.dataTrip =dateTrip

    def getFromTo(self):
        return f"{self.from_} - {self.to}"

    def getPessengers(self):
        temp = [f"{i} . {v} " for i , v in enumerate(self.pessengers,1)]
        return "\n". join(temp)
    def __str__(self):
        return f"{self.getFromTo()} \n{self.train} Platform {self.platform} \npessegers {self.getPessengers()} \npriceTrip : {self.priceTrip} \ndataTrip : {self.dataTrip}"
    
trip = Trip('Toshkend', 'Samarqand', t1, pl, pessenges, 45, datetime.now())
trip1 = Trip('Toshkend', 'Buxoro', t1, pl1, pessenges1, 30, datetime.now())
trip2 = Trip('Toshkend', 'Andijon', t1, pl2, pessenges2, 50, datetime.now())
tripss = [trip, trip1, trip2]
        
class RailwayStadion:

    def __init__(self, name , adress, trips : List[Trip]):
        self.name = name
        self.adress = adress
        self.trips = trips
    def getTrip(self):
        tmp = [f"{i} . {v}" for i , v in enumerate(self.trips, 1)]
        return '\n'. join(tmp)
    def __str__(self):
        return f"Name : {self.name} \nadress : {self.adress} \nTrips : {self.getTrip()}"
    
rail = RailwayStadion('janubiy vafzal', 'sergili tumani: toshkent', tripss)
print(rail)
        