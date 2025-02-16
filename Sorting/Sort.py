from abc import ABC, abstractmethod
from typing import TypeVar, List, Callable, Any
import copy
from Linear_structures import Linear_Structure

T = TypeVar('T')


class Sort(ABC):
    """
    Abstract class for sorting algorithms for linear structures.
    """

    def __init__(self) -> None:
        pass

    @abstractmethod
    def sort(self, ln_struct: Linear_Structure[T], key: Callable = lambda x: x, reverse: bool = False) -> None:
        """
        Sorts a linear structure in ascending order.
        
        Parameters:
        ln_struct: Linear structure to be sorted.
        key: Function that returns the key used to sort the elements.
        reverse: If True, the structure is sorted in descending order.
        """
        pass

    def sort_and_return(self, ln_struct: Linear_Structure[T], key: Callable = lambda x: x, reverse: bool = False) -> \
    any[T]:
        """
        Sorts a linear structure in ascending order and returns the sorted structure
        The original structure is not modified.
        """
        copied_ln_struct = copy.deepcopy(ln_struct)
        self.sort(copied_ln_struct, key, reverse)
        return copied_ln_struct

    def swop(self, ln_struct: any[T], i: int, j: int) -> None:
        """
        Swops two elements in a linear structure.
        """
        temp = ln_struct[i]
        ln_struct[i] = ln_struct[j]
        ln_struct[j] = temp
        # or in a pythonic way: ln_struct[i], ln_struct[j] = ln_struct[j], ln_struct[i]
