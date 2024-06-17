def multiplicar(a, b):
    print("Estas ejecutando la multipliacion")
    c = a * b
    return c

resultado = multiplicar(7,7)
print(resultado)

def compararNumeros(num1: int, num2: int) -> None:
    if type(num1) is not int or type(num2) is not int:
        raise Exception("No son 2 enteros")
    
    if num1 > num2:
        print("El primer valor es mayor")
    elif num1 < num2:
        print("El segundo valor es mayor")
    else:
        print("Es igual")

compararNumeros("5", 8)