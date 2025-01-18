class Shape:
    def __init__(self, color):
        self.color = color
        self.area = 0

    def yuza(self):
        return self.color
    
    def get_info(self):
        return f"rangi {self.color} \nyuza {self.yuza}"
    
    def __str__(self):
        return self.color
    
class Rectangle(Shape):
    def __init__(self, color, boyi, eni):
        super().__init__(color)
        self.boyi = boyi
        self.eni = eni

    def yuza(self):
        self.area = self.boyi * self.eni
        return self.area
    
    def get_info(self):
        return f"rangi {self.color} boyi {self.boyi}  eni {self.eni}"
    
s = Rectangle('red', 12, 3)
print(s.yuza())
print(s.get_info())
print(s)

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def yuza(self):
        self.area = self.side ** 2
        return self.area
    
    def get_info(self):
        return f"rangi {self.color} va tomoni {self.side}"
    
si = Square('balck', 9)

print(si.yuza())
print(si.get_info())
print(si)

