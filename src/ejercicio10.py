def inicializar_estadisticas(participantes):
    estadisticas = {}

    for nombre in participantes:
        estadisticas[nombre] = {
            "total": 0,
            "rondas_ganadas": 0,
            "mejor_ronda": 0,
            "rondas_jugadas": 0
        }

    return estadisticas

def calcular_puntaje_ronda(puntajes_jueces):
    return puntajes_jueces["judge_1"] + puntajes_jueces["judge_2"] + puntajes_jueces["judge_3"]

def procesar_ronda(ronda, estadisticas):
    resultados_ronda = {}

    for participante in ronda["scores"]:
        puntaje = calcular_puntaje_ronda(ronda["scores"][participante])
        resultados_ronda[participante] = puntaje

        estadisticas[participante]["total"] += puntaje
        estadisticas[participante]["rondas_jugadas"] += 1

        if puntaje > estadisticas[participante]["mejor_ronda"]:
            estadisticas[participante]["mejor_ronda"] = puntaje

    # Buscar ganador de la ronda
    ganador = max(resultados_ronda, key=resultados_ronda.get)
    estadisticas[ganador]["rondas_ganadas"] += 1

    return resultados_ronda, ganador

def obtener_tabla_ordenada(estadisticas):
    tabla = []

    for participante in estadisticas:
        total = estadisticas[participante]["total"]
        rondas_ganadas = estadisticas[participante]["rondas_ganadas"]
        mejor_ronda = estadisticas[participante]["mejor_ronda"]
        rondas_jugadas = estadisticas[participante]["rondas_jugadas"]
        promedio = total / rondas_jugadas

        tabla.append({
            "nombre": participante,
            "total": total,
            "rondas_ganadas": rondas_ganadas,
            "mejor_ronda": mejor_ronda,
            "promedio": promedio
        })

    tabla.sort(key=lambda x: x["total"], reverse=True)
    return tabla

def mostrar_tabla(tabla):
    print("Cocinero            Puntaje   Rondas ganadas   Mejor ronda   Promedio")
    
    for fila in tabla:
        print(f'{fila["nombre"]:<20} {fila["total"]:<9} {fila["rondas_ganadas"]:<16} {fila["mejor_ronda"]:<13} {fila["promedio"]:.1f}')

    