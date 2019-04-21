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

def scrape_og(url, category, filename = "data/obserwator_gospodarczy.csv", sites = 100):
    print('Scraping "Obserwator Gospodarczy", kategoria: {}, ilość stron: {}\n'.format(category, sites))
    for i in tqdm(range(1, sites)):
        try:
            if i == 1:
                page = requests.get(url + str(i))
            else:
                page = requests.get(url + str((i-1)*6))
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')

            soup = soup.find_all("div", {"class" : 't3-content'})[0]

            soup = soup.find_all("h3")
            names = []
            for s in soup:
                names.append(clean(s.text))

            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, "0"])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("Obserwator Gospodarczy:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue
