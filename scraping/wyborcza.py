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

def scrape_wyborcza(url, category, filename = './data/wyborcza.csv', sites = 500):
    print('Scraping "Wyborcza", kategoria: {}, ilość stron: {}'.format(category, sites))
    for i in tqdm(range(1, sites)):
        try:
            page = requests.get(url + str(i) + "_23718332")
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')

            soup = soup.find_all("h2")

            names = []
            for s in soup:
                names.append(clean(s.text))

            names = names[:-1]
            if len(names) == 0:
                print("End of articles reached.")
                break
            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, "0"])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("Wyborcza:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue
