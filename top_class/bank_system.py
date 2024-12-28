
from random import randint

class Shaxs:
    def __init__(self, ism, famil, pas_ser, shaxs):
        self.ism = ism
        self.famil = famil
        self.pas_ser = pas_ser
        self.shaxs = shaxs

    def get_ism(self):
        return f"{self.shaxs} shaxs ismi {self.shaxs}"
    
    def get_famil(self):
        return f"{self.shaxs} shaxs familiysi {self.famil}"
    
    def get_pas(self):
        return f"pasport seriya va raqami {self.pas_ser}"
    
    def get_shaxs(self):
        return f"{self.ism} {self.famil} {self.shaxs} shaxs sifatida ro'xatda turadi"
    
    def get_info(self):
        return f"{self.ism} {self.famil} {self.shaxs} shaxs passport malumotlari "

class CardMal(Shaxs):
    MIN_SUM = 1000

    def __init__(self, ism, famil, pas_ser, shaxs, tel_raqam):
        super().__init__(ism, famil, pas_ser, shaxs)
        self.tel_raqam = tel_raqam
        self.hisob_raqam = []
        self.muddati = []
        self.balans = 0
        self.his_mud = {}
        self.tr_history = []

    def get_history(self):
        return self.tr_history

    def plas_raq(self):
        tastiq = input(f"{self.get_info()} va telefon raqami {self.tel_raqam} tastiqlaysizmi\n").lower()
        if tastiq == 'ha':
            self.hisob_raqam.append(f"{randint(9860, 9860)}{randint(1000, 9999)}{randint(1000, 9999)}{randint(1000, 9999)}")
            self.muddati.append(f'{randint(1, 12):02}/{randint(24,30)}')
            self.his_mud = dict(zip(self.hisob_raqam, self.muddati))
        else:
            print('malumotlarni tekshirib qayta murojat qiling')

    def balanss(self):
        for k , v in self.his_mud.items():
            ball = input(f"sizning karta raqamingiz {k} va muddati {v} hisobingizni to'ldirasizmi HA/YO'Q\n").lower()
            if ball == 'ha':
                try:
                    while True:
                        summa = int(input("to'ldirmoqchi bo'lgan summa\n"))
                        if summa >= self.MIN_SUM:
                            self.balans += summa
                            print(f"hisobingiz {summa} ga to'ldirildi : joriy balans {self.balans}")
                            self.tr_history.append(f"kirim -> {summa}")
                            break
                        else:
                            print(f'minimal summa {self.MIN_SUM}')
                except ValueError:
                    print("kritilayotgan malumot raqamlardan iborat bo'lsin")
            else:
                print("bizni tanlaganiz uchun raxmat")

    def get_HisRaq(self):
        return self.his_mud
    
    def get_balans(self):
        return f"sizning balansingiz {self.balans}"

class Transfer(CardMal):
    def __init__(self, ism, famil, tel_raqam, pas_ser: int = None, shaxs: str = None):
        super().__init__(ism, famil, pas_ser, shaxs, tel_raqam)
        self.ism = ism
        self.famil = famil
        self.tel_raqam = tel_raqam

    def get_shaxs(self):
        return f"{self.ism}, {self.famil} va telefon raqami {self.tel_raqam}"
    
    def otkazma(self):
        tastiq = input(f"qabul qiluvchi {self.get_shaxs()}  HA/YO'Q").lower()
        if tastiq == 'ha':
            try:
                summa = int(input("o'tkazma summasini krting : min = 1000 so'm\n"))
                if summa >= self.MIN_SUM:
                    if self.balans >= summa:
                        summa_t = input(f"o'tqazma summasi {summa} OK/X\n").lower()
                        if summa_t == 'ok':
                            while True:
                                try:
                                    kod = randint(10000, 99999)
                                    print(kod)
                                    kod_t = int(input("tastiqlash kodini kriting \n"))
                                    if kod_t == kod:
                                            self.balans -= summa
                                            print(f"o'tkazma muvofaqiyatli yakunlandia; balansda {self.get_balans()}")
                                            self.tr_history.append(f"chiqim -> {summa}")  # Tarixga chiqimni qo'shish
                                            break
                                    else:
                                        print('kodni qayta kriting')
                                except ValueError:
                                    print('kod raqamlardan iborat adashmang')
                        else:
                            print("balansingizda mablag' yetarli emas")
                    else: 
                        print("balansingizda mablag' yetarli emas")
                else:
                    print(f"min {self.MIN_SUM} so'm ")
            except ValueError:
                print('summaga raqam kriting')
        else :
            print("bizni tanlaganiz uchun raxmat")

karta_foydalanuvchi = CardMal("Ali", "Valiyev", "AA1234567", "Fizik", "+998901234567")
karta_foydalanuvchi.plas_raq()
karta_foydalanuvchi.balanss()
print(karta_foydalanuvchi.get_balans())
transfer_foydalanuvchi = Transfer("Bek", "Karimov", "+998912345678")
transfer_foydalanuvchi.balans = karta_foydalanuvchi.balans 
transfer_foydalanuvchi.otkazma()
print(karta_foydalanuvchi.get_history())  # Tarixni chiqarish
