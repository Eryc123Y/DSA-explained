from typing import TypeVar, Iterable

T = TypeVar('T')

def basic_counting_sort(ln_struct: Iterable[int], reverse: bool = False) -> Iterable[int]:
    """
    Sorts a linear structure in ascending order using the basic counting sort algorithm.
    The relative order is not preserved for elements with the same value.

    Parameters:
    ln_struct: Linear structure to be sorted.
    reverse: If True, the structure is sorted in descending order.
    """
    if not ln_struct:
        return []
    
    # Find min and max to accommodate negative numbers
    min_val = min(ln_struct)
    max_val = max(ln_struct)
    
    # Adjust the counting array size and offsets
    count_map = [0] * (max_val - min_val + 1)
    
    # Count occurrences, map to the counting array by offsetting the min value
    for elem in ln_struct:
        count_map[elem - min_val] += 1
    
    # Reconstruct the array
    result = []
    for i, count in enumerate(count_map):
        if count > 0:
            result.extend([i + min_val] * count)
    
    if reverse:
        result.reverse()
    
    return result
        

def main():
    ln_struct = [4, 2, 2, 8, 3, 3, 1]
    print("Before sorting:", ln_struct)
    ln_struct = basic_counting_sort(ln_struct)
    print("After sorting:", ln_struct)
    
    
if __name__ == "__main__":
    main()
                
    