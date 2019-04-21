import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time

def clean(string):
    string = string.replace("\n", "")
    string = string.replace("\r", "")
    string = string.replace("\t", "")
    string = string.strip(" ")
    return string

def scrape_interia_biznes(url, category, filename = "data/interia.csv", sites = 600):
    print('Scraping "Interia biznes", kategoria: {}, ilość stron: {}'.format(category, sites))
    for i in tqdm(range(1, sites)):
        try:
            if i%10 == 0:
                time.sleep(5)
            page = requests.get(url + str(i))
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')

            soup = soup.find_all("strong")
            names = []

            for s in soup:
                names.append(clean(s.text))

            names = names[:9]
            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, 0])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("Interia biznes:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue

def scrape_interia(url, category, filename = "data/interia.csv", sites = 600):
    print('Scraping "Interia", kategoria: {}, ilość stron: {}'.format(category, sites))
    for i in tqdm(range(1, sites)):
        try:
            if i%10 == 0:
                time.sleep(5)
            page = requests.get(url + str(i))
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')

            soup = soup.find_all("h2")
            names = []

            for s in soup:
                names.append(clean(s.text))

            names = names[1:-1]

            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, 0])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("Interia:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue
