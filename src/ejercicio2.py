def duracion_a_segundos(duracion):
    partes = duracion.split(":")
    minutos = int(partes[0])
    segundos = int(partes[1])
    return minutos * 60 + segundos


def segundos_a_minutos_segundos(total_segundos):
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return minutos, segundos


def duracion_total(playlist):
    total = 0
    for cancion in playlist:
        total += duracion_a_segundos(cancion["duration"])
    return total


def cancion_mas_larga(playlist):
    mas_larga = playlist[0]
    
    for cancion in playlist:
        if duracion_a_segundos(cancion["duration"]) > duracion_a_segundos(mas_larga["duration"]):
            mas_larga = cancion
            
    return mas_larga


def cancion_mas_corta(playlist):
    mas_corta = playlist[0]
    
    for cancion in playlist:
        if duracion_a_segundos(cancion["duration"]) < duracion_a_segundos(mas_corta["duration"]):
            mas_corta = cancion
            
    return mas_corta