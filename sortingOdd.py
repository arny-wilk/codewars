a = [5, 3, 2, 8, 1, 4]
b = sorted([item for item in a if item%2 != 0])
odd_int = 0
for i in range(len(a)):
    if a[i] %2 != 0:
        a[i] = b[odd_int]
        odd_int += 1
print(a)
