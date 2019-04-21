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

def scrape_se(url, category, filename = "data/super_express.csv", sites = 1000):
    print('Scraping "Super Express", kategoria: {}, ilość stron:{}'.format(category, sites))
    for i in tqdm(range(sites)):
        try:
            if i%10 == 0:
                time.sleep(10)
            page = requests.get(url + str(i))
            page = page.text
            soup = BeautifulSoup(page, 'html.parser')
            #get page with BS

            soup = soup.find_all("div", {"class":"element__headline"})
            names = []
            for s in soup:
                names.append(clean(s.text))

            names = names[:8]

            for i in range(len(names)):
                with(open(filename, 'a', encoding = 'utf-8')) as file:
                    writer = csv.writer(file,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                    writer.writerow([names[i], category, "0"])

        except Exception as e:
            with open("errors.txt", 'a', encoding = 'utf-8') as efile:
                efile.write("SuperExpress:\nError on page {}, skipping. \n".format(i))
                efile.write(str(e) + "\n\n\n")
                continue
