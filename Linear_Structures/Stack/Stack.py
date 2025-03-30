from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Iterator

T = TypeVar('T')


class Stack(ABC, Generic[T]):
    """
    Abstract class for stacks.
    """

    @abstractmethod
    def push(self, item: T) -> None:
        """
        Pushes an item to the stack.
        """
        pass

    @abstractmethod
    def pop(self) -> T:
        """
        Pops an item from the stack.
        """
        pass

    @abstractmethod
    def peek(self) -> T:
        """
        Returns the top item from the stack.
        """
        pass

    @abstractmethod
    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.
        """
        pass

    @abstractmethod
    def __len__(self) -> int:
        """
        Returns the number of items in the stack.
        """
        pass

    @abstractmethod
    def __contains__(self, item0: T) -> bool:
        """
        Checks if an item is in the stack.
        """
        pass

    @abstractmethod
    def clear(self) -> None:
        """
        Removes all items from the stack.
        """
        pass
