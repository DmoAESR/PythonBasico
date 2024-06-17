def multiplicar(a, b):
    print("Estas ejecutando la multipliacion")
    c = a * b
    return c

variable_global = 10

if __name__ == "__main__":
    variable1 = 10
    print ("Se ejecuta dentro de inicio.py, pero no al invocar la función multiplicar")
else:
    print ("Se ejecuta el invocar multiplicar en otro .py")