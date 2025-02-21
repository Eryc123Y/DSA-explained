from typing import TypeVar, Callable, Iterable

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def Quick_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the quick sort algorithm.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """

    def partition(left: int, right: int) -> int:
        """
        Partitions the list around a pivot element.
        """
        # Choose the rightmost element as the pivot
        pivot = ln_struct[right]
        i = left - 1

        # Iterate over the elements from left to right
        for j in range(left, right):
            # Compare the keys of the elements
            if (key(ln_struct[j]) <= key(pivot)) != reverse:
                i += 1
                swap(ln_struct, i, j)

        # Place the pivot element in its correct position
        swap(ln_struct, i + 1, right)
        return i + 1

    def quick_sort(left: int, right: int) -> None:
        """
        Recursively sorts the list using the quick sort algorithm.
        """
        if left < right:
            # Partition the list
            pivot = partition(left, right)

            # Recursively sort the left and right sublists
            quick_sort(left, pivot - 1)
            quick_sort(pivot + 1, right)

    # Call the recursive quick_sort function
    quick_sort(0, len(ln_struct) - 1)