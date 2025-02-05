import json
import requests

natija = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
data = natija.json()
filtered_data = list(filter(lambda x: x['Ccy'] in ['USD','RUB','EUR'], data))
with open('p.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=2 , ensure_ascii=False)
data = []
for i in filtered_data:
    data.append(f'{i['CcyNm_UZ']}\nSotish kursi: {i['Rate']}\nOlish kursi: {round(float(i['Rate'])*0.97, 2)}\nSana: {i['Date']}\n{'='*20}')

class Tanzaksiya:
    def course(self):
        for i in data:
            print(i.center(80))
        return