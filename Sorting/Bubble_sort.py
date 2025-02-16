from Sort import Sort
from typing import TypeVar, List, Callable, Any, Iterable
from Linear_Structures.Vector import Vector

T = TypeVar('T')


class BubbleSort(Sort):
    """
    Bubble sort algorithm.
    """

    def sort(self, ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
        """
        Sorts a linear structure in ascending order.
        
        Parameters:
        ln_struct: Linear structure to be sorted.
        key: Function that returns the key used to sort the elements.
        reverse: If True, the structure is sorted in descending order.
        """
        n = len(ln_struct)
        # we need to keep reference to the left of unsorted part of the list
        for i in range(n):
            # n-1 is the last index, -i here is to avoid comparing the last i elements
            # as they are already sorted, thus n-i-1 is the right boundary of the unsorted part
            for j in range(0, n - i - 1):
                if key(ln_struct[j]) > key(ln_struct[j + 1]):
                    swop(ln_struct, j, j + 1)
        if reverse:
            ln_struct.reverse()



