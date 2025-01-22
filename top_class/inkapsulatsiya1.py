from random import randint
from datetime import datetime
date = datetime.now()
month = date.month
year = date.year

class BankCard:
    def __init__(self):
        self.__balance = 0
        self.__card_num = randint(9860000000000000, 9860999999999999)
        self.__deadline = f"{month}/{year+5}"
        self.__code = randint(1111,9999)

    @property
    def balance(self):
        '''balance check'''
        return f"sizning balansingiz {self.__balance} so'm bor"
    
    def add_balance(self):
        '''balance replenishment'''
        answer = int(input('balans toldirish qiymatni kriting'))
        if answer > 0:
            self.__balance += answer
            return f"balansingizga {answer} so'm to'ldirildi hozirda balans {self.__balance}"
        else:
            return f"balans to'ldirish manfiy bo'lishi mumkin emas"
        
    def remove_balance(self):
        answer = int(input("yechmoqchi bo'lgan summangiz"))
        if answer > 0 and self.__balance > answer:
            self.__balance -= answer
            return f"balansingizdan {answer} yechib olindi"
        else:
            return f"balansingizda mablag' yetarli emas"

    @property
    def deadline(self):
        '''validity period'''
        return self.__deadline  
     
    @property
    def card_num(self):
        '''card number'''
        return self.__card_num
    @property
    def code(self):
        '''amal qilish muddati'''
        return f"karta tastiqlash kodi {self.__code}"
    
a = BankCard()
print(a.code)
print(a.card_num)
print(a.deadline)
print(a.add_balance())
print(a.remove_balance())

    


        