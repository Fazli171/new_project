class Avtomobil:
    def init (self, brend, benzin_sarfi, benzin_qavati):
        self.__brend = brend  
        self.__holat = False
        self.__benzin = benzin_qavati  
        self.__benzin_sarfi = benzin_sarfi  

    @property
    def brend(self):
        return self.__brend

    @brend.setter
    def brend(self, yangi_brend):
        if isinstance(yangi_brend, str) and yangi_brend:
            self.__brend = yangi_brend
        else:
            print("Brend noto'g'ri!")

    @property
    def benzin(self):
        return self.__benzin

    @benzin.setter
    def benzin(self, benzin_quy):
        if benzin_quy >= 0:
            self.__benzin = benzin_quy
        else:
            print("Benzin miqdori manfiy bo'lishi mumkin emas!")

    @property
    def benzin_sarfi(self):
        return self.__benzin_sarfi

    @benzin_sarfi.setter
    def benzin_sarfi(self, yangi_b_s):
        if yangi_b_s > 0:
            self.__benzin_sarfi = yangi_b_s 
        else:
            print("Benzin sarfi musbat son bo'lishi kerak!")

    @property
    def holat(self):
        return "yoqilgan" if self.__holat else "o'chirilgan"

    def yoqish(self):
        if self.__holat:
            print(f"{self.__brend} allaqachon yoqilgan!")
        else:
            self.__holat = True
            print(f"{self.__brend} muvaffaqiyatli yoqildi.")

    def ochirish(self):
        if not self.__holat:
            print(f"{self.__brend} allaqachon o'chirilgan!")
        else:
            self.__holat = False
            print(f"{self.__brend} muvaffaqiyatli o'chirildi.")

    def yurish(self, masofa):
        if not self.__holat:
            print(f"{self.__brend} o'chirilgan! Avval uni yoqing.")
            return
        
        zarur_benzin = self.__benzin_sarfi * masofa

        if zarur_benzin <= self.__benzin:
            self.__benzin -= zarur_benzin
            print(f"{self.brend} {masofa} km yurmoqda... Benzin: {self.benzin:.2f} litr")
        else:
            print(f"{self.__brend} o'zi uchun yetarli benzin topa olmadi. Benzin yetarli emas!")

    def toldirish(self, miqdor, masofa=None):
        if miqdor <= 0:
            print("Noto'g'ri miqdor!")
            return
        
        self.__benzin += miqdor
        print(f"{self.__brend} uchun {miqdor} litr benzin to'ldirildi.")
        
        if masofa:
            zarur_benzin = self.__benzin_sarfi * masofa
            if zarur_benzin <= self.__benzin:
                print(f"{masofa} km yurish uchun benzin yetarli!")
            else:
                print(f"{masofa} km yurish uchun benzin yetarli emas!")

avto = Avtomobil("Toyota", 0.4, 20)

# Avto holatini tekshirish
print(f"Moshina holati: {avto.holat}")  # O'chirilgan holatda bo'ladi

# Moshinani yoqish
avto.yoqish()
print(f"Moshina holati: {avto.holat}")  # Yoqilgan holatda bo'ladi

# Benzin to'ldirish va masofa tekshirish
avto.toldirish(10, 50)  # 50 km masofa uchun benzin yetarli yoki emasligini tekshiradi

# Moshinani yurish
avto.yurish(10)

# Moshinani o'chirish
avto.ochirish()
print(f"Moshina holati: {avto.holat}")  # O'chirilgan holatga qaytadi