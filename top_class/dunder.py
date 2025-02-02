lis = [1, 2, 5, 7, 9, 34, 90, 12, 45]

class Math:
    def __init__(self, emaunt, liss, itm):
        self.emaunt = emaunt
        self.x = 10
        self.liss = liss
    def __str__(self):
        return self.emaunt
    
    def __repr__(self):
        return f"malumot reprda chiqdi {self.emaunt}"
    
    def __delattr__(self, name):
        '''class xususiyatini o'chirish '''
        print( f"{name} axususiyati o'chirildi")
        super.__delattr__(name)

    def __eq__(self, value):
        if isinstance(value, Math):
            return self.emaunt == value.emaunt
        return f'faqat tegishli class abyektlari bilan solishtiriladi'

    def __len__(self):
        return len(self.liss)
    
    def __getitem__(self, index):
        return self.liss[index]
    
    def __setitem__(self, index, value):
        self.liss[index] = value

    def __contains__(self, qiymat):
        return qiymat in self.liss
    
    def __iter__(self):
        return iter(self.itm)


mat = Math(200, lis)
print(mat[2])
print(len(mat))
mat[1] = 22
print(mat.liss)
print(11 in lis)


