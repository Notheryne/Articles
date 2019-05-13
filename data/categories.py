import csv

categories = []
filename = 'all_data.csv'
with open(filename, 'r', encoding="utf-8") as rfile:
    reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
    for row in reader:
        if row["Category"] not in categories:
            categories.append(row["Category"])
        else:
            pass

print(categories)
