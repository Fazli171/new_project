class Math:
    def __init__(self, emaunt):
        self.emaunt = emaunt
        self.x = 10

    def __str__(self):
        return self.emaunt
    
    def __repr__(self):
        return f"malumot reprda chiqdi {self.emaunt}"
    
    def __delattr__(self, name):
        print( f"{name} axususiyati o'chirildi")
        super.__delattr__(name)
mat = Math('200')
del mat.x   
print(mat.x)