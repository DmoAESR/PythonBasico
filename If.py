variable = 10

if variable:
    print("Es distinto de 0")

if variable > 20:
    print("Es verdadero")
else:
    print("Es falso")

variable = 3

if variable == 1:
    print("La variable es 1")
elif variable == 2:
    print("La variable es 2")
elif variable == 3:
    print("La variable es 3")
else:
    print("La variable tiene otro valor")

cadena1 = "Hola"
cadena2 = "hola"

if cadena1.lower() == cadena2.lower():
    print("Las cadenas son iguales")


variable = 10

while variable:
    print("El valor es: " + str(variable))
    variable -= 1