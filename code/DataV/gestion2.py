import csv
import pandas as pd

with open('Feuille2.csv') as f:
    reader = csv.reader(f)
    data = list(reader)

#print(data)

#lignes_ordonnees = sorted(data, key=lambda test: test[2])

for i in data:
    print(i)
    print(i[1][2])

#print(lignes_ordonnees)
#print(name)
#name = data[1]

#df = pd.read_csv(data)
#df1 = df.sort_values(by='', ascending=True)
#print(df1)