def selectionSort(lista: list[int]) -> None:
    """
    PRE:
    POST: Ordena los elementos de la lista en forma ascendente.
    TESTS:
    >>> selectionSortTest([1, 5, 4, 3])
    [1, 3, 4, 5]
    """
    for i in range(len(lista)):
        indiceMinimo = i
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[indiceMinimo]:
                indiceMinimo = j
        lista[i], lista[indiceMinimo] = lista[indiceMinimo], lista[i]


# Funcion para testear sin tener que devolver la lista desde selectionSort()
def selectionSortTest(listaTest: list[int]) -> list[int]:
    selectionSort(listaTest)
    return listaTest
