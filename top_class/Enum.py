from enum import Enum

class Gender(Enum):
    Male = 'male'
    Female = 'female'

class Person :
    def __init__(self, fullName, passpordID, gender: Gender):
        self.fullName = fullName
        self.passpordID = passpordID
        self.gender = gender

    def get_Fullname(self):
        return self.fullName
    
    def set_Fullname(self,new_fullName):
        self.fullName = new_fullName

    def passpordID(self):
        return self.passpordID

    def set_passpordID(self, new_passpordID):
        self.passpordID = new_passpordID

