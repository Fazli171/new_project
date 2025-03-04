import json
from collections import Counter

# from abc import ABC, abstractmethod
# class Transport(ABC):
#     def __init__(self, nomi, tezlik):
#         self.nomi = nomi
#         self.tezlik = tezlik
#     @abstractmethod
#     def harakatlanish(self):
#         pass
#     @abstractmethod
#     def toxtash(self):
#         pass

# class Aftomobil(Transport):
#     def __init__(self, nomi, tezlik, yoq_tur):
#         super().__init__(nomi, tezlik)
#         self.yoq_tur = yoq_tur

#     def harakatlanish(self):
#         return f"{self.nomi} aftomobili {self.yoq_tur} bilan {self.tezlik} gacha harakatlanadi"
    
#     def toxtash(self):
#         return f"aftomobil abs tormoz tizimi bilan to'xtaydi"
    
# class Velosipet(Transport):
#     def __init__(self, nomi, tezlik, ped_turi):
#         super().__init__(nomi, tezlik)
#         self.ped_turi = ped_turi

#     def harakatlanish(self):
#         return f"{self.nomi} velosiped harakatlanishi {self.ped_turi} bilan {self.tezlik} gacha chiqa oladi"
    
#     def toxtash(self):
#         return f"qo'l tormozi bilan to'xtaydi"

# try:
#     mal = [1, 3, 5, 6, 7]
#     file = 'mevalar.json'
#     with open(file , 'r+', encoding='utf-8') as f:
#         try:
#             data = json.load(f)

#         except (json.JSONDecodeError, ValueError):
#             data = []

#         data.append(mal)

#         json.dump(data, f, ensure_ascii=False, indent= 2)
#         print('faylga yozildi')


# except Exception:
#     print("xatolik bor")

# class FileManager:
#     def __init__(self, file):
#         self.file = file

#     def read(self):
#         try:
#             with open(self.file, 'r', encoding='utf-8') as f:
#                 data = json.load(f)
#                 return data if isinstance(data, list) else []
#         except (json.JSONDecodeError, ValueError, FileNotFoundError):
#             return []  

#     def write(self, new_data):
#         if isinstance(new_data, list):
#             with open(self.file, 'w', encoding='utf-8') as f:
#                 json.dump(new_data, f, indent=2, ensure_ascii=False)
#         else:
#             raise ValueError("write() metodi faqat ro‘yxat (list) qabul qiladi.")

#     def append(self, one_data):
#         data = self.read()
#         data.append(one_data)
#         with open(self.file, 'w', encoding='utf-8') as f:
#             json.dump(data, f, indent=2, ensure_ascii=False)


# s = FileManager('mevalar.json')
# print(s.read())  
# s.write([1, 2, 3, 4])  
# s.append(77)  
# print(s.read()) 

# try:
#     file = 'mevalar.json'

#     with open(file, 'r', encoding='utf-8') as k:
#         content = k.read().strip()
        
#         if not content:  
#             print("Fayl bo'sh!")
#             data1 = []
#             data2 = {}
#         else:
#             data = json.loads(content)  
#             data1 = data if isinstance(data, list) else []
#             print("Ro'yxat:", data1)
#             data2 = data if isinstance(data, dict) else {}
#             print("Lug'at:", data2)
        
# except json.JSONDecodeError as e:
#     print(f'JSON o\'qishda xato: {e}')
# except Exception as e:
#     print(f'Xato bor: {e}')

# try:
#     file = 'mevalar.json'
#     with open(file, 'r+', encoding='utf-8') as f:
#         try:
#             data = json.load(f)

#             data1 = data if isinstance(data, list) else []
#             print(data1)
#         except json.JSONDecodeError:
#             f.seek(0)
#             json.dump([], f)~
#             print('fayl bosh unga bosh list yaratildi')
# except Exception:
#     print('xatolik bor')


# with open('pwd.txt', 'r', encoding='utf-8') as f:
#     file = f.readlines()

# parol = [i.strip().split(';')[1] for i in file ]
# counter = Counter(parol)
# print(counter.most_common(5))

 