from typing import TypeVar, List, Callable, Any, Iterable

from Linear_Structures.Vector import Vector

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def Bubble_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """
    n = len(ln_struct)
    # keep reference to the left of unsorted part of the list
    for i in range(n):
        # n-1 is the last index, -i here is to avoid comparing the last i elements
        # n-i-1 is the right boundary of the unsorted part
        # we are like bubbling the largest element to the right, while the smallest element bubbles to the left
        for j in range(0, n - i - 1):
            if (key(ln_struct[j]) > key(ln_struct[j + 1])) != reverse:
                swap(ln_struct, j, j + 1)


def Cocktail_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the cocktail sort algorithm.
    Cocktail sort is a variation of bubble sort that sorts in both directions.
    It is more efficient than bubble sort for large lists.
    Parameters:
    """
    n = len(ln_struct)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if (key(ln_struct[i]) > key(ln_struct[i + 1])) != reverse:
                swap(ln_struct, i, i + 1)
                swapped = True
        if not swapped: # if no swaps were made, the list is sorted, stop iteration
            break
        swapped = False
        end -= 1
        for i in range(end - 1, start - 1, -1):
            if (key(ln_struct[i]) > key(ln_struct[i + 1])) != reverse:
                swap(ln_struct, i, i + 1)
                swapped = True
        start += 1


# Example usage
ls = Vector(elements=[3, 5, 2, 1, 4])
Cocktail_sort(ln_struct=ls, reverse=True)
print(ls)  # Output should be [1, 2, 3, 4, 5]
