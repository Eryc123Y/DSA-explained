from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from ..Linear_Structure import Linear_structure

T = TypeVar('T')


class Stack(Linear_structure, ABC, Generic[T]):
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
