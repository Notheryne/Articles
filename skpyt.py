
import csv
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from tqdm import tqdm
import numpy as np
le = preprocessing.LabelEncoder()

articles = {}
filename = 'data/all_data.csv'
with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        title = row['Title']
        category = row['Category']
        articles[title] = category

titles = []
categories = []
for key,value in articles.items():
    words = key.split(" ")
    titles.append(words)
    categories.append(value)

'''titles_encoded = []
for title in titles:
    titles_encoded.append(le.fit_transform(title))'''
"""titles_encoded = []
for title in titles:
    arr_titles = []
    for word in title:
        arr_titles.append(le.fit_transform(word))
    titles_encoded.append(np.array(arr_titles))
titles_encoded= np.array(titles_encoded)"""

titles_encoded = ([le.fit_transform(word) for word in [title for title in titles]]
categories_encoded = (le.fit_transform(categories)

#print(titles_encoded, categories_encoded)

print(titles_encoded[0],categories_encoded[0])
#print(features)

model = GaussianNB()

model.fit(titles_encoded, categories_encoded)
