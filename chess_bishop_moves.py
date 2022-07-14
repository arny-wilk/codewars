# Pyhton 3 program to solve

# number of rows = 8
# number of columns = 8


def deplacements_fou(position_intiale: tuple):
    position_intiale[0].upper()
    if not "A" <= position_intiale[0] <= "H" or not 1 <= position_intiale[1] <= 8:
        raise ValueError

    deplacements_diagonale = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    resultat = []
    for diagonale in deplacements_diagonale:
        position_temporaire =list(position_intiale)
        while "A" <= position_temporaire[0] <= "H" and 1 <= position_temporaire[1] <= 8:
            if tuple(position_temporaire) != position_intiale:
                resultat.append(tuple(position_temporaire))
            position_temporaire[0] = chr(ord(position_temporaire[0]) + diagonale[0])
            position_temporaire[1] += diagonale[1]
    return resultat



print(deplacements_fou(("C", 4)))



