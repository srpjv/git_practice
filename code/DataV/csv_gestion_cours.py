#output = open("feuille1.csv", "w", newline = '')
writer = csv.writer(outout)
writer.writerow(["spam", "spam", "spam"])
#Contenu à
writer.writerow(["Babar", "Carlota", "Python", "Test"])
output.close()

#Lire avec une boucle for

example = open("feuille1")
reader = csv.reader(example)

for ro in reader:
    print("Ligne numéro" + str(reader.line_num) + '' + str (row))


#Délimiteur et fin de ligne

writer = csv.writer(output, delimiter ="\t", lineterminator = "")

#Projet
#Retirer l'en-tête des fichiers csv

#Créer une boucle pour parcourir le fichier
#Créer un nouveau dossier

# Passer les fihciers qui ne sont pas des csv

#Lire le fichier
# Passer la première ligne
#Ecrire le nouveau fichier sans l'en-tête


