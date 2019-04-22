import csv

interia_data = "data/interia.csv"
gazeta_data = "data/gazeta.csv"
og_data = "data/obserwator_gospodarczy.csv"
se_data = "data/super_express.csv"
wyborcza_data = "data/wyborcza.csv"

data = []
with open(interia_data, 'r', encoding="utf-8") as rfile:
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
