class Math:
    def __init__(self, emaunt):
        self.emaunt = emaunt

    def __str__(self):
        return self.emaunt
    
    def __repr__(self):
        return f"malumot reprda chiqdi {self.emaunt}"
    
mat = Math('200')
print(mat)   
print(repr(mat))     