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

nodup_categories = list(dict.fromkeys(categories))
categories_ids = {}
tokenized_categories = []
for i in range(len(nodup_categories)):
    categories_ids[nodup_categories[i]] = i

for category in categories:
    tokenized_categories.append(categories_ids[category])

titles_str = ' '.join(titles)
words = titles_str.split(' ')
words = list(dict.fromkeys(words))
words_ids = {}

for i in range(len(words)):
    words_ids[words[i]] = i

tokenized_titles = []

for title in titles:
    tokenized_title = []
    tmp = title.split(" ")
    for word in tmp:
        tokenized_title.append(int(words_ids[word]))
    tokenized_titles.append(tokenized_title)

"""for i in range(10):
    print(titles[i])
    print(tokenized_titles[i])
"""
tokenized_articles = []

for i in range(len(tokenized_titles)):
    tokenized_titles[i].append(int(tokenized_categories[i]))

#for i in range(len(tokenized_titles)):
    #tokenized_articles[tokenized_titles[i]] = tokenized_categories[i]

#print(tokenized_articles)

#for i in range(len(tokeni))

with open(filename2, 'a', encoding='utf-8') as wfile:
    writer = csv.writer(wfile,delimiter=',')
    for token in tokenized_titles:
        #writer.writerow([key, value])
        writer.writerow(token)
