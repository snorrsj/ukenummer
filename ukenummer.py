import requests
from bs4 import BeautifulSoup

URL = 'https://ukenr.no/'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="ugenr")

print(f'Det er {results.text}')