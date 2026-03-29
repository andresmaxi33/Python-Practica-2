def calcular_envio(peso, zona):
    if zona not in ["local", "regional", "nacional"]:
        return None

    if peso <= 1:
        if zona == "local":
            return 500
        elif zona == "regional":
            return 1000
        elif zona == "nacional":
            return 2000

    elif peso <= 5:
        if zona == "local":
            return 1000
        elif zona == "regional":
            return 2500
        elif zona == "nacional":
            return 4500

    else:
        if zona == "local":
            return 2000
        elif zona == "regional":
            return 5000
        elif zona == "nacional":
            return 8000