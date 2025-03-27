from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator, Optional, Collection
from ..Vector import Vector
T = TypeVar('T')


class Queue(ABC, Generic[T]):
    """
    Abstract class for queues.
    """

    def __init__(self) -> None:
        self._size = 0

    def is_empty(self) -> bool:
        """Returns True if the queue is empty."""
        return self._size == 0

    def size(self) -> int:
        """Returns the number of items in the queue."""
        return self._size

    def __len__(self) -> int:
        """Returns the number of items in the queue."""
        return self._size

    def __str__(self) -> str:
        """Default string representation using iteration."""
        return str([item for item in self])

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """Adds an item to the queue."""
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """Removes and returns the front item from the queue."""
        pass

    @abstractmethod
    def peek(self) -> T:
        """Returns the front item without removing it."""
        pass

    @abstractmethod
    def clear(self) -> None:
        """Removes all items from the queue."""
        pass

    @abstractmethod
    def __iter__(self) -> Iterator[T]:
        """Returns an iterator for the queue."""
        pass
