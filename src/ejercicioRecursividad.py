# Programar una funcion potencia que tenga como parametro una base y un exponente enteros, y devuelva el resultado.
# NO SE PUEDE resolver con iteraciones. Debe ser una funcion recursiva.

class IndeterminacionException(Exception):
    """Excepcion lanzada cuando se intenta calcular una indeterminacion"""


def potenciaExponentePositivo(base: int, exponente: int) -> int:
    """
    PRE: El exponente debe ser positivo. Solo deberia ser llamada desde potencia(), pero igual funcionaria si se llama
    desde otra funcion.
    POST: Devuelve la potencia de la base y el exponente ingresados. El caso 0 elevado a 0 devuelve 1, que dependiendo
    el contexto puede ser correcto.
    """
    if base == 0 and exponente == 0:
        raise IndeterminacionException("La operacion ingresada es indeterminada.")
    elif exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        # Optimización del algoritmo: como se calcula practicamente lo mismo dos veces, se ahorran llamados si solo
        # calculamos la potencia(base, exponente // 2) una sola vez, luego se multiplica y devuelve. Si es impar, se
        # multiplica manualmente una vez más la base al resultado. De esta forma, el algoritmo hace log(n) llamados.
        resultado = potenciaExponentePositivo(base, exponente // 2)
        resultado *= resultado
        if exponente % 2 == 0:
            return resultado
        else:
            return base * resultado


def potencia(base: int, exponente: int) -> int | float:
    """
    PRE:
    POST: Devuelve la potencia de la base y el exponente ingresados. Los casos de 0 elevado a 0 y 0 elevado a un
    exponente negativo son indeterminados. En tales casos, lanza excepcion.
    TESTS:
    # Este caso se puede tomar como 1 o como indeterminado, dependiendo del uso.
    >>> potencia(0, 0)
    Traceback (most recent call last):
    ...
    ejercicioRecursividad.IndeterminacionException: La operacion ingresada es indeterminada.
    >>> potencia(0, -1)
    Traceback (most recent call last):
    ...
    ejercicioRecursividad.IndeterminacionException: La operacion ingresada es indeterminada.
    >>> potencia(0, 3)
    0
    >>> potencia(2, 2)
    4
    >>> potencia(2, 5)
    32
    >>> potencia(-2, 2)
    4
    >>> potencia(-2, 3)
    -8
    >>> potencia(2, -2)
    0.25
    >>> potencia(-2, -3)
    -0.125
    """
    if base == 0 and exponente < 0:
        raise IndeterminacionException("La operacion ingresada es indeterminada.")
    elif exponente < 0:
        return 1 / potenciaExponentePositivo(base, exponente * -1)
    else:
        return potenciaExponentePositivo(base, exponente)
