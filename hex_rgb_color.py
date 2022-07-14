code_couleur = "#FF00FF"

def hex_to_rgb(value):
    rouge = int(value[1:3], 16)
    vert = int(value[3:5], 16)
    bleu = int(value[5:7], 16)

    return rouge, vert, bleu

print(hex_to_rgb(code_couleur))

