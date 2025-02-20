from typing import TypeVar, Callable, Iterable

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def Selection_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the selection sort algorithm.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """

    n = len(ln_struct)
    # keep reference to the left of unsorted part of the list
    for i in range(n):
        # find the index of the minimum element in the unsorted part
        min_index = i
        for j in range(i + 1, n):
            # if reverse, we find the maximum element
            # if not reverse, we find the minimum element
            if (key(ln_struct[j]) < key(ln_struct[min_index])) != reverse:
                min_index = j
        # swap the minimum element with the leftmost element of the unsorted part
        swap(ln_struct, i, min_index)