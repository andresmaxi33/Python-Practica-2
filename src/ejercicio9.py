def nombre_valido(nombre):
    if nombre is None:
        return False
    if nombre.strip() == "":
        return False
    return True


def nota_valida(nota):
    if nota is None:
        return False
    if nota == "":
        return False
    if not nota.isdigit():
        return False
    return True


def limpiar_registros(students):
    registros_limpios = []

    for alumno in students:
        nombre = alumno["name"]
        nota = alumno["grade"]
        estado = alumno["status"]

        if nombre_valido(nombre) and nota_valida(nota):
            alumno_limpio = {
                "name": nombre.strip().title(),
                "grade": int(nota),
                "status": estado.strip().title()
            }
            registros_limpios.append(alumno_limpio)

    return registros_limpios


def eliminar_duplicados(registros):
    alumnos_unicos = {}

    for alumno in registros:
        nombre = alumno["name"]

        if nombre not in alumnos_unicos:
            alumnos_unicos[nombre] = alumno
        else:
            if alumno["grade"] > alumnos_unicos[nombre]["grade"]:
                alumnos_unicos[nombre] = alumno

    return list(alumnos_unicos.values())


def ordenar_por_nombre(registros):
    return sorted(registros, key=lambda alumno: alumno["name"])