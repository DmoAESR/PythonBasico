cadena = "Hola Mundo!"

for caracter in cadena:
    print(caracter)

lista = ["hola", "mundo", "!"]

for elemento in lista:
    print(elemento)

for elemento in lista:
    for caracter in elemento:
        print(caracter)

for elemento in reversed(lista):
    print(elemento)


for iterador in range(0,5):
    print(iterador)


inicio = 0
fin = 20
step = 2

for iterador in range(inicio, fin, step):
    print(iterador)