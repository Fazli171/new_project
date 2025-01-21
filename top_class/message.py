from abc import ABC, abstractmethod
class Notification(ABC):

    @abstractmethod
    def noti_fication(self):
        pass
    @abstractmethod
    def message(self, xabar):
        pass

class Telegram(Notification):

    def noti_fication(self):
        print("telegram bildirishnoma")

    def message(self, xabar):
        print(f"sizga {xabar} xabri keldi")

class Inistagram(Notification):

    def noti_fication(self):
        print("inistagram bildirishnima")

    def message(self, xabar):
        print(f"sizga  {xabar} xabar keldi")

class Soliq(Notification):

    def noti_fication(self):
        print("soliq qarzdorligi haqida xabarnoma")

    def message(self, xabar):
        print(f"hurmatli fuqoro sizning soliq bi'yicha umumiy qarzdorligingiz {xabar}")

class Shape(ABC):

    def yuza(self):
        pass
    def peremetr(self):
        pass


        