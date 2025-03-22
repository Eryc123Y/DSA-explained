from typing import TypeVar, Callable, Iterable, Tuple, Collection

T = TypeVar('T')


def swap(ln_struct: Iterable[T], i: int, j: int) -> None:
    """
    Swaps two elements in a linear structure.
    """
    temp = ln_struct[i]
    ln_struct[i] = ln_struct[j]
    ln_struct[j] = temp


def quick_sort(ln_struct: Iterable[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
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

    def sort(left: int, right: int) -> None:
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
    sort(0, len(ln_struct) - 1)
    
    
def naive_quick_select(ln_struct: Collection[T], k: int) -> T:
    """
    Finds the k-th smallest element in a linear structure using the quick select algorithm.

    Parameters:
    ln_struct: Linear structure to be searched.
    k: Index of the element to be found.
    """
    def partition_lumutos(left: int, right: int) -> int:
        # Choose the rightmost element as the pivot
        pivot = ln_struct[right]
        i = left - 1

        # Iterate over the elements from left to right
        for j in range(left, right):
            # Compare the keys of the elements
            if (ln_struct[j] <= pivot):
                i += 1
                swap(ln_struct, i, j)

        # Place the pivot element in its correct position
        swap(ln_struct, i + 1, right)
        return i + 1
        
    
    def select(left: int, right: int, k: int) -> T:
        """
        Recursively finds the k-th smallest element in the list using the quick select algorithm.
        """
        if left == right:
            return ln_struct[left]

        # Partition the list
        pivot = partition_lumutos(left, right)

        # Recursively search the left or right sublist
        if k == pivot:
            return ln_struct[k]
        elif k < pivot:
            return select(left, pivot - 1, k)
        else:
            return select(pivot + 1, right, k)
    
    if not ln_struct:
        return None
    if k < 0 or k >= len(ln_struct):
        raise ValueError('k is out of bounds')
    return select(0, len(ln_struct) - 1, k)

def median_of_medians_select(arr: Collection[T], k: int) -> T:
    """
    Returns the k-th smallest element in arr (0-indexed) using the 
    Median of Medians algorithm, which guarantees worst-case linear time.
    
    Parameters:
      arr: List of comparable elements.
      k: Index (0-indexed) of the desired smallest element.
    
    Raises:
      ValueError: If k is out of bounds.
      
    Returns:
      The k-th smallest element.
    """
    if not 0 <= k < len(arr):
        raise ValueError("k is out of bounds")
    
    # Base case: Use sorting when list is small.
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    # Partition arr into sublists of at most 5 elements.
    sublists = [arr[i:i+5] for i in range(0, len(arr), 5)]
    # Find the median of each sublist.
    medians = [sorted(sub)[len(sub) // 2] for sub in sublists]
    
    # Recursively compute the pivot as the median of the medians.
    pivot = median_of_medians_select(medians, len(medians) // 2)
    
    # Partition the array into three lists.
    lows  = [x for x in arr if x < pivot]
    equals = [x for x in arr if x == pivot]
    highs = [x for x in arr if x > pivot]
    
    if k < len(lows):
        return median_of_medians_select(lows, k)
    elif k < len(lows) + len(equals):
        # The pivot is the k-th smallest.
        return pivot
    else:
        # Adjust k and search in the high partition.
        return median_of_medians_select(highs, k - len(lows) - len(equals))

# now we can implement an optimized quick select algorithm using the median of medians algorithm 
# to guarantee worst-case linear time of O(n) instead of O(n^2) of the naive quick select algorithm
def ultimate_quick_sort(arr: Collection[T], key: Callable[[T], T] = lambda x: x, reverse: bool = False) -> None:
    """
    Optimized quicksort that uses median-of-medians pivot selection to 
    guarantee worst-case O(n log n) performance.
    
    This function sorts the list in place.
    """
    
    def partition(left: int, right: int, pivot_val: T) -> int:
        """
        Partition the array using Lomuto's scheme. First, locate the pivot value
        (provided by median-of-medians), swap it to the end, then partition.
        """
        # Find an index for the pivot value in the current subarray.
        for idx in range(left, right + 1):
            if key(arr[idx]) == key(pivot_val):
                swap(arr, idx, right)
                break
        
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            # Compare using the given key and reverse flag.
            if (key(arr[j]) <= key(pivot)) != reverse:
                i += 1
                swap(arr, i, j)
        swap(arr, i + 1, right)
        return i + 1
    
    def sort(left: int, right: int) -> None:
        if left < right:
            # Choose the pivot using median of medians on the subarray.
            subarray = arr[left:right+1]
            # Get the median of the subarray.
            pivot_val = median_of_medians_select(subarray, len(subarray) // 2)
            # Partition around the chosen pivot.
            pivot_index = partition(left, right, pivot_val)
            sort(left, pivot_index - 1)
            sort(pivot_index + 1, right)
    
    sort(0, len(arr) - 1)
    
    # Reverse if necessary.
    if reverse:
        arr.reverse()