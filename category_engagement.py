import csv
import statistics as st
import matplotlib.pyplot as plt

articles = {}
filename = 'data/trojmiasto.csv'

with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        if row['Category'] in articles:
            articles[row['Category']].append(int(row['Opinions']))
        else:
            articles[row['Category']] = [int(row['Opinions'])]

opinions_mean = []
for k, v in articles.items():
    articles[k] = int(round(st.mean(v), 0))

sorted = sorted(articles.items(), key=lambda kv: kv[1])

categories = []
opinions = []

for i in sorted:
    categories.append(i[0])
    opinions.append(i[1])
indexes = [i for i in range(len(categories))]

plt.barh(indexes, opinions)
plt.yticks(indexes, categories)
plt.show()
