def PromedioMayores(lista: list) -> float:
    lista.sort()
    ultimos_tres = lista[-3:]
    return sum(ultimos_tres)/len(ultimos_tres)

mi_lista = [8, 5, 7, 6, 11, 99]

print(str(PromedioMayores(mi_lista)))