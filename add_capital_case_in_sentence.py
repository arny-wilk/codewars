texte = "le but de cet exercice est de modifier le texte que vous êtes en train de lire. vous devez en effet manipuler la chaîne de caractères actuelle pour rajouter les majuscules au début de chaque phrase. pour cela vous devez utiliser plusieurs méthodes disponibles sur les chaînes de caractères. si vous avez besoin d'aide, affichez l'aide en cliquant sur le bouton à gauche à la fin de l'énoncé."

liste = texte.split('. ')
new_liste = [ ele.capitalize() for ele in liste ]

print('. '.join(new_liste))
