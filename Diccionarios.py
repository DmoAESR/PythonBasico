diccionario = {"elemento1":1,"elemento2":7,10:"cadena"}

diccionario["elemento2"] = 'a'
diccionario[10] = "cadena modificada"

print(diccionario)

del(diccionario["elemento2"])

print(diccionario)

print(diccionario.keys())
print(diccionario.values())