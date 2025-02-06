import json
import requests

natija = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
data = natija.json()
filtered_data = list(filter(lambda x: x['Ccy'] in ['USD','RUB','EUR'], data))
with open('p.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=2 , ensure_ascii=False)
data = []
for i in filtered_data:
    data.append(f"{i['CcyNm_UZ']}\nSotish kursi: {i['Rate']}\nOlish kursi: {round(float(i['Rate'])*0.97, 2)}\nSana: {i['Date']}\n{'='*20}")

class Tanzaksiya:
    def course(self):
        for i in data:
            print(f"{i.center(80)}✅")
        return

    def sell(self):

        while True:
            try:
                result = int(input("SOTISH : Valuta juftligini ko'rsating \nUSD->UZS = 0\nEUR->UZS = 1\nRUB->UZS = 2: \n -> "))
                if result in [0, 1, 2]:
                    emaut = float(input(f"{filtered_data[result]['CcyNm_UZ']} -> qiymatni kriting\n -> "))
                    print(f"{round((float(filtered_data[result]['Rate']) * 0.97 )* emaut, 2)} uzs ✅")
                    break
                else:
                    print (f"siz yubrgan <{result}> bo'yicha malumot yo'q  ❌")
            except ValueError:
                print('Xato: siz faqat raqam kriting')
    def buy(self):
        while True:
            try:
                result = int(input("Sotib olish: Valuta juftligini ko'rsating \nUZS->USD = 0\nUZS=>EUR = 1\nUZS->RUB = 2\n -> "))
                if result in [0, 1, 2]:  
                    emaut = float(input("UZS -> qiymatni kriting\n -> "))
                    return f"{round(emaut / (float(filtered_data[result]['Rate'])), 2)} {filtered_data[result]['CcyNm_UZ']} ✅"
                else:
                    return f"siz yubrgan <{result}> bo'yicha malumot yo'q  ❌"
            except ValueError:
                print("Xato: siz faqat raqamlar kriting")
d = Tanzaksiya()

while True:
    exchange = input("Valut ayirboshlash xizmatlari \n    Kurs(0)\n    Sotish(1)\n    Sotib olish(2) \nchiqish (exit)\n ").lower()
    if exchange == '0':
        print(d.course())
        
    elif exchange == '1':
        print(d.sell())
        
    elif exchange == '2':
        print(d.buy())
        
    elif exchange in ['exit', 'chiqish']:
        print("Xizmatdan foydalanganingiz uchun rahmat!")
        break
    else:
        print("bunday ximat turi yo'q")    








