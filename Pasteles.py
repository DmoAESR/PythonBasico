def pasteles(receta, disponibles):
    lista_ingredientes = []
    for elemento in receta:
        lista_ingredientes.append(disponibles[elemento] // receta[elemento])
    return min(lista_ingredientes)


if __name__ == "__main__":
    receta = {"harina" : 500, "azucar" : 200, "huevos" : 1}
    disponibles = {"harina" : 1200, "azucar" : 1200, "huevos" : 5, "leche" : 200}
    # harina = 2, azucar = 6, huevos = 5
    print(pasteles(receta, disponibles))


def pasteles(receta, disponibles):
    lista_ingredientes = []
    for elemento in receta:
        if elemento not in disponibles.keys():
            return 0
        else:
            lista_ingredientes.append(disponibles[elemento] // receta[elemento])
    return min(lista_ingredientes)


if __name__ == "__main__":
    receta = {"harina" : 500, "azucar" : 200, "huevos" : 1, "manzanas" : 1}
    disponibles = {"harina" : 1200, "azucar" : 1200, "huevos" : 5, "leche" : 200}
    # harina = 2, azucar = 6, huevos = 5
    print(pasteles(receta, disponibles))



def pasteles(receta, disponibles):
    return min(disponibles.get(llave, 0) // receta[llave] for llave in receta)


if __name__ == "__main__":
    receta = {"harina" : 500, "azucar" : 200, "huevos" : 1, "manzanas" : 1}
    disponibles = {"harina" : 1200, "azucar" : 1200, "huevos" : 5, "leche" : 200, "manzanas" : 1}
    # harina = 2, azucar = 6, huevos = 5
    print(pasteles(receta, disponibles))