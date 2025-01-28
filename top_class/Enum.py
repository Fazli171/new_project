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

class Plartform:
    def __init__(self, platformId: str, status: bool):
        self.platformId = platformId
        self.status = status
    
    def __str__(self):
        return f"platform Id {self.platformId} status {"bo'sh" if self.status else "bo'sh emas"}"
    
class Trip:
    def __init__(self, from_ , to , train: Train, platform: Plartform, pessengers: List[Pessenger], priceTrip, dateTrip):
        self.from_ = from_
        self.to = to
        self.train = train
        self.platform = platform
        self.pessengers = pessengers
        self.priceTrip = priceTrip
        self.dataTrip =dateTrip

    
        
        
        
        

        
        


    


