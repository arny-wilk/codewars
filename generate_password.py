import string
import random

letters = string.ascii_letters + string.digits + string.punctuation

taille = 8

password = ''.join(random.choice(letters) for _ in range(taille))
print(password)

