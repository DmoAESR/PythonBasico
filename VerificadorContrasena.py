# Símbolos: (espacio) ! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _` { | } ~ (33 caracteres)
def alphanumeric(contrasena: str) -> bool:
    return contrasena.isalnum()

print(alphanumeric("hellos world_")) # -> False
print(alphanumeric("Passw0rd")) # -> True
print(alphanumeric("       ")) # -> False
print(alphanumeric("___ * ____")) # -> False
print(alphanumeric("&)))((()))")) # -> False
print(alphanumeric("43534h56jmTHHF3k")) # -> True
print(alphanumeric("")) # -> False



def alphanumeric(contrasena: str) -> bool:
    if not contrasena:
        return False
    for caracter in contrasena:
        caracter = ord(caracter)
        if not (32 <= caracter <= 126):
            return False
    return True

print(alphanumeric("hellos world_")) # -> False
print(alphanumeric("Passw0rd")) # -> True
print(alphanumeric("       ")) # -> False
print(alphanumeric("___ * ____")) # -> False
print(alphanumeric("&)))((()))")) # -> False
print(alphanumeric("43534h56jmTHHF3k")) # -> True
print(alphanumeric("")) # -> False