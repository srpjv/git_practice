valeur = int(input("Vous voulez check quelle année : "))
if valeur % 4 == 0 or valeur % 100 == 0 or  valeur % 400 == 0:
    print("Cette année est bissextile")
else:
    print("Cette année n'est pas bessextile")
