import requests
from bs4 import BeautifulSoup

# Kanal URL manzili
url = "https://t.me/s/statistika_fifa_penalty_fast"

# Sahifani yuklash
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Xabarlarni o'qish
messages = soup.find_all("div", class_="tgme_widget_message_text")
for message in messages:
    print(message.text)