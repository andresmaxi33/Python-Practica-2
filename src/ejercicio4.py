def validar_email(email):
    # Debe tener exactamente un @
    if email.count("@") != 1:
        return False

    # No debe empezar ni terminar con @ o .
    if email.startswith("@") or email.endswith("@"):
        return False
    
    if email.startswith(".") or email.endswith("."):
        return False

    # Separar en parte antes y después del @
    partes = email.split("@")
    usuario = partes[0]
    dominio_completo = partes[1]

    # Debe haber al menos un carácter antes del @
    if len(usuario) < 1:
        return False

    # Debe haber al menos un punto después del @
    if "." not in dominio_completo:
        return False

    # La parte después del último punto debe tener al menos 2 caracteres
    dominio_final = dominio_completo.split(".")[-1]
    if len(dominio_final) < 2:
        return False

    return True