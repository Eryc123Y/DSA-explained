from abc import ABC, abstractmethod
from typing import TypeVar, Iterator, Generic
from ctypes import py_object
from Linear_Structure import Linear_structure

T = TypeVar('T')


class Array(Linear_structure, Generic[T]):

    def __init__(self, capacity: int = 10) -> None:
        self.super().__init__()
        self.capacity = capacity
        # initialize the array with None
        self.array = (py_object * self.capacity)()
        self.array = [None] * self.capacity

    def is_full(self) -> bool:
        return self.size == self.capacity

    def append(self, element: T) -> None:
        pass

    def pop(self) -> T:
        pass

    def __len__(self) -> int:
        pass

    def __getitem__(self, index: int) -> T:
        pass

    def __setitem__(self, index: int, element: T) -> None:
        pass

    def __delitem__(self, index: int) -> None:
        pass

    def __iter__(self) -> Iterator[T]:
        pass

    def __str__(self):
        pass

    def clear(self) -> None:
        pass


