from abc import ABC, abstractmethod
from typing import TypeVar, Iterator, Generic

T = TypeVar('T')


class Linear_structure(ABC, Generic[T]):
    """
    Abstract class for linear structures.
    """

    def __init__(self) -> None:
        self.size = 0

    def is_empty(self) -> bool:
        """
        Returns True if the linear structure is empty.
        """
        return self.size == 0

    @abstractmethod
    def append(self, element: T) -> None:
        """
        Appends an element to the linear structure.
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """
        Removes and returns the last element of the linear structure.
        """
        pass

    def size(self) -> int:
        return self.size

    @abstractmethod
    def index(self, element: T) -> int:
        """
        Returns the index of the first occurrence of the element in the linear structure.
        returns -1 if the element is not in the linear structure.
        """
        pass

    @abstractmethod
    def insert(self, index: int, element: T) -> None:
        """
        Inserts an element at the given index.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of elements in the linear structure.
        """
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> T:
        """
        Returns the element at the given index.
        """
        pass

    @abstractmethod
    def __setitem__(self, index: int, element: T) -> None:
        """
        Sets the element at the given index.
        """
        pass

    @abstractmethod
    def __delitem__(self, index: int) -> None:
        """
        Deletes the element at the given index.
        """
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """
        Returns an iterator for the linear structure.
        """
        pass

    def __contains__(self, element: T) -> bool:
        """
        Returns True if the element is in the linear structure.
        """
        return self.index(element) != -1

    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the linear structure.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Removes all elements from the linear structure.
        """
        pass
    
    @abstractmethod
    def reverse(self) -> None:
        """
        Reverses the linear structure.
        """
        pass
