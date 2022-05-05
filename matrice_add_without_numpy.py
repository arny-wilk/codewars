

matrice_a = [[1, 2, 3], [3, 7, 3]]
matrice_b = [[6, 4, 2], [3, 1, 0]]
matrice_c = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

result = [[0, 0, 0], [0, 0, 0]]

def addition_matrice(a, b):
# iterate through rows
    try:
        for i in range(len(a)):
            # iterate through columns
            for j in range(len(b[0])):
                result[i][j] = a[i][j] + b[i][j]

        return result

    except ValueError:
        raise ValueError("ValueError exception thrown")

print(addition_matrice(matrice_a, matrice_b))
print(addition_matrice(matrice_a, matrice_c))
