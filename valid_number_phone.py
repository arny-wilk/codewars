exemple_numero_telephone = "06-85-42-63-44"

def valid_phone_number(num):
    forma = num.split('-')
    new_list = ''.join(forma)
    if len(forma) == 5 and new_list.isdigit():
        return True
    return False

print(valid_phone_number(exemple_numero_telephone))
