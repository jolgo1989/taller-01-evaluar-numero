# src/soluciones.py

def evaluar_numero(numero: int) -> str:
    """
    Recibe un número entero y retorna:
    - 'positivo' si el número es mayor a cero.
    - 'negativo' si el número es menor a cero.
    - 'cero' si el número es igual a cero.
    """
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
