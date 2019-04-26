import csv
import statistics as st
import matplotlib.pyplot as plt
import re

articles = {}
filename = 'data/trojmiasto.csv'

def clean(string):
    new_str = [s for s in string if s.isalnum()]
    new_str = ''.join(new_str)
    new_str = new_str.lower()
    return new_str


with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        fw = row['Title'].split(' ')

        for f in fw:
            f = clean(f)
            if f in articles:
                articles[f].append(int(row['Opinions']))
            else:
                articles[f] = [int(row['Opinions'])]


relevant_articles = {}
for k, v in articles.items():
    if len(v) > 1:
        relevant_articles[k] = v

for k, v in relevant_articles.items():
    relevant_articles[k] = int(round(st.mean(v), 0))

sorted = sorted(relevant_articles.items(), key=lambda kv: kv[1])
#print(sorted)
words = [i[0] for i in sorted]
opinions = [i[1] for i in sorted]
indexes = [i for i in range(len(words))]

max = -30
plt.barh(indexes[max:], opinions[max:])
plt.yticks(indexes[max:], words[max:])
plt.show()
