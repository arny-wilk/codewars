liste_en_bazar = [14, 2.21, ["docstring", 74, "cactus", {"chien": 8}], 74, (12, [47, 7.3])]
autre_liste = [2.3, (7, [[4, (9)], "test"]), 5]


def compteur_profondeur(liste):
    if isinstance(liste, (int, float)):
        return 1
    elif isinstance(liste, (tuple, list)):
        return sum([compteur_profondeur(element) for element in liste])
    return 0


print(compteur_profondeur(liste_en_bazar))
print(compteur_profondeur(autre_liste))



