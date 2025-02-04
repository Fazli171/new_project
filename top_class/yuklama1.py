from abc import ABC, abstractmethod
class Transport(ABC):
    def __init__(self, nomi, tezlik):
        self.nomi = nomi
        self.tezlik = tezlik
    @abstractmethod
    def harakatlanish(self):
        pass
    @abstractmethod
    def toxtash(self):
        pass

class Aftomobil(Transport):
    def __init__(self, nomi, tezlik, yoq_tur):
        super().__init__(nomi, tezlik)
        self.yoq_tur = yoq_tur

    def harakatlanish(self):
        return f"{self.nomi} aftomobili {self.yoq_tur} bilan {self.tezlik} gacha harakatlanadi"
    
    def toxtash(self):
        return f"aftomobil abs tormoz tizimi bilan to'xtaydi"
    
class Velosipet(Transport):
    def __init__(self, nomi, tezlik, ped_turi):
        super().__init__(nomi, tezlik)
        self.ped_turi = ped_turi

    def harakatlanish(self):
        return f"{self.nomi} velosiped harakatlanishi {self.ped_turi} bilan {self.tezlik} gacha chiqa oladi"
    
    def toxtash(self):
        return f"qo'l tormozi bilan to'xtaydi"