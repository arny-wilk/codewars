import numpy as np

def addition_matrices(matrice_a, matrice_b):
    try:
        vec_a = np.array(matrice_a)
        vec_b = np.array(matrice_b)
        vec_add= vec_a + vec_b
        new_list = vec_add.tolist()
        return new_list
    except ValueError as v:
        print(f"Erreure de type: {v}")



matrice_a = [[1, 2, 3], [3, 7, 3]]
matrice_b = [[6, 4, 2], [3, 1, 0]]

print(addition_matrices(matrice_a, matrice_b))

