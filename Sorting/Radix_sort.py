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