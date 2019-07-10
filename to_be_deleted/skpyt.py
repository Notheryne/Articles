
import csv
from sklearn import preprocessing
from sklearn.naive_bayes import ComplementNB
from tqdm import tqdm
import numpy as np
le = preprocessing.LabelEncoder()

articles = {}
filename = 'data/all_data_num.csv'
"""with open(filename, 'r', encoding="utf-8") as rfile:
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
titles_encoded = []
for title in titles:
    arr_titles = []
    for word in title:
        arr_titles.append(le.fit_transform(word))
    titles_encoded.append(np.array(arr_titles))
titles_encoded= np.array(titles_encoded)

titles_encoded = ([le.fit_transform(word) for word in [title for title in titles]]
categories_encoded = (le.fit_transform(categories)
"""
#print(titles_encoded, categories_encoded)
data = []
with open(filename, 'r', encoding='utf-8') as rfile:
    reader = csv.reader(rfile, delimiter = ",")
    for row in reader:
        if row != []:
            data.append(row)

titles = [i[:-1] for i in data]
categories = [i[-1] for i in data]
titless = []
for i in titles:
    temp = []
    for j in i:
        temp.append(int(j))
    titless.append(temp)
titles = titless
categories = [int(i) for i in categories]

print(titles[:10])

titles_padded = []
for title in titles:
    temp = title
    while len(temp) != 26:
        temp.append(-1)
    titles_padded.append(temp)


titles_arr = np.array([np.array(title) for title in titles_padded])
model = ComplementNB()

print(model.fit(titles_arr, categories).predict(titles_arr))
#x = [61,62,63,64,10,65,66,67,68,69,70,71,72,73,74]
#while len(x) < 26:
    #x.append(-1)

#print(model.predict([x]))
print(model.score(titles_arr, categories))
