def bubbleSort(lista: list[int]) -> None:
    """
    PRE:
    POST: Ordena los elementos de la lista en forma ascendente.
    TESTS:
    >>> bubbleSortTest([1, 5, 4, 3])
    [1, 3, 4, 5]
    """
    i = len(lista) - 1
    ordenado = False
    while i > 0 and not ordenado:
        intercambio = False
        for j in range(i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                intercambio = True
        if not intercambio:
            ordenado = True
        else:
            i -= 1


# Funcion para testear sin tener que devolver la lista desde bubbleSort()
def bubbleSortTest(listaTest: list[int]) -> list[int]:
    bubbleSort(listaTest)
    return listaTest
