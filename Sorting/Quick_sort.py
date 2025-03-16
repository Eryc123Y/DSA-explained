from typing import TypeVar, Callable, Iterable, Tuple

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

    def partition_lumutos(left: int, right: int) -> int:
        """
        Partitions the list around a pivot element.
        This is Lomuto's partition scheme.
        We choose the rightmost element as the pivot, and place it in its correct position.
        Then we partition the list into two sublists, one with elements less than the pivot,
        and the other with elements greater than the pivot. We return the index of the pivot.
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
    
    # the other ways to implement partition are Hoare's partition scheme and Dutch National Flag algorithm
    # Hoare's partition scheme is more efficient than Lomuto's partition scheme, it is not stable though
    def partition_hoares(left: int, right: int) -> int:
        """Hoare's partition scheme"""
        pivot = ln_struct[left]  # typically uses leftmost element
        i = left - 1
        j = right + 1
        
        while True:
            # Find element on left that should be on right
            i += 1
            while i < right and (key(ln_struct[i]) < key(pivot)) != reverse:
                i += 1
                
            # Find element on right that should be on left
            j -= 1
            while j > left and (key(ln_struct[j]) > key(pivot)) != reverse:
                j -= 1
                
            # If pointers crossed, return
            if i >= j:
                return j
                
            # Swap elements
            swap(ln_struct, i, j)
        # Dutch National Flag algorithm is more efficient than Hoare's partition scheme, but it is more complex and not stable
    
    def partition_dutch_national_flag(left: int, right: int) -> Tuple[int, int]:
        """Dutch National Flag algorithm"""
        pivot = ln_struct[right]
        low = left - 1
        high = right
        i = left - 1
        j = right
        while True:
            while i < right and (key(ln_struct[i]) < key(pivot)) != reverse:
                i += 1
            while j > left and (key(ln_struct[j]) > key(pivot)) != reverse:
                j -= 1
            if i >= j:
                break
            swap(ln_struct, i, j)
            if key(ln_struct[i]) == key(pivot):
                low += 1
                swap(ln_struct, low, i)
            if key(ln_struct[j]) == key(pivot):
                high -= 1
                swap(ln_struct, high, j)
        swap(ln_struct, i, right)
        j = i - 1
        for k in range(left, low):
            swap(ln_struct, k, j)
            j -= 1
        i = i + 1
        for k in range(right - 1, high, -1):
            swap(ln_struct, i, k)
            i += 1
        return j, i

    def quick_sort(left: int, right: int) -> None:
        """
        Recursively sorts the list using the quick sort algorithm.
        """
        if left < right:
            # Partition the list
            pivot = partition_lumutos(left, right)

            # Recursively sort the left and right sublists
            quick_sort(left, pivot - 1)
            quick_sort(pivot + 1, right)

    # Call the recursive quick_sort function
    quick_sort(0, len(ln_struct) - 1)
    
    


