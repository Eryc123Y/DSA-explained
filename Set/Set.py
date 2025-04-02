from typing import TypeVar, Generic, List, Optional, Tuple, Iterator

from abc import ABC, abstractmethod

T = TypeVar('T')


class Set(ABC, Generic[T]):
    """
    Abstract class for sets.
    """

    def __init__(self) -> None:
        self._size = 0

    def is_empty(self) -> bool:
        """Returns True if the set is empty."""
        return self._size == 0

    def size(self) -> int:
        """Returns the number of items in the set."""
        return self._size

    def __len__(self) -> int:
        """Returns the number of items in the set."""
        return self._size

    def __str__(self) -> str:
        """Default string representation using iteration."""
        return str([item for item in self])

    @abstractmethod
    def add(self, item: T) -> None:
        """Adds an item to the set."""
        pass

    @abstractmethod
    def remove(self, item: T) -> None:
        """Removes an item from the set."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Removes all items from the set."""
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator for the set."""
        pass

    @abstractmethod
    def __contains__(self, item: T) -> bool:
        """Checks if an item is in the set."""
        pass

    @abstractmethod
    def __eq__(self, other: object) -> bool:
        """Checks if two sets are equal."""
        pass

    def __ne__(self, other: object) -> bool:
        """Checks if two sets are not equal."""
        return not self.__eq__(other)

    @abstractmethod
    def union(self, other: 'Set[T]') -> 'Set[T]':
        """Returns the union of two sets."""
        pass

    @abstractmethod
    def intersection(self, other: 'Set[T]') -> 'Set[T]':
        """Returns the intersection of two sets."""
        pass

    @abstractmethod
    def difference(self, other: 'Set[T]') -> 'Set[T]':
        """Returns the difference of two sets."""

    def symmetric_difference(self, other: 'Set[T]') -> 'Set[T]':
        """Returns the symmetric difference of two sets."""
        return self.union(other).difference(self.intersection(other))

    @abstractmethod
    def subset(self, other: 'Set[T]') -> bool:
        """Checks if the set is a subset of another set."""
        pass

    @abstractmethod
    def superset(self, other: 'Set[T]') -> bool:
        """Checks if the set is a superset of another set."""
        pass
