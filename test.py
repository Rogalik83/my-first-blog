annee = input("veuillez saisir l'année : ")
annee = int(annee)
bissextile = False
if annee % 400 == 0:
    bissextile = True
elif annee % 100 == 0:
    bissextile = False
elif annee % 4 == 0:
    bissextile = True
else:
    bissextile = False
if bissextile:
    print("L'année saisie est bissextile")
else:
    print("L'année saisie n'est pas bissextile")



"""variante 2
annee = input("veuillez saisir l'année : ")
annee = int(annee)
bissextile = False
if annee % 400 == 0 or (annee % 4 == 0 and annee % 100 == 0):
    print("L'année saisie est bissextile")
else:
    print ("L'année saisie n'est pas bissextile")"""
