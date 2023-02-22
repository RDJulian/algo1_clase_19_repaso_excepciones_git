def insertionSort(lista: list[int]) -> None:
    """
    PRE:
    POST: Ordena los elementos de la lista en forma ascendente.
    TESTS:
    >>> insertionSortTest([1, 5, 4, 3])
    [1, 3, 4, 5]
    """
    for i in range(1, len(lista)):
        elementoAInsertar = lista[i]
        j = i - 1
        while j >= 0 and elementoAInsertar < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = elementoAInsertar


# Funcion para testear sin tener que devolver la lista desde insertionSort()
def insertionSortTest(listaTest: list[int]) -> list[int]:
    insertionSort(listaTest)
    return listaTest
