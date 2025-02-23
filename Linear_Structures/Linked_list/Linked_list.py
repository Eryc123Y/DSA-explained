from abc import ABC
from typing import TypeVar
from Linear_Structures.Linear_Structure import Linear_structure

T = TypeVar('T')


class Linked_list(Linear_structure[T], ABC):
    """
    Linked list Base class.
    """

    def __init__(self):
        """
        Initialize a linked list.
        """
        super().__init__()
        self.head = None
        self.tail = None



