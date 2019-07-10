import csv
import statistics as st
import matplotlib.pyplot as plt

file = "./data/all_data.csv"

data = {}

with open(file, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        data[row['Title']] = row['Category']

print(len(data))
i = 0

counter = {}

for key, value in data.items():
    if value in counter:
        counter[value] += 1
    else:
        counter[value] = 0

sorted_counter = sorted(counter.items(), key=lambda kv: kv[1])

categories = []
no_of_articles = []
indexes = []
index = 0
for i in sorted_counter:
    categories.append(i[0])
    no_of_articles.append(i[1])
    indexes.append(index)
    index += 1
    

"""plt.barh(categories, no_of_articles)
plt.yticks(indexes, categories)
plt.show()"""

num_data = []

for key, value in data.items():
    num_data.append((len(key), value))

new_data = {}

for item in num_data:
    if item[1] in new_data:
        new_data[item[1]][0] += item[0]
        new_data[item[1]][1] += 1
    else:
        new_data[item[1]] = [item[0], 1]

mean_data = {}
for key, value in new_data.items():
    mean_data[key] = (round(value[0]/value[1], 2))

sorted_mean = sorted(mean_data.items(), key=lambda kv: kv[1])

print(sorted_mean)
categories = []
means = []
indexes = []
index = 0
for item in sorted_mean:
    categories.append(item[0])
    means.append(item[1])
    indexes.append(index)
    index += 1

plt.barh(categories, means)
plt.yticks(indexes, categories)
plt.show()