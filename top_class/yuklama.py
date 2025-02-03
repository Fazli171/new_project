from typing import List
import json
from datetime import datetime, timedelta

# class Book:
#     def __init__(self, title: str, author: str, year: int, genre: str):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.genre = genre

#     def get_info(self) -> str:
#         """Kitob haqida to'liq ma'lumot qaytaradi."""
#         return f"{self.title} - {self.author}, {self.year} ({self.genre})"

#     def update_title(self, new_title: str):
#         """Kitob nomini o'zgartiradi."""
#         self.title = new_title

# class Library:
#     def __init__(self, books: List[Book] = None):
#         """Kutubxona obyektini yaratish."""
#         self.books = books if books is not None else []

#     def add_book(self, book: Book):
#         """Kutubxonaga yangi kitob qo'shadi."""
#         self.books.append(book)

#     def remove_book(self, title: str):
#         """Berilgan nomdagi kitobni kutubxonadan o'chiradi."""
#         self.books = [book for book in self.books if book.title != title]

#     def find_books_by_author(self, author: str) -> List[Book]:
#         """Muallifga tegishli barcha kitoblarni qaytaradi."""
#         return [book for book in self.books if book.author == author]

#     def sort_books_by_year(self):
#         """Kitoblarni yillar bo'yicha saralaydi."""
#         self.books.sort(key=lambda book: book.year)

#     def get_all_books(self) -> List[str]:
#         """Kutubxonadagi barcha kitoblarning ma'lumotlarini qaytaradi."""
#         return [book.get_info() for book in self.books]

#     def clear_library(self):
#         """Kutubxonadagi barcha kitoblarni o'chiradi."""
#         self.books.clear()

# library = Library()

# book1 = Book("Python Basics", "John Doe", 2020, "Programming")
# book2 = Book("Advanced Python", "Jane Smith", 2021, "Programming")
# book3 = Book("Data Science", "John Doe", 2019, "Science")

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# print(library.get_all_books())

# print([b.get_info() for b in library.find_books_by_author("John Doe")])

# library.sort_books_by_year()
# print(library.get_all_books())

# library.remove_book("Python Basics")
# print(library.get_all_books())

# library.clear_library()
# print(library.get_all_books())



# class Frut:
#     def __init__(self, name, kg_soni, saq_mud):
#         self.name = name
#         self.kg_soni = kg_soni
#         self.saq_mud = saq_mud

#     def get_info(self):
#         return {
#             "name": self.name,
#             "kg_soni": self.kg_soni,
#             "saq_mud": self.saq_mud.strftime("%d-%B %Y")  
#         }

# mevalar = {}
# n = 1

# while True:
#     name = input("Mevani nomini kiriting (yoki 'stop' deb yozing): ").lower()
#     if name == "stop":
#         break
#     if not name.isalpha():
#         print("Iltimos, meva nomini faqat harflar bilan kiriting! Raqam yoki maxsus belgilar ishlatmang.")
#         continue

#     while True:
#         kg_soni = input("Mevani kg(soni) ni kiriting: ")
#         if kg_soni.isdigit():
#             kg_soni = int(kg_soni)
#             break
#         else:
#             print("Iltimos, mevaning kg(soni)ni faqat raqamlar bilan kiriting!")

#     while True:
#         saq_mud = input("Saqlash muddatini kiriting (kunlarda): ")
#         if saq_mud.isdigit():
#             saq_mud = int(saq_mud)  
#             s = datetime.now() + timedelta(days=saq_mud)
#             break
#         else:
#             print("Iltimos, faqat raqamlardan foydalaning!")

#     meva_key = f"meva{n}"
#     mevalar[meva_key] = Frut(name, kg_soni, s).get_info() 
#     n += 1

# try:
#     with open("mevalar.json", "a", encoding="utf-8") as file:
#         json.dump(mevalar, file, indent=4, ensure_ascii=False)
#     print("\n✅ Mevalar JSON faylga saqlandi: mevalar.json")
# except Exception as e:
#     print(f"\n❌ Xatolik yuz berdi: {e}")


'''
class dokon 
obj = maxsulotlar
class mevalar 


'''
# from typing import List

# class Mevalar:
#     def __init__(self, name, kg_dona):
#         self.name = name
#         self.kg_dona = kg_dona

#     def __str__(self):
#         return f"meva nomi : {self.name} kg(dona) : {str(self.kg_dona)}"
    
# meva1 = Mevalar('olma', 12)
# meva2 = Mevalar('Anjir', 20)
# meva3 = Mevalar('gilos', 30)
# meva4 = Mevalar('olxori', 18)

# mevalar = [meva1, meva2, meva3, meva4]

# class Masalliq:
#     def __init__(self, name, kg):
#         self.name = name
#         self.kg = kg

#     def __str__(self):
#         return f"nomi {self.name} kg {self.kg}"

# masalliq1 = Masalliq('shakar', 5)
# masalliq2 = Masalliq('suv', 3)
# masalliq3 = Masalliq('tuz', 2)

# masalliqlar = [masalliq1, masalliq2, masalliq3]

# class Product:
#     def __init__(self, meva: List[Mevalar], masalliq: List[Masalliq]):
#         self.meva = meva
#         self.masalliq = masalliq

#     def __str__(self):
#         return f"Mevalar: \n" + "\n".join(str(m) for m in self.meva) + "\nMasalliqlar: \n" + "\n".join(str(m) for m in self.masalliq)
    
# product = Product(mevalar, masalliqlar)

# print(product)


class Student:
    def __init__(self, name, age, kurs):
        self.name = name
        self.kurs = kurs
        self.age = age

    def get_info(self):
        return {
            "name ": self.name.title(),
            "age" : self.age,
            "kurs" : self.kurs
        }
        
talabalar = {}

while True:
    name = input("talaba ismini kriting : ").lower()
    if name == 'stop':
        break
    if not name.isalpha():
        print('Talaba ismida raqamlar ishtiroki mumkin emas')
        continue
    while True:
        age = input('talaba yoshini kriting : ')
        if age.isdigit():
            age = int(age)
            break
        else:
            print('talaba yoshi raqamlardan iborat bolishi zarur')

    while True:
        kurs = input("talaba kursini kriting : ") 
        if kurs.isdigit():
            kurs = int(kurs)
            break
        else:
            print("talaba yoshini raqamlardan iborat bo'lishi zarur")
    

    talaba = f"talaba{len()}"
    talabalar[talaba] = Student(name, age, kurs).get_info()
    
 
try:
    with open("talabalar.json", "a", encoding="utf-8") as file:
        json.dump(talabalar, file, indent=4, ensure_ascii=False)
    print("\n✅ talabalar JSON faylga saqlandi: talabalar.json")
except Exception as e:
    print(f"\n❌ Xatolik yuz berdi: {e}")
