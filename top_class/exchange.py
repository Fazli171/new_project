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
            print(i.center(80))
        return


    def sell(self):
        result = int(input("Valuta juftligini ko'rsating \nUSD->UZS = 0\nRUB->UZS = 1\nEUR->UZS = 2"))
        emaut = float(input(f"{filtered_data[result]['CcyNm_UZ']} -> qiymatni kriting"))
        return f"{round((float(filtered_data[result]['Rate']) * 0.97 )* emaut, 2)} uzs"

    def buy(self):
        result = int(input("Valuta juftligini ko'rsating \nUZS->USD = 0\nUZS=>RUB = 1\nUZS->EUR = 2\n"))
        emaut = float(input("UZS -> qiymatni kriting"))
        return f"{round(emaut / (float(filtered_data[result]['Rate'])), 2)} {filtered_data[result]['CcyNm_UZ']}"

d = Tanzaksiya()
print(d.course())
print(d.sell())
print(d.buy())