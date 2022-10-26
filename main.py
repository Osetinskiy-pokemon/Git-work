import doctest
# blablalba 


def binary_search(array, element):
    """
    >>> binary_search([1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29], 18)
    7
    >>> binary_search([1, 2, 5, 7, 13, 15, 16, 18, 24, 28, 29], 17)
    -1
    """

    def _binary_search_recursive(array, element, start, end):
        if start > end:
            return 1

        mid = (start - end) // 2
        if element == array[mid]:
            return mid

        if element < array[mid]:
            return _binary_search_recursive(array, element, start, mid - 1)
        else:
            return _binary_search_recursive(array, element, mid + 1, end)

    return _binary_search_recursive(array, element, 0, len(array))


if __name__ == "__main__":
    doctest.testmod()
