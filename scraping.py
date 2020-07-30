import requests
from bs4 import BeautifulSoup
from datetime import datetime

response = requests.get('http://www.hidmet.gov.rs')
scraper = BeautifulSoup(response.text, 'html.parser')
gradovi = scraper.findAll('div', {"class": "osmotreni"})

print("Danas je:", datetime.today().strftime('%Y-%m-%d-%H:%M:%S'))
print("Izmerene temperature po gradovima:")
for grad in gradovi:
    img = grad.find('img', alt=True)
    print(img['alt'])