# Determina si el parametro es un Palindromo
def is_palindromo(texto):
    texto = str(texto)
    if (texto == ''):
        return False
    else:
        return texto == texto[::-1]