def procesar_datos_complejos(a, b, c, d):
    """
    Esta función tiene alta complejidad ciclomática (muchos if/else).
    Lizard debería marcarla con un CCN alto.
    """
    resultado = 0
    
    # Inicio del código complejo
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    resultado = a + b + c + d
                else:
                    resultado = a + b + c - d
            else:
                if d > 0:
                    resultado = a + b - c + d
                else:
                    resultado = a + b - c - d
        else:
            if c > 0:
                for i in range(10):
                    if i % 2 == 0:
                        resultado += i
            else:
                resultado = a - b
    elif a < 0:
        if b < 0:
            resultado = a * b
        else:
            resultado = a / b
    
    return resultado

def funcion_muerta():
    # Esta función nunca se usa, pero añade complejidad al archivo
    x = 1
    if x == 1:
        return x
    else:
        return 0