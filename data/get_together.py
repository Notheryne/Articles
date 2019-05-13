import csv

def clean(string):
    new_str = [s for s in string if s.isalnum()]
    new_str = ''.join(new_str)
    return new_str

articles = {}
filenames = ['gazeta.csv',
            'interia.csv',
            'obserwator_gospodarczy.csv',
            'super_express.csv',
            'trojmiasto.csv',
            'wyborcza.csv']
for filename in filenames:
    with open(filename, 'r', encoding="utf-8") as rfile:
        reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
        for row in reader:
            title = row['Title']
            category = row['Category']
            articles[title] = category

filename = "all_data.csv"
filename2 = "all_data_num.csv"
titles = []
categories = []
for key, value in articles.items():
    titles.append(key)
    categories.append(value)

titles = ' '.join(titles)
words = titles.split(' ')
print(len(words))
words = list(dict.fromkeys(words))
print(len(words))

"""
with open(filename2, 'a', encoding='utf-8') as wfile:
    writer = csv.writer(wfile,delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(["Title", "Category"])
    for key, value in articles.items():
        #writer.writerow([key, value])
        words = key.split(" ")
        title_encoded = le.fit_transform(words)
        category_encoded = le.fit_transform([value])
        writer.writerow([title_encoded, category_encoded])"""
