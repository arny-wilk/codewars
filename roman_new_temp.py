def conversion_romain_entier(nombre_romain: str) -> int:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    result = 0
    higher_number = 0
    nombre_romain = nombre_romain[::-1]

    for num in nombre_romain:
        value = roman.get(num)
        if value < higher_number:
            result -= value
        else:
            result += value
            higher_number = value
    return result



print(conversion_romain_entier('X'))
print(conversion_romain_entier('XV'))
print(conversion_romain_entier('III'))
print(conversion_romain_entier('CDIII'))
print(conversion_romain_entier('MMMCIX'))
print(conversion_romain_entier('XCV'))
print(conversion_romain_entier('CXLIX'))
