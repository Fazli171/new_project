class Admin:
    def __init__(self):
        self.parol = []
        self.login = []
        self.log_por = {}
    def set_login(self):
        while True:
            login = input('login yarating')
            if 6 < len(login):
                if any (i.isdigit() for i in login):
                    if any(i.isupper() for i in login):
                            self.login.append(login)
                            print('qoniqarli login')
                            break
                    else:
                        print("login hech bo'lmaganda bitta kotta harf bo'lishi kerak")
                else:
                    print("login harflar va raqamlardan iborat bo'lsin")
            else:
                print('login 6 ta belgidan kop bolishi kerak')  
    def set_parol(self):
        while True:
            parol = input("parol o'ylab toping")
            if parol != self.login[-1]:
                if 6 < len(parol):
                    if any (i.isupper() for i in parol):
                        if any(i.isdigit() for i in parol):
                            self.parol.append(parol)
                            print("qoniqarli parol")
                            break
                        else:
                            print("parol hech bo'lmasa bitta raqam bo'lishi kerak")
                    else:
                        print("parol hech bo'lmaganda bitta harfi kotta bo'lishi kerak")       
                else:
                    print("parol 6 belgidan ko'p bo'lishi kerak")
            else:
                print("parol va login bir xil bo'lishi mumkin emas")
    def set_prof(self):
        if len(self.login) == len(self.parol):
            self.log_por = dict(zip(self.login,self.parol))
            return self.log_por
        else :
            return 'malumotlar yetarli emas'

class AdminPanel(): 
    def __init__(self, admin_abj):
    
        self.log_por = admin_abj.set_prof()
    def Ad_panel(self):
        while True:
            login = input('loginni kriting  ')
            if login in self.log_por:
                print("login muvoffaqiyatli kritdingiz")
                sanoq = 0
                while True:   
                    parol = input("parolni kriting  ")
                    if parol == self.log_por[login]:
                        print("tizimga hush kelibsiz")
                        break
                    else:
                        print("siz xato porol kritdingiz")
                    if sanoq >= 3:
                        print("urintishlar soni ortib ketdi")
                        break
                    sanoq += 1
            else:
                print('siz kritgan login mavjud emas')

admin = Admin()
admin.set_login()
admin.set_parol()
panel = AdminPanel(admin)
panel.Ad_panel()
print(admin.set_prof())

