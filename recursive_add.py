def additive(num):
    if num == 0:
        return 0
    else :
        return num + additive(num - 1)

def temp_additive(num):
    result = [i for i in range(num+1)]
    result = sum(result)
    return result

resultat = additive(10)
print(resultat)
