liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]

nom_a_chercher = "Julie"
nouveau_nom = "Julien"

liste = [ liste[i].replace(nom_a_chercher, nouveau_nom) for i in range(len(liste))]

print(liste)


