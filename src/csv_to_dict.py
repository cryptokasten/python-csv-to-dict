import json
import csv

f = open("data/input.csv", "rt")
reader = csv.reader(f)

doc = {}
for row in reader:
    key, value = row[0], row[1]
    doc[key] = value

f = open("data/output.json", "wt")
f.write(json.dumps(doc, indent=4))
f.close()
