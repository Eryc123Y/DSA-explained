from symtable import Class

from ..Linked_list.SLList import SLList
from .Stack import Stack
from typing import TypeVar, Generic, Iterator, Optional, Collection
import unittest

T = TypeVar('T')


class Linked_stack(Stack[T], Generic[T]):

    def __init__(self, elems: Optional[Collection[T]]) -> None:
        """
        Initializes a stack with an optional iterable.
        """
        super().__init__()
        if elems:
            self.stack = SLList(elems)
        else:
            self.stack = SLList()

    def push(self, item: T) -> None:
        self.stack.append(item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self) -> T:
        return self.stack[-1]

    def append(self, element: T) -> None:
        return self.push(element)

    def index_of(self, element: T) -> int:
        return self.stack.index_of(element)

    def insert(self, position: int, element: T) -> None:
        raise IndexError("insert not implemented for stack")

    def __len__(self) -> int:
        return len(self.stack)

    def __getitem__(self, subscript: Optional[int, slice]) -> T:
        return self.stack[subscript]

    def __setitem__(self, subscript: int, element: T) -> None:
        self.stack[subscript] = element

    def __delitem__(self, index: int) -> None:
        del self.stack[index]

    def __iter__(self) -> Iterator[T]:
        return iter(self.stack)

    def __contains__(self, element: T) -> bool:
        return element in self.stack

    def __str__(self) -> str:
        return str(self.stack)

    def clear(self) -> None:
        self.stack.clear()

    def reverse(self) -> None:
        self.stack.reverse()
