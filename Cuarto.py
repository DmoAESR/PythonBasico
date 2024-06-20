def cuarto(mes: int) -> int:
    return ((mes + 2) // 3)

print(cuarto(1)) # -> 1
print(cuarto(3)) # -> 1
print(cuarto(6)) # -> 2
print(cuarto(8)) # -> 3
print(cuarto(11)) # -> 4
print(cuarto(12)) # -> 4