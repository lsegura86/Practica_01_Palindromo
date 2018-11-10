# Determina si el parametro es un Palindromo
def is_palindromo(texto):
    texto = str(texto)
    if (texto == ''):
        return False
    else:
        if texto == texto[::-1]:
            return True
        else:
            return False