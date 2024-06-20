def generador_hashtag(cadena: str):
    if not cadena or len(cadena) > 140:
        return False
    else:
        lista_palabras = cadena.split()
        return_cadena = ""
        for palabra in lista_palabras:
            return_cadena += palabra.capitalize()
        return '#' + return_cadena
    

if __name__ == "__main__":
    print(generador_hashtag("curso Python!")) #CursoPython!
    print(generador_hashtag("curso Python!          "))
    print(generador_hashtag("")) # False
    print(generador_hashtag("a"*141)) # False
    print(generador_hashtag("a s l g"))
