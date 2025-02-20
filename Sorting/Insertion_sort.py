from typing import TypeVar, Callable, Iterable

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def Insertion_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the insertion sort algorithm.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """

    # Outer loop, starting from the second element
    for i in range(1, len(ln_struct)):
        # Inner loop, starting from the current element and moving left
        # the sliding window is the unsorted part of the list, similar to bubble sort
        j = i
        # the code is quite compact, but the idea is simple (see below)
        # If reverse, we check if the key of the left element is less than the key of the right element, and swap
        # If not reverse, we check if the key of the left element is greater than the key of the right element, and swap
        # You may want to write the code in a more verbose way or try some examples to understand it better
        while j > 0 and (key(ln_struct[j - 1]) > key(ln_struct[j])) != reverse:
            swap(ln_struct, j - 1, j)
            j -= 1