def cifrar_cesar(mensaje, desplazamiento):
    resultado = ""

    for caracter in mensaje:
        if caracter.isalpha():
            if caracter.islower():
                base = ord('a')
            else:
                base = ord('A')

            nueva_letra = chr((ord(caracter) - base + desplazamiento) % 26 + base)
            resultado += nueva_letra
        else:
            resultado += caracter

    return resultado


def descifrar_cesar(mensaje, desplazamiento):
    return cifrar_cesar(mensaje, -desplazamiento)