# diferencia_listas([1,2],[1]) -> [2]
# diferencia_listas([1,2,3],[2,5,3]) -> [1]

def diferencias_listas(lista_origen, lista_resta):
    for elemento_b in lista_resta:
        while elemento_b in lista_origen:
            lista_origen.remove(elemento_b)
    return lista_origen

a = [1,2,3]
b = [2,5,3]

print(diferencias_listas(a,b))

def diferencias_listas(lista_origen, lista_resta):
    lista_return = []
    for elemento in lista_origen:
        if elemento not in lista_resta:
            lista_return.append(elemento)
    return lista_return


print(diferencias_listas(a,b))


def diferencias_listas(lista_origen, lista_resta):
    return [x for x in lista_origen if x not in lista_resta]

print(diferencias_listas(a,b))