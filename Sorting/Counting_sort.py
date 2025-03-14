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
        
def stable_counting_sort(ln_struct: Iterable[int], reverse: bool = False) -> Iterable[int]:
    """
    Sorts a linear structure in ascending order using the stable counting sort algorithm.
    The relative order is preserved
    """
    # similar approach, but two differences:
    # 1. Instead of counting the occurrences, we count the cumulative sum of the indices
    # this is to preserve the relative order information
    # 2. We iterate the original array in reverse order to preserve the relative order
    if not ln_struct:
        return []
    
    # Find min and max to accommodate negative numbers
    min_val, max_val = min(ln_struct), max(ln_struct)
    cumulative_map = [0] * (max_val - min_val + 1)
    for elem in ln_struct:
        cumulative_map[elem - min_val] += 1
    for i in range(1, len(cumulative_map)):
        cumulative_map[i] += cumulative_map[i - 1]
    
    res = [0] * len(ln_struct)
    for i in range(len(ln_struct) - 1, -1, -1):
        elem = ln_struct[i]
        index = elem - min_val
        cumulative_map[index] -= 1 # decrement the count, as we added the later element to the result, so the previous element should be shifted to the left
        res[cumulative_map[index]] = elem
    
    if reverse:
        res.reverse()
    
    return res
    
    

def main():
    ln_struct = [4, 2, 2, 8, 3, 3, 1]
    print("Before sorting:", ln_struct)
    ln_struct = stable_counting_sort(ln_struct)
    print("After sorting:", ln_struct)
    
    
if __name__ == "__main__":
    main()
                
    