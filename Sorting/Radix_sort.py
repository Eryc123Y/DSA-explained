from typing import TypeVar, Iterable, Callable

T = TypeVar('T')

def basic_radix_sort_aux(ln_struct: Iterable[int], exp: int) -> Iterable[int]:
    """
    Auxiliary function for the basic radix sort algorithm
    This is basically the counting sort algorithm for the current digit.
    """
    count_map = [0] * 10 # initialize the count array
    # count the occurrences of each digit
    for elem in ln_struct: 
        count_map[(elem // exp) % 10] += 1
    # calculate the cumulative sum
    for i in range(1, 10):
        count_map[i] += count_map[i - 1]
    # reconstruct the array
    res = [0] * len(ln_struct)
    for i in range(len(ln_struct) - 1, -1, -1):
        # retrieve the current digit/element
        current_digit = (ln_struct[i] // exp) % 10
        res[count_map[current_digit] - 1] = ln_struct[i]
        # update the target index for the current digit by decrementing the count
        count_map[current_digit] -= 1
    return res

    


def basic_radix_sort(ln_struct: Iterable[int], reverse: bool = False) -> Iterable[int]:
    """
    Sorts a linear structure in ascending order using the basic radix sort algorithm.
    The relative order is not preserved for elements with the same value.
    Only consider positive integers and base 10.

    Parameters:
    ln_struct: Linear structure to be sorted.
    reverse: If True, the structure is sorted in descending order.
    """
    if not ln_struct:
        return []
    max_val = max(ln_struct)
    exp = 1
    while max_val // exp > 0:
        ln_struct = basic_radix_sort_aux(ln_struct, exp)
        exp *= 10
    if reverse:
        ln_struct.reverse()
    return ln_struct
    

def radix_sort_aux(ln_struct: Iterable[int], exp: int, base: int, key: Callable) -> Iterable[int]:
    """
    Auxiliary function for the radix sort algorithm
    This is basically the counting sort algorithm for the current digit.
    
    Parameters:
    ln_struct: Linear structure to be sorted.
    exp: The current digit position.
    base: The base of the numbers in the linear structure.
    key: Function that returns the key used to sort the elements.
    
    """
    map = [0] * base # initialize the count array
    # count the occurrences of each digit
    for elem in ln_struct:
        digit = (key(elem) // exp) % base
        map[digit] += 1
    # calculate the cumulative sum
    for i in range(1, base):
        map[i] += map[i - 1]
    # reconstruct the array
    res = [0] * len(ln_struct)
    for i in range(len(ln_struct) - 1, -1, -1):
        # retrieve the current digit/element
        digit = (key(ln_struct[i]) // exp) % base
        res[map[digit] - 1] = ln_struct[i]
        # update the target index for the current digit by decrementing the count
        map[digit] -= 1
    return res

def radix_sort(ln_struct: Iterable[int], 
               base: int, reverse:bool = False, 
               key: Callable = lambda x: x) -> Iterable[int]:
    """
    Sorts a linear structure in ascending order using the radix sort algorithm.
    The relative order is not preserved for elements with the same value.
    This implementation allows different base and key function, also consider negative numbers.

    Parameters:
    ln_struct: Linear structure to be sorted.
    base: The base of the numbers in the linear structure.
    reverse: If True, the structure is sorted in descending order.
    key: Function that returns the key used to sort the elements.
    """
    if not ln_struct:
        return []
    # find the min and max value
    min_val = min(ln_struct)
    # adjust the counting array size and offsets
    # this maps all numbers to positive integers, but keep the relative order
    offset = 0
    if min_val < 0:
        offset = abs(min_val)
    
    shifted_arr = [elem + offset for elem in ln_struct]
    max_val = max(shifted_arr)
    # now we can sort the shifted array as in the normal case
    exp = 1
    while max_val // exp > 0:
        shifted_arr = radix_sort_aux(shifted_arr, exp, base, key)
        exp *= base
    
    # we need to restore the value before offsetting for integrity
    result = [elem - offset for elem in shifted_arr]
    if reverse:
        result.reverse()
    return result


def counting_sort_by_char(strings: list[str], position: int) -> list[str]:
    """
    Performs counting sort on a list of strings based on the character at a specific position.
    
    Parameters:
    strings: List of strings to be sorted
    position: Character position to sort by (0 is leftmost character)
    
    Returns:
    Sorted list of strings
    """
    # ASCII has 256 possible characters
    count = [0] * 257  # 256 for ASCII chars + 1 for "no character" (shorter strings)
    
    # Count occurrences
    for s in strings:
        # If string is shorter than position, use 0 (comes before any char)
        char_val = ord(s[position]) if position < len(s) else 0
        count[char_val + 1] += 1  # +1 offset to reserve 0 for shorter strings
    
    # Calculate cumulative counts
    for i in range(1, 257):
        count[i] += count[i - 1]
    
    # Build the sorted array
    result = [None] * len(strings)
    for s in reversed(strings):  # Process in reverse for stability
        char_val = ord(s[position]) if position < len(s) else 0
        result[count[char_val]] = s
        count[char_val] += 1
    
    return result


def radix_sort_strings(strings: list[str], reverse: bool = False) -> list[str]:
    """
    Sorts a list of strings using radix sort.
    
    Parameters:
    strings: List of strings to be sorted
    reverse: If True, the strings are sorted in descending order
    
    Returns:
    Sorted list of strings
    """
    if not strings:
        return []
    
    # Find maximum string length
    max_length = max(len(s) for s in strings)
    
    # Counting sort for each character position, starting from rightmost
    for position in range(max_length - 1, -1, -1):
        strings = counting_sort_by_char(strings, position)
    
    if reverse:
        strings.reverse()
    
    return strings


def radix_sort_strings_optimized(strings: list[str], reverse: bool = False) -> list[str]:
    """
    Sorts a list of strings using radix sort with length-based preprocessing.
    
    By first separating strings by length, we:
    1. Avoid unnecessary character comparisons
    2. Only need to sort each length group up to its own max length
    3. Immediately establish correct ordering between different length strings
    
    Parameters:
    strings: List of strings to be sorted
    reverse: If True, the strings are sorted in descending order
    
    Returns:
    Sorted list of strings
    """
    if not strings:
        return []
    
    # Group strings by length
    length_groups = {}
    for s in strings:
        length = len(s)
        if length not in length_groups:
            length_groups[length] = []
        length_groups[length].append(s)
    
    # Sort each length group separately
    result = []
    lengths = sorted(length_groups.keys(), reverse=reverse)
    
    for length in lengths:
        group = length_groups[length]
        
        # Optimization: If only one string of this length, no need to sort
        if len(group) <= 1:
            result.extend(group)
            continue
        
        # Apply radix sort to this group
        # Process characters from right to left (MSD radix sort)
        for position in range(length - 1, -1, -1):
            group = counting_sort_by_char_optimized(group, position)
        
        result.extend(group)
    
    return result


def counting_sort_by_char_optimized(strings: list[str], position: int) -> list[str]:
    """
    Optimized counting sort for strings of the same length.
    No need to check if position is valid since all strings have the same length.
    """
    # ASCII has 256 possible characters
    count = [0] * 256
    
    # Count occurrences
    for s in strings:
        char_val = ord(s[position])
        count[char_val] += 1
    
    # Calculate cumulative counts
    for i in range(1, 256):
        count[i] += count[i - 1]
    
    # Build the sorted array
    result = [None] * len(strings)
    for s in reversed(strings):  # Process in reverse for stability
        char_val = ord(s[position])
        count[char_val] -= 1
        result[count[char_val]] = s
    
    return result

# test the radix sort
def main():
    ln_struct = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(ln_struct, 10))
    print(radix_sort(ln_struct, 10, reverse=True))
    ln_struct = [170, 45, 75, 90, 802, 24, 2, 66, -1, -2, -3]
    print(radix_sort(ln_struct, 10))
    print(radix_sort(ln_struct, 10, reverse=True))
    ln_struct = [170, 45, 75, 90, 802, 24, 2, 66]
    print(radix_sort(ln_struct, 16))
    print(radix_sort(ln_struct, 16, reverse=True))
    ln_struct = [170, 45, 75, 90, 802, 24, 2, 66, -1, -2, -3]
    print(radix_sort(ln_struct, 16))
    print(radix_sort(ln_struct, 16, reverse=True))

if __name__ == "__main__":
    main()