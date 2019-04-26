import csv
import matplotlib.pyplot as plt
import statistics as st
import numpy as np

filename = "data/trojmiasto.csv"

articles = {}

with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        articles[row['Title']] = row['Opinions']

headlines_names = []
for key, value in articles.items():
    headlines_names.append(key)

headlines = []
opinions = []

for key,value in articles.items():
    headlines.append(len(key))
    opinions.append(int(value))

ranges = {}

for key, value in articles.items():
    tmp = len(key) - len(key)%5
    if tmp in ranges:
        ranges[tmp].append(int(value))
    else:
        ranges[tmp] = [int(value)]

ranges_max = []
ranges_medians = []
ranges_devs = []
for key, value in ranges.items():
    ranges_max.append(max(ranges[key]) / st.mean(value))
    ranges_medians.append(st.median(ranges[key]))
    ranges_devs.append(st.stdev(ranges[key]))


for key, value in ranges.items():
    ranges[key] = round(st.mean(value), 3)

w = 1
keys1 = [k - w for k, v in ranges.items()]
keys2 = [k + w for k, v in ranges.items()]
types = ['Mean', 'Std Deviation', 'Median']
plt.bar(keys1, ranges.values(), width=w, color='b')
plt.bar(ranges.keys(), ranges_devs, width=w,color='g')
plt.bar(keys2, ranges_medians, width=w,color='r')
plt.legend(types, loc=2)
#ax.autoscale(tight=True)
plt.show()
