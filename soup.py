import requests
from bs4 import BeautifulSoup
import csv

URL = "https://weather.com/en-IN/weather/today/l/509b04e24f3c30c98dd3588d6682e0594fb4f10527ce0f19b38236f3580cb767"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html5lib')


table = soup.find('div', attrs={'class': 'today-daypart-temp'})
#table = soup.find('span')

for row in table:
    print("Temp of Kullu Today: "+str(row)[15:17]+" C")
