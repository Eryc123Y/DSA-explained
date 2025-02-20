from typing import TypeVar, Callable, Iterable

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def shell_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the shell sort algorithm.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """

    # shell sort is a variation of insertion sort, with a gap between elements to be compared
    # this gap is reduced in each iteration, until it becomes 1, which is the same as insertion sort

    # Get the length of the input structure
    n = len(ln_struct)

    # Initialize the gap size to n/2
    # The gap size determines the distance between elements to be compared
    gap = n // 2

    # Continue until the gap becomes 0
    while gap > 0:
        # For each element starting from position 'gap'
        for i in range(gap, n):
            # For each element that is 'gap' positions behind the current element
            # Compare and swap if needed, similar to insertion sort but with a gap
            j = i
            while j >= gap:
                # Compare elements that are 'gap' positions apart
                # If reverse is True, we want descending order
                # If reverse is False, we want ascending order
                if (key(ln_struct[j - gap]) > key(ln_struct[j])) != reverse:
                    # Swap elements if they are in wrong order
                    swap(ln_struct, j - gap, j)
                    j -= gap
                else:
                    # If elements are in correct order, stop the inner loop
                    break

        # Reduce the gap size by half for the next iteration
        # When gap becomes 1, it performs regular insertion sort
        gap //= 2


