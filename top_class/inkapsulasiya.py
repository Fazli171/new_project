class Avtomobil:
    def init(self, brend, benzin_sarfi, benzin_qavati):
        self.__brend = brend  # Avtomobilning brendi
        self.__holat = False  # Avtomobilning holati (yoqilgan yoki o'chirilgan)
        self.__benzin = benzin_qavati  # Benzin miqdori (yashirin, inkapsulyatsiya)
        self.__benzin_sarfi = benzin_sarfi  # Benzin sarfi (1 km uchun litr)

    @property
    def brend(self):
        """Brendni olish."""
        return self.__brend

    @brend.setter
    def brend(self, yangi_brend):
        """Brendni o'zgartirish."""
        if isinstance(yangi_brend, str) and yangi_brend:
            self.__brend = yangi_brend
        else:
            print("Brend noto'g'ri!")

    @property
    def benzin(self):
        """Benzin miqdorini olish."""
        return self.__benzinz

    @benzin.setter
    def benzin(self, yangi_benzin_miqdori):
        """Benzin miqdorini o'zgartirish."""
        if yangi_benzin_miqdori >= 0:
            self.__benzin = yangi_benzin_miqdori
        else:
            print("Benzin miqdori manfiy bo'lishi mumkin emas!")

    @property
    def benzin_sarfi(self):
        """Benzin sarfini olish."""
        return self.__benzin_sarfi

    @benzin_sarfi.setter
    def benzin_sarfi(self, yangi_benzin_sarfi):
        """Benzin sarfini o'zgartirish."""
        if yangi_benzin_sarfi > 0:
            self.__benzin_sarfi = yangi_benzin_sarfi
        else:
            print("Benzin sarfi musbat son bo'lishi kerak!")

    def yoqish(self):
        """Avtomobilni yoqish."""
        if self.__holat:
            print(f"{self.__brend} allaqachon yoqilgan!")
        else:
            self.__holat = True
            print(f"{self.__brend} muvaffaqiyatli yoqildi.")

    def ochirish(self):
        """Avtomobilni o'chirish."""
        if not self.__holat:
            print(f"{self.__brend} allaqachon o'chirilgan!")
        else:
            self.__holat = False
            print(f"{self.__brend} muvaffaqiyatli o'chirildi.")

    def yurish(self, masofa):
        """Avtomobilni yuritish va benzin yetarliligini tekshirish."""
        if not self.__holat:
            print(f"{self.__brend} o'chirilgan! Avval uni yoqing.")
            return
        
        # Yurgan masofaga qarab benzin sarfi
        zarur_benzin = self.__benzin_sarfi * masofa

        if zarur_benzin <= self.__benzin:
            self.__benzin -= zarur_benzin
            print(f"{self.brend} {masofa} km yurmoqda... Benzin: {self.benzin:.2f} litr")
        else:
            print(f"{self.__brend} o'zi uchun yetarli benzin topa olmadi. Benzin yetarli emas!")

    def toldirish(self, miqdor):
        """Benzinni to'ldirish."""
        if miqdor <= 0:
            print("Noto'g'ri miqdor!")
        else:
            self.__benzin += miqdor
            print(f"{self.__brend} uchun {miqdor} litr benzin to'ldirildi.")

# Obyekt yaratish
avto = Avtomobil("Toyota", benzin_sarfi=0.05, benzin_qavati=50)  # Benzin sarfi: 0.05 litr/km, maksimal benzin: 50 litr

# Property metodlari orqali atributlarga kirish va o'zgartirish
print(avto.brend)  # "Toyota"
avto.brend = "Honda"  # Brendni o'zgartirish
print(avto.brend)  # "Honda"

print(avto.benzin)  # 50
avto.benzin = 40  # Benzin miqdorini o'zgartirish
print(avto.benzin)  # 40

print(avto.benzin_sarfi)  # 0.05
avto.benzin_sarfi = 0.06  # Benzin sarfini o'zgartirish
print(avto.benzin_sarfi)  # 0.06