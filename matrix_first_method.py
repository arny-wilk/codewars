def addition_matrices(matrice_a: list, matrice_b: list) -> list:
    hauteur_matrice_a = len(matrice_a)
    hauteur_matrice_b = len(matrice_b)
    longueur_matrice_a = len(matrice_a[0])
    longueur_matrice_b = len(matrice_b[0])
    if hauteur_matrice_a == hauteur_matrice_b and longueur_matrice_a == longueur_matrice_b :
        matrice_resultat = []
        for index_ligne in range(hauteur_matrice_b):
            ligne = []
            for index_colonne in range(longueur_matrice_b):
                ligne.append(matrice_a[hauteur][longueur] + matrice_b[hauteur][longueur])
            matrice_resultat.append(ligne)
        return matrice_resultat
    else :
        raise ValueError
