
class Player:
    def __init__(self, ism: str = "Jaloliddin"):
       self.ism = ism

    def action(self):
        return f"{self.ism} o'yinchi harakatlanmoqda"
    
class Derived(Player):
    def __init__(self, ism = "Jaloliddin"):
        super().__init__(ism)

    def action(self):
        return f"{self.ism} Jangchi hujum qilmoqda!"
    
class Mage(Player):
    def __init__(self, ism = "Jaloliddin"):
        super().__init__(ism)

    def action(self):
        return f"Sehrgar sehr ishlatmoqda!"

class Healer(Player):
    def __init__(self, ism = "Jaloliddin"):
        super().__init__(ism)

    def action(self):
        return f"Shifokor o‘z jamoadoshini davolamoqda!"

p0 = Player()
print(p0.action())  
p = Derived()
print(p.action())
p1 = Mage()
print(p1.action())
p2 = Healer()
print(p2.action())