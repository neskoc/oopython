#!/usr/bin/python3
"""sort.py kmom05."""


def insertionsort(ul):
    """Sort of unordered list (Insertion)."""
    for i in range(1, len(ul)):
        j = i
        while j > 0:
            if isinstance(ul[j-1], str) != isinstance(ul[j], str):
                if isinstance(ul[j-1], str):
                    ul[j], ul[j-1] = ul[j-1], ul[j]
                j -= 1
            elif ul[j] < ul[j-1]:
                ul[j], ul[j-1] = ul[j-1], ul[j]
                j -= 1
            else:
                break
    return ul

def recursive_insertionsort(ul, n=None):
    """Recursive sort of unordered list (Insertion)."""
    if n is None:
        n = len(ul)
    if n <= 1:
        return None
    recursive_insertionsort(ul, n - 1)
    last = ul[n - 1]
    j = n - 2
    condition = True
    while j >= 0 and condition:
        if isinstance(ul[j], str) != isinstance(last, str):
            if isinstance(ul[j], str):
                ul[j + 1] = ul[j]
                j -= 1
        elif ul[j] > last:
            ul[j + 1] = ul[j]
            j -= 1
        else:
            condition = False
    ul[j + 1] = last
    return ul

def recursive_bubblesort(ul, n=None):
    """Recursive sort of unordered list (Bubblesort)."""
    if n is None:
        n = len(ul)

    if n == 1:
        return None
    for i in range(n - 1):
        if isinstance(ul[i], str) != isinstance(ul[i + 1], str):
            if isinstance(ul[i], str):
                ul[i], ul[i + 1] = ul[i + 1], ul[i]
        elif ul[i] > ul[i + 1]:
            ul[i], ul[i + 1] = ul[i + 1], ul[i]

    recursive_bubblesort(ul, n - 1)
    return ul

def test_sortfunctions():
    """Test sorting algorithms."""
    print("Insertionsort")
    test_list = ["a", 5, 3, "e", 1, "abc", 10, 6]
    print(insertionsort(test_list))
    print("Recursive Insertionsort")
    test_list = ["a", 5, 3, "e", 1, "abc", 10, 6]
    print(recursive_insertionsort(test_list))
    print("Recursive Bubblesort")
    test_list = ["a", 5, 3, "e", 1, "abc", 10, 6]
    print(recursive_bubblesort(test_list))

if __name__ == "__main__":
    test_sortfunctions()
