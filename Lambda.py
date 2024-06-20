if __name__ == "__main__":
    local_variable = 0

    multiplicacion = lambda a,b: a*b
    print(multiplicacion(5,5))
    resultado = multiplicacion(8, 8)
    print(resultado)

    suma_diez = lambda a: a + 10
    print(suma_diez(5))

    lista_nombres = ["Arturo Lopez", "Raul Jimenez", "Pancho Perez"]
    lista_nombres.sort()
    print(lista_nombres)

    lista_nombres.sort(key = lambda nombre:nombre.split(" ")[1])
    print(lista_nombres)
    
    lista_nombres.append("Ricardo Luis Arreola")
    print(lista_nombres)
    
    lista_nombres.sort(key = lambda nombre:nombre.split(" ")[-1])
    print(lista_nombres)