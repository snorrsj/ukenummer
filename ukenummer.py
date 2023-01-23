import requests
from bs4 import BeautifulSoup
import datetime

URL = 'https://ukenr.no/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ugenr")

day = datetime.datetime.today().weekday()
days = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
now = datetime.datetime.now()
month = ["Januar", "Februar", "Mars", "April",
        "Mai", "Juni", "Juli", "August", "September",
        "Oktober", "November", "Desember"]


print(f'Det er {results.text}')
print(f'{days[day]}, {now.strftime("%d")}. {month[now.month]} {now.strftime("%Y")}')

