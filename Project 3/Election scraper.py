# Election Scraper - JR

import time
import csv
import requests
from bs4 import BeautifulSoup as bs


start = time.time()


def muni_data_f(url):
    source = requests.get(url)
    soup = bs(source.text, 'html.parser')

    muni_data_info = {}

    muni_data_info["registered"] = soup.find('td', headers='sa2').text
    muni_data_info["envelopes"] = soup.find('td', headers='sa5').text
    muni_data_info["valid"] = soup.find('td', headers='sa6').text

    return muni_data_info


def poli_parties(url):
    poli_url = url
    source = requests.get(poli_url)
    soup = bs(source.text, 'html.parser')
    poli_names_list = []
    poli_names_count = []
    poli_dict = {}

    for i in range(1, 3):
        poli_names = soup.find_all('td', headers=f't{i}sa1 t{i}sb2')
        for poli_name in poli_names:
            poli_names_list.append(poli_name.text)

    for i in range(1, 3):
        poli_counts = soup.find_all('td', headers=f't{i}sa2 t{i}sb3')
        for poli_count in poli_counts:
            poli_hodnota = poli_count.text
            poli_hodnota = poli_hodnota.replace(u'\xa0','')

            poli_names_count.append(poli_hodnota)

    for i in range(len(poli_names_list)):
        poli_dict[poli_names_list[i]] = poli_names_count[i]

    poli_dict.pop('-', None)

    return poli_dict


def hlavicka():
    poli_url = 'https://volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=1'
    source = requests.get(poli_url)
    soup = bs(source.text, 'html.parser')

    poli_names_list = []
    poli_dict_hlavicka = {}

    for i in range(1,3):
        poli_names = soup.find_all('td', headers=f't{i}sa1 t{i}sb2')
        for poli_name in poli_names:
            poli_names_list.append(poli_name.text)

    for i in range(len(poli_names_list)):
        poli_dict_hlavicka[poli_names_list[i]] = 0

    poli_dict_hlavicka['Česká národní fronta'] = 0
    poli_dict_hlavicka['Národ Sobě'] = 0

    poli_dict_hlavicka.pop('-')

    return poli_dict_hlavicka


URL = "https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ"
URL2 = 'https://volby.cz/pls/ps2017nss/'

muni_list = []

raw_html = requests.get(URL)
parsed_soup = bs(raw_html.text, 'html.parser')
tables = parsed_soup.find_all('table') #[1:]

for table in tables:
    municipal_rows = table.find_all("tr")[2:]

    for row in municipal_rows:
        if row.find("td").text == "-":
            continue

        muni_data = {"code": "", "name": "", "registered": 0,
                     "envelopes": 0, "valid": 0}

        muni_data.update(hlavicka())

        muni_url = f"{URL2}{row.find('a')['href']}"

        muni_data["code"] = row.find("a").text
        muni_data["name"] = row.a.findNext("td").text

        muni_data.update(poli_parties(muni_url))
        muni_data.update(muni_data_f(muni_url))

        muni_list.append(muni_data)


        with open('MUNICIPAL.csv', mode='w') as csv_file:
            zahlavi = muni_data.keys()
            zapis = csv.DictWriter(csv_file, fieldnames=zahlavi)

            zapis.writeheader()
            for line in muni_list:
                zapis.writerow(line)


elapsed = time.time() - start
print(f"ELAPSED TIME: {elapsed}")
