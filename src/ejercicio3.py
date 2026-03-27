def obtener_spoilers(entrada):
    palabras = entrada.split(",")
    spoilers = []
    
    for palabra in palabras:
        spoilers.append(palabra.strip())
    
    return spoilers


def censurar_review(review, spoilers):
    review_censurada = review
    
    for spoiler in spoilers:
        asteriscos = "*" * len(spoiler)
        review_censurada = review_censurada.replace(spoiler, asteriscos)
        review_censurada = review_censurada.replace(spoiler.lower(), asteriscos)
        review_censurada = review_censurada.replace(spoiler.upper(), asteriscos)
        review_censurada = review_censurada.replace(spoiler.capitalize(), asteriscos)
    
    return review_censurada