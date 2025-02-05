import json
import requests

natija = requests.get('https://cbu.uz/uz/arkhiv-kursov-valyut/json/')
data = natija.json()
filtered_data = list(filter(lambda x: x['Ccy'] in ['USD','RUB','EUR'], data))
with open('p.json', 'w', encoding='utf-8') as f:
    json.dump(filtered_data, f, indent=2 , ensure_ascii=False)