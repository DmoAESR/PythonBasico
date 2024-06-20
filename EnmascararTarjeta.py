# tarjeta_credito ("4556364607935616") == "************5616"
# tarjeta_credito ("64607935616") == "*******5616"
# tarjeta_credito ("1") == "1"

def tarjeta_credito(numero_tarjeta):
    valor_escondido = ""
    for index in range(0, len(numero_tarjeta)-4):
        valor_escondido += "*"

    valor_escondido += numero_tarjeta[-4:]
    return valor_escondido

print(tarjeta_credito("4556364607935616"))


def tarjeta_credito(numero_tarjeta):
    return "*" * (len(numero_tarjeta) - 4) + numero_tarjeta[-4:]

print(tarjeta_credito("64607935617"))