lista = [1,2,3,4]

print(lista[0])

lista[1] = 5

print(lista[1])

print(len(lista))
print(max(lista))
print(min(lista))

lista.append("h")
print(lista)

# print(max(lista))

lista.remove("h")
lista.sort()
print(lista)

tuple_ = (1,"hola",7,"adios")
# tuple_.append(2)
print(tuple_)

set_ = {"hola",3,"mundo",3}
print(set_)

set_.add(8)
set_.discard("hola")
print(set_)