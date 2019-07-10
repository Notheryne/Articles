import csv

"""
Check if there are any duplicates.

"""
interia_data = "data/interia.csv"
gazeta_data = "data/gazeta.csv"
og_data = "data/obserwator_gospodarczy.csv"
se_data = "data/super_express.csv"
wyborcza_data = "data/wyborcza.csv"
files = [interia_data, gazeta_data, og_data, se_data, wyborcza_data]
data = []
for file in files:
    with open(file, 'r', encoding="utf-8") as rfile:
        reader = csv.DictReader(rfile, delimiter = ',', quotechar='"')
        for row in reader:
            data.append(row['Title'])

print(len(data))
nodup = []
dup = []
for i in data:
    if i in nodup:
        dup.append(i)
    else:
        nodup.append(i)

print(len(nodup))
print(len(dup))
print(dup)
with open("duplicates.txt", 'w', encoding="utf-8") as wfile:
    for i in dup:
        wfile.write(i + "\n")
