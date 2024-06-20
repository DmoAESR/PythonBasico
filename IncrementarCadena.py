def incremento_cadena(cadena: str):
    cadena_separada = ["", ""]
    for elemento in cadena:
        if elemento.isdigit():
            cadena_separada[1] += elemento
        else:
            cadena_separada[0] += elemento
    
    if not cadena_separada[1]:
        cadena_separada[1] = "1"
    else:
        cadena_separada[1] = str(int(cadena_separada[1]) + 1).zfill(len(cadena_separada[1]))
    return "".join(cadena_separada)


print(incremento_cadena("hola5")) # -> hola6
print(incremento_cadena("hola")) # -> hola1
print(incremento_cadena("hola000")) # -> hola001
print(incremento_cadena("hola010")) # -> hola011
print(incremento_cadena("hola099")) # -> hola100
print(incremento_cadena("hola99")) # -> hola100