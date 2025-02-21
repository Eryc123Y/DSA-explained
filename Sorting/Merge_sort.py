from typing import TypeVar, Callable, Iterable

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def merge_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
    """
    Sorts a linear structure in ascending order using the merge sort algorithm.

    Parameters:
    ln_struct: Linear structure to be sorted.
    key: Function that returns the key used to sort the elements.
    reverse: If True, the structure is sorted in descending order.
    """

    def merge(left: int, middle: int, right: int) -> None:
        """
        Merges two sorted parts of the list.
        """
        # Create two temporary lists to store the left and right parts
        left_part = ln_struct[left:middle + 1]
        right_part = ln_struct[middle + 1:right + 1]

        # Initialize indices for the left and right parts
        left_index = 0
        right_index = 0

        # Initialize the index for the merged list
        merged_index = left

        # Merge the two parts into the original list
        while left_index < len(left_part) and right_index < len(right_part):
            # Compare the keys of the elements
            if (key(left_part[left_index]) <= key(right_part[right_index])) != reverse:
                ln_struct[merged_index] = left_part[left_index]
                left_index += 1
            else:
                ln_struct[merged_index] = right_part[right_index]
                right_index += 1
            merged_index += 1

        # Copy the remaining elements from the left part
        while left_index < len(left_part):
            ln_struct[merged_index] = left_part[left_index]
            left_index += 1
            merged_index += 1

        # Copy the remaining elements from the right part
        while right_index < len(right_part):
            ln_struct[merged_index] = right_part[right_index]
            right_index += 1
            merged_index += 1

    def merge_sort_helper(left: int, right: int) -> None:
        """
        Recursively sorts the list using the merge sort algorithm.
        """
        if left < right:
            # Find the middle index
            middle = (left + right) // 2

            # Sort the left and right parts
            merge_sort_helper(left, middle)
            merge_sort_helper(middle + 1, right)

            # Merge the sorted parts
            merge(left, middle, right)

    # Call the helper function to start the sorting process
    merge_sort_helper(0, len(ln_struct) - 1)