# letra_faltante(['a','b','c','d','f']) -> e
# letra_faltante(['O','Q','R','S']) -> P

def letra_faltante(lista_letras):
    indice = 0
    while ord(lista_letras[indice]) + 1 == ord(lista_letras[indice + 1]):
        indice += 1
    return chr(ord(lista_letras[indice]) + 1)

lista_letras = ['a','b','c','d','f']

print(letra_faltante(lista_letras))
