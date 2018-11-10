# Metodo de deteccion de anagramas
def detector_anagramas(texto_1, texto_2):
    texto_1 = str(texto_1)
    texto_2 = str(texto_2)
    return sorted(texto_1) == sorted(texto_2)