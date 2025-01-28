from enum import Enum

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
    def __init__(self, fullName, passpordID, gender :Gender):
        super().__init__(fullName, passpordID)
        self.gender = gender

    def get_info(self):
        return super().get_info() + f"gender {self.gender}"

