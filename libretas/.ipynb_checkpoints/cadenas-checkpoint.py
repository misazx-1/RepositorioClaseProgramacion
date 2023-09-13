# 1. Escribe un predicado que verifica si una cadena de caracteres es
# un dígito.

def es_digito(s):
    """
    Determina si s es una cadena de un caracter que sea dígito.
    """
    return (
        s == '0' or
        s == '1' or
        s == '2' or
        s == '3' or
        s == '4' or
        s == '5' or
        s == '6' or
        s == '7' or
        s == '8' or
        s == '9'
    )


# 2. Escribe un predicado que verifica si una cadena de caracteres
# consiste únicamente de dígitos.

def solo_digitos_desde(s, i):
    """
    Determina si una cadena consiste únicamente de dígitos a partir de
    la posición i.
    """
    return True if i >= len(s) else (
        es_digito(s[i]) and solo_digitos_desde(s, i + 1)
    )

def solo_digitos(s):
    """
    Determina si s es una cadena que consiste únicamente de dígitos.
    """
    return isinstance(s, str) and solo_digitos_desde(s, 0)


# 3. Escribe una función que genere un dígito de forma aleatoria.

import random

def digito_aleatorio():
    """
    Regresa una cadena con un dígito aleatorio.
    """
    return random.choice('0123456789')


# 4. Escribe una función que genera una cadena con $n$ dígitos
# aleatorios.

def genera_digitos_aleatorios(n):
    """
    Regresa una cadena de longitud n que consiste únicamente de
    dígitos elegidos aleatoriamente. No se valida el tipo del
    argumento.
    """
    return '' if n <= 0 else (
        digito_aleatorio() +
        genera_digitos_aleatorios(n - 1)
    )

def digitos_aleatorios(n):
    """
    Regresa una cadena de longitud n que consiste únicamente de
    dígitos elegidos aleatoriamente.
    """
    assert isinstance(n, int), "solo se aceptan enteros"
    assert n >= 0, "solo se aceptan enteros no negativos"
    return genera_digitos_aleatorios(n)


# 5. Escribe una función que calcule la distancia de Hamming de dos
# cadenas de dígitos del mismo tamaño.

def distancia_desde(dstr1, dstr2, i):
    """
    Calcula la cantidad de diferencias entre las cadenas de dígitos
    dstr1 y dstr2 a partir de la posición i.
    """
    return 0 if i >= len(dstr1) else (
        0 if dstr1[i] == dstr2[i] else 1
    )

def distancia(dstr1, dstr2):
    """
    Calcula la cantidad de diferencias entre las cadenas de dígitos
    dstr1 y dstr2.
    """
    assert solo_digitos(dstr1), "solo se aceptan cadenas de dígitos"
    assert solo_digitos(dstr2), "solo se aceptan cadenas de dígitos"
    assert len(dstr1) == len(dstr2), "las cadenas deben tener el mismo tamaño"
    return distancia_desde(dstr1, dstr2, 0)
    

# 6. Escribe una función que dada una cadena de dígitos, regresa una
# cadena igual pero con un dígito cualquiera modificado a otro de
# forma aleatoria.

def otro_digito(dig):
    """
    Regresa un digito distinto a dig.
    """
    return random.choice('0123456789'.replace(dig, ''))

def cambia_digito_en(dstr, i):
    """
    Cambia el dígito de dstr en la posición i por otro de forma
    aleatoria.
    """
    return dstr[0:i] + otro_digito(dstr[i]) + dstr[i+1:]

def cambia_digito1(dstr):
    """
    Regresa una cadena como dstr pero con un único dígito modificado a
    otro de forma aleatoria.
    """
    return cambia_digitos(dstr, 1)
    

# 7. Escribe una función que dada una cadena de dígitos, regresa una
# cadena igual pero con dos dígitos cualquiera modificados a otros de
# forma aleatoria.

def cambia_digito2(dstr):
    """
    Regresa una cadena como dstr pero con dos dígitos modificados a
    otros de forma aleatoria.
    """
    return cambia_digitos(dstr, 2)


# 8. Escribe una función que dada una cadena de dígitos, regresa una
# cadena igual pero con tres dígitos cualquiera modificados a otros de
# forma aleatoria.

def cambia_digito3(dstr):
    """
    Regresa una cadena como dstr pero con tres dígitos modificados a
    otros de forma aleatoria.
    """
    return cambia_digitos(dstr, 3)


# 9. Escribe una función que dada una cadena de $N$ dígitos, regrese
# una cadena igual pero con $n$ dígitos cualquiera modificados a otros
# de forma aleatoria, donde $n \leq N$.

def cambia_digitos_iter(dstr, N, n, m, i):
    rand = random.random()
    rest = n - m
    pending = N - i
    return '' if pending == 0 else (
        otro_digito(dstr[i]) + cambia_digitos_iter(dstr, N, n, m + 1, i + 1)
        if rand <= rest / pending else (
                dstr[i] + cambia_digitos_iter(dstr, N, n, m, i + 1)
        )
    )

def cambia_digitos(dstr, n):
    """
    Regresa una cadena como dstr pero con n dígitos modificados a
    otros de forma aleatoria.
    """
    assert solo_digitos(dstr), "solo se aceptan cadenas de dígitos"
    assert isinstance(n, int), "debe ser un entero"
    assert n >= 0, "debe ser un entero no negativo"
    assert n <= len(dstr), "debe ser un entero no negativo menor que la longitud de la cadena"
    return cambia_digitos_iter(dstr, len(dstr), n, 0, 0)
