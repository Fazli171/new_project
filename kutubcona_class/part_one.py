class Kutubxona:

    kitoblar = {}
    kitob = {}

    def __init__(self):
        pass

    def kitob_qosh(self):
        while True:
            javob = input("Kitob qo'shasizmi? (ha/yo'q): ").lower()
            if javob == 'ha':
                kitob, muallif = map(str, input("Kitob nomi va muallifini vergul bilan ajrating: ").split(','))
                javob1 = input(f"{kitob.title()} kitobining muallifi {muallif.title()} tasdiqlaysizmi? (ha/yo'q): ").lower()
                if javob1 == 'ha':
                    Kutubxona.kitoblar.setdefault(kitob.strip(), muallif.strip())
                    print(f"'{kitob.title()}' kitob muvoffaqiyatli qo'shildi.")
                else:
                    print("Malumotlarni qayta kiriting.")
            else:
                print("Kitob qo'shish qismi yakunlandi.")
                return

    def kitobni_ol(self):
        while True:
            javob = input("Olmoqchi bo'lgan kitobni yozing yoki enter tugmasini bosing: ").lower()
            if javob == '':
                print("Hech narsa tanlanmadi.")
                return ", ".join([f"o'chirilayotgan {kitob} (muallifi: {muallif})" for kitob, muallif in Kutubxona.kitob.items()])
            if javob in Kutubxona.kitoblar.keys():
                ochir_kitob = Kutubxona.kitoblar.pop(javob)
                Kutubxona.kitob[javob] = ochir_kitob  
                print(f"'{javob.title()}' kitob o'chirildi va alohida saqlandi.")
                return
            else:
                print("Bunday kitob mavjud emas.")

    def get_info(self):
        return ", ".join([f"{kitob} (muallifi: {muallif})" for kitob, muallif in Kutubxona.kitoblar.items()])


kutubxona = Kutubxona()
kutubxona.kitob_qosh()  
print(kutubxona.get_info())  
kutubxona.kitobni_ol()  
print(kutubxona.get_info())  


    