from Sort import Sort
from Linear_structures import Linear_Structure
from typing import TypeVar, List, Callable, Any

T = TypeVar('T')
class BubbleSort(Sort):
    """
    Bubble sort algorithm.
    """
    
    def sort(self, ln_struct: Linear_Structure[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
        """
        Sorts a linear structure in ascending order.
        
        Parameters:
        ln_struct: Linear structure to be sorted.
        key: Function that returns the key used to sort the elements.
        reverse: If True, the structure is sorted in descending order.
        """
        n = len(ln_struct)
        for i in range(n):
            for j in range(0, n-i-1):
                if key(ln_struct[j]) > key(ln_struct[j+1]):
                    ln_struct[j], ln_struct[j+1] = ln_struct[j+1], ln_struct[j]
        if reverse:
            ln_struct.reverse()
            
            
            
            