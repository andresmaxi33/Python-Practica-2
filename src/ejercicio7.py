import random

def obtener_participantes(entrada):
    nombres = entrada.split(",")
    participantes = []
    
    for nombre in nombres:
        limpio = nombre.strip()
        participantes.append(limpio)
    
    return participantes

def validar_participantes(participantes):
    if len(participantes) < 3:
        return False

    # Normalizar (minusculas) para comparar
    normalizados = []
    for nombre in participantes:
        normalizados.append(nombre.lower())

    # Ver duplicados
    if len(normalizados) != len(set(normalizados)):
        return False

    return True


def sortear_amigos(participantes):
    while True:
        mezclados = participantes.copy()
        random.shuffle(mezclados)

        valido = True
        for i in range(len(participantes)):
            if participantes[i] == mezclados[i]:
                valido = False
                break

        if valido:
            return mezclados