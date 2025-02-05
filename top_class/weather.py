import requests
import json


class Weather:

    def weather(self):
        result = input("qaysi shahar ob havosi kerak: ").title()
        url = "https://yahoo-weather5.p.rapidapi.com/weather"

        querystring = {"location": result, "format": "json", "u": "f"}

        headers = {
            "X-RapidAPI-Key": "028f8b5236msh3dbc44ec3641e7ap1dfc20jsn7fd67833d3e7",
            "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            data = response.json()
            return json.dumps(data, indent=4)
        else:
            return f"Xatolik: {response.status_code}"