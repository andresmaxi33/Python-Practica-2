def extraer_hashtags(posts):
    hashtags = []
    
    for post in posts:
        palabras = post.split()
        
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtags.append(palabra)
    
    return hashtags


def contar_hashtags(hashtags):
    frecuencias = {}
    
    for hashtag in hashtags:
        if hashtag in frecuencias:
            frecuencias[hashtag] += 1
        else:
            frecuencias[hashtag] = 1
    
    return frecuencias


def obtener_trending(frecuencias):
    trending = {}
    
    for hashtag in frecuencias:
        if frecuencias[hashtag] > 1:
            trending[hashtag] = frecuencias[hashtag]
    
    return trending