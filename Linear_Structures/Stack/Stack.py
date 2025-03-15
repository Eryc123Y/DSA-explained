from abc import ABC, abstractmethod
from typing import TypeVar, Iterator, Generic
from Linear_Structure import Linear_structure

T = TypeVar('T')

class Stack(Linear_structure, Generic[T]):
    """
    Abstract class for stacks.
    """
    