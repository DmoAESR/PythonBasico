def validar_parentesis(cadena) -> bool:
    parentesis_counter = 0
    for elemento in cadena:
        if elemento == "(":
            parentesis_counter += 1
        if elemento == ")":
            parentesis_counter -= 1
        if parentesis_counter < 0:
            return False
    
    if parentesis_counter == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print(validar_parentesis("()"))
    print(validar_parentesis(")()"))
    print(validar_parentesis("(())"))
    print(validar_parentesis("(())(()()())"))
    print(validar_parentesis("(c)(a)(()b)"))


def validar_parentesis(cadena) -> bool:
    parentesis_counter = 0
    for elemento in cadena:
        if elemento == "(":
            parentesis_counter += 1
        if elemento == ")":
            parentesis_counter -= 1
        if parentesis_counter < 0:
            return False
    
    return not parentesis_counter


if __name__ == "__main__":
    print(validar_parentesis("()"))
    print(validar_parentesis(")()"))
    print(validar_parentesis("(())"))
    print(validar_parentesis("(())(()()())"))
    print(validar_parentesis("(c)(a)(()b)"))

