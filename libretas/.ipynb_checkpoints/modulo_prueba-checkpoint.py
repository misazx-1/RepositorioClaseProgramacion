def cadena_es_digito(a):
    try:
        if int(a) < 10 and int(a) > -1 and type(a) == type('a'):
            return True
        else:
            return False
    except:
        return False