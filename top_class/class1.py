class Person:
    def __init__(self, ism, fam, yosh):
        self.ism = ism
        self.fam = fam
        self.yosh = yosh

    def get_info(self):
        return f"{self.ism} {self.fam}, yoshi {self.yosh} da"


class Application(Person):
    def __init__(self, ism, fam, yosh, lavozim):
        super().__init__(ism, fam, yosh)
        self.lavozim = lavozim

    def ariza(self):
        if self.yosh >= 18:
            print("Ariza qabul qilindi")
        else:
            print("Siz balog'at yoshiga yetmagansiz, ariza o'tkazib yuborildi.")
            return False
        return True


class JobRoles(Application):
    ish_lar = [] 
    def __init__(self, ism, fam, yosh, lavozim):
        super().__init__(ism, fam, yosh, lavozim)
        self.job = {
            "Frontend Developer": 1000,
            "Backend Developer": 1200,
            "Full-Stack Developer": 1500,
            "Mobile App Developer": 1300,
            "Game Developer": 1400,
            "Software Engineer": 1600,
            "Data Scientist": 2000,
            "Data Analyst": 1800,
            "Machine Learning Engineer": 2200,
        }

    def qabul(self, ish_s: int = 40):
        self.ish_s = ish_s
        if self.ish_s < 40:
            print("Kampaniya qoidalariga ko'ra haftasiga 40 soatdan kam ishlash mumkin emas.")
            return  

        if self.lavozim in self.job.keys():
            natija = input(
                f'''Sizni arizangizni ko'rib chiqdik. Lavozim: {self.lavozim}, ish soati: {self.ish_s}.
Sizga bu qoniqarlimi? (HA/YO'Q): '''
            ).lower()
            if natija == 'ha':
                javob = input(
                    f'''Sizga {self.lavozim} uchun {self.job[self.lavozim]} oylik to'lanadi. 
Bu narx sizga qoniqarlimi? (HA/YO'Q): '''
                ).lower()
                if javob == 'ha':
                    print("Tabriklaymiz, siz ishga qabul qilindingiz!")
                    JobRoles.ish_lar.append(
                        f"{self.get_info()} {self.lavozim} oyligi {self.job[self.lavozim]} ish soati {self.ish_s}"
                    )
                else:
                    print("Afsuski, sizga bundan yuqori maosh taklif qila olmaymiz.")
            else:
                print("Ariza bekor qilindi.")
        else:
            print("Kechirasiz, siz tanlagan lavozim bizda mavjud emas.")

    @classmethod
    def get_all_info(cls):
        if not cls.ish_lar:
            return "Sizda qabul qilingan ishlar mavjud emas."
        return "\n".join(cls.ish_lar)


ishchilar = [
    JobRoles("Fazliddin", "Narzullayev", 26, "Backend Developer"),
    JobRoles("Husniddin", "Abduhalilov", 17, "Frontend Developer"),
    JobRoles("Abror", "Toraqulov", 16, "Full-Stack Developer"),
    JobRoles("Faxri", "Bekmirzayev", 26, "Software Engineer")
]

for ishchi in ishchilar:
    print(ishchi.get_info())
    if ishchi.ariza(): 
        ishchi.qabul(40)
    print("-" * 50)

print("Barcha ishchilar:")
print(JobRoles.get_all_info())
