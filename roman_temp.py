def conversion_romain_entier(nombre_romain):

    roman = {'I': 1, 'II': 2, 'III': 3, 'V': 5, 'X': 10, 'L': 50 ,'C': 100, 'D': 500, 'M': 1000}

    result = 0
    plus_grande_valeur = 0
    nombre_romain = nombre_romain[::-1]
    for symbole in nombre_romain:
        valeur_symbole = roman.get(symbole)
        if valeur_symbole < plus_grande_valeur:
            result -= valeur_symbole
        else :
            result += valeur_symbole
            plus_grande_valeur = valeur_symbole
    return result



print(conversion_romain_entier('MMMM'))
print(conversion_romain_entier('MMM'))
print(conversion_romain_entier('CDXLIII'))
print(conversion_romain_entier('MMMCMLXXXVI'))
print(conversion_romain_entier('MDXI'))
print(conversion_romain_entier('CXLIX'))
