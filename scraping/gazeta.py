import requests
from bs4 import BeautifulSoup
import csv
from tqdm import tqdm
import time


def scrape_gazeta(url, category, filename = "./data/gazeta.csv", sites = 450):
    print('Scraping "gazeta.pl", kategoria: {}, ilość stron: {}'.format(category, sites))
    for i in tqdm(range(1, sites)):
        try:
            if i%10 == 0:
                time.sleep(5)

            page = requests.get(url + str(i) + "_19834947")
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')

            soup = soup.find_all("h2")
            names = []
            for s in soup:
                names.append(s.text)

            if len(names) == 0:
                print("End of articles reached")
                break

            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, 0])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("Gazeta.pl:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue
