variable1 = 3
variable2 = 2

# Operadores Aritmeticos
print("suma: " + str(variable1 + variable2))
print("resta: " + str(variable1 + variable2))
print("multiplicacion: " + str(variable1 + variable2))
print("division: " + str(variable1 + variable2))


print("residuo: " + str(variable1 % variable2))
print("exponente: " + str(variable1 ** variable2))
print("floor div: " + str(variable1 // variable2))
print("floor div: " + str(8 // 3))

# Operadores Logicos
# 3 = 0011
# 2 = 0010
print("and:" + str(variable1 & variable2))
print("or:" + str(variable1 | variable2))
print("not:" + str(~variable1))
print("xor:" + str(variable1 ^ variable2))

print("corrimiento izq:" + str(variable1 << 1))
print("corrimiento der:" + str(variable1 >> 1))

# Operadores comparacion
print("mayor que: " + str(variable1 >= variable2))
print("menor que: " + str(variable1 <= variable2))
print("igual que: " + str(variable1 == variable2))
print("distinto que: " + str(variable1 != variable2))

# Operadores membresia
cadena = "hola"
if 'o' in cadena and 'z' in cadena:
    print("si esta")
else:
    print("no esta")


if 'o' in cadena or 'z' in cadena:
    print("si esta")
else:
    print("no esta")

if not('o' in cadena or 'z' in cadena):
    print("si esta")
else:
    print("no esta")