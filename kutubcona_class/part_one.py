class Kutubxona:
    def __init__(self):
        self.kitoblar = {}
        self.olingan_kitoblar = {} 

    def kitob_qosh(self):
        while True:
            javob = input("Kitob qo'shasizmi? (ha/yo'q): ").lower()
            if javob == 'ha':
                try:
                    kitob, muallif = map(str, input("Kitob nomi va muallifini vergul bilan ajrating: ").split(','))
                    kitob, muallif = kitob.strip(), muallif.strip()
                    javob1 = input(f"{kitob.title()} kitobining muallifi {muallif.title()} tasdiqlaysizmi? (ha/yo'q): ").lower()
                    if javob1 == 'ha':
                        if kitob in self.kitoblar:
                            print(f"'{kitob.title()}' allaqachon mavjud.")
                        else:
                            self.kitoblar[kitob] = muallif
                            print(f"'{kitob.title()}' kitob muvoffaqiyatli qo'shildi.")
                    else:
                        print("Ma'lumotlarni qayta kiriting.")
                except ValueError:
                    print("Ma'lumotni to'g'ri formatda kiriting: Kitob nomi, Muallif")
            elif javob == 'yo\'q':
                print("Kitob qo'shish qismi yakunlandi.")
                break
            else:
                print("Faqat 'ha' yoki 'yo'q' deb javob bering.")

    def kitobni_ol(self):
        while True:
            javob = input("Olmoqchi bo'lgan kitob nomini yozing yoki enter tugmasini bosing: ").strip()
            if javob:
                if javob in self.kitoblar:
                    muallif = self.kitoblar.pop(javob)
                    self.olingan_kitoblar[javob] = muallif
                    print(f"'{javob.title()}' kitobi olingan kitoblar ro'yxatiga qo'shildi.")
                else:
                    print(f"'{javob.title()}' kitobi mavjud emas.")
            else:
                print("Kitob olish qismi yakunlandi.")
                break

    def get_info(self):
        if self.kitoblar:
            return ", ".join([f"{kitob.title()} (muallifi: {muallif.title()})" for kitob, muallif in self.kitoblar.items()])
        else:
            return "Kutubxonada kitoblar mavjud emas."

    def get_olingan_kitoblar(self):
        if self.olingan_kitoblar:
            return ", ".join([f"{kitob.title()} (muallifi: {muallif.title()})" for kitob, muallif in self.olingan_kitoblar.items()])
        else:
            return "Olingan kitoblar mavjud emas."


# Sinov
kutubxona = Kutubxona()
kutubxona.kitob_qosh()
print("Kutubxonadagi kitoblar:", kutubxona.get_info())
kutubxona.kitobni_ol()
print("Kutubxonadagi kitoblar:", kutubxona.get_info())
print("Olingan kitoblar:", kutubxona.get_olingan_kitoblar())
    