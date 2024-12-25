class Admin:
    def __init__(self,ism, famil, yosh):
        
        self.ism = ism
        self.famil = famil
        self.yosh = yosh
        self.parol = []
        self.login = []
        self.log_por = {}

    def paroll(self):
        belgilar = set('[!@#$%^&*()_+=}]|[{;:,<>./?~`]')
        while True:
            login = input("login o'ylab toping")
            if len(login) > 6 :
                if any(i.isupper() for i in login):
                    if any(i.isdigit() for i in login):
                        if any(i.islower() for i in login):
                            if any(i in belgilar for i in login):
                               print("login qoniqarli") 
                               self.login.append(login)
                               parol = input("parol o'lab toping")
                               if len(parol) > 6 :
                                   if any(i.isupper() for i in parol):
                                       if any(i.islower() for i in parol):
                                           if any(i.isdigit() for i in parol):
                                               if any(i in belgilar for i in parol):
                                                    print("parol qoniqarli") 
                                                    self.parol.append(parol)
                                                    break
                                                else:
                                                   print("parolda kamida bitta maxsus belgi bo'lishi zarur")                                               
                                           else:
                                               print("parolda kamida bitta raqam ishtiroki bo'ishi zarur")
                                       else:
                                           print("parolda kamida bitta kichik harf bo'lishi zarur")
                                   else:
                                       print("parolda kamida bitta katta harf bo'lishi zarur")
                               else:
                                   print("parol kamida 6 ta belgidan iborat bo'lishi zarur")
                            else:
                                print("parolda kamida bitta maxsus belgi bo'lishi zarur")
                        else:
                            print("loginda kamida bitta kichik harif bo'ishi shart")
                    else:
                        print("loginda kamida bitta raqam ishtirok etsin")
                else:
                    print("loginda kamida bitta katta harf ishtiroki bo'lsin")
            else:
                print("login 6 ta belgidan yuqori bo'lishi zarur")
    def logpor(self):
        self.log_por = dict(zip(self.login, self.parol))
        return self.log_por
admin = Admin('Fazliddin', 'Narzullayev', 26)
admin.paroll()

class Admin1:
    def __init__(self, ism, famil, yosh):
        self.ism = ism
        self.famil = famil
        self.yosh = yosh
        self.parol = []
        self.login = []

    def tekshir_parol_login(self, input_text, max_len=6):
        """Login va parolni tekshirish funksiyasi"""
        while True:
            user_input = input(input_text)
            if len(user_input) <= max_len:
                print(f"Input kamida {max_len} ta belgidan iborat bo'lishi kerak.")
                continue
            if not any(i.isupper() for i in user_input):
                print("Inputda kamida bitta katta harf bo'lishi kerak.")
                continue
            if not any(i.isdigit() for i in user_input):
                print("Inputda kamida bitta raqam bo'lishi kerak.")
                continue
            if not any(i.islower() for i in user_input):
                print("Inputda kamida bitta kichik harf bo'lishi kerak.")
                continue
            if not any(i in '[!@#$%^&*()_+=}]|[{;:,<>./?~`]' for i in user_input):
                print("Inputda kamida bitta maxsus belgi bo'lishi kerak.")
                continue
            return user_input

    def paroll(self):
        """Login va parolni o'rnatish"""
        print("Login yaratish jarayoni boshlanadi:")
        login = self.tekshir_parol_login("Loginni o'ylab toping: ")
        self.login.append(login)
        print("Parol yaratish jarayoni boshlanadi:")
        parol = self.tekshir_parol_login("Parolni o'ylab toping: ")
        self.parol.append(parol)
        print("Login va parol muvaffaqiyatli yaratildi!")

admin = Admin1('Fazliddin', 'Narzullayev', 26)
admin.paroll()
