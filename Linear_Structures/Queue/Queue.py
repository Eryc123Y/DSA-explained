from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ..Linear_Structure import Linear_structure

T = TypeVar('T')

class Queue(Linear_structure, ABC, Generic[T]):
    """
    Abstract class for queues.
    """

    @abstractmethod
    def enqueue(self, item: T) -> None:
        """
        Enqueues an item to the queue.
        """
        pass

    @abstractmethod
    def dequeue(self) -> T:
        """
        Dequeues an item from the queue.
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """
        Returns the front item from the queue.
        """
        pass
    
    @abstractmethod
    def is_empty(self) -> bool:
        """
        Returns True if the queue is empty, False otherwise.
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """
        Returns the number of items in the queue.
        """
        pass
    
    
    def __len__(self):
        return self.size()
    
    
    @abstractmethod
    def __str__(self):
        """
        Returns a string representation of the queue.
        """
        return str(self._items)
    
    @abstractmethod
    def __iter__(self):
        """
        This is a reference implementation that concrete classes should override.
        It creates a temporary copy to avoid modifying the original queue.
        """
        pass
