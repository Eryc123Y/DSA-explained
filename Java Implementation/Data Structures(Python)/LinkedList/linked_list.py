from __future__ import annotations

from node import Node, T, Generic
from typing import Union, List
import node

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class LinkedList(Generic[T]):
    """ Partial List ADT implemented with linked nodes. """
    def __init__(self) -> None:
        """ Linked-list object initialiser. """
        self.head = None
        self.length = 0
    
    def append(self, item: T) -> None:
        """ Insert an item at the end of the list. """
        self.insert(self.length, item)  # Use insert to append
        
    def add_first(self, item: T) -> None:
        """ Insert an item at the beginning of the list. """
        self.insert(0, item)
        
    def remove(self, item: T) -> None:
        """ Remove the first occurrence of item from the list."""
        self.head, removed = node.remove(self.head, item)
        if removed:
            self.length -= 1
            
            
    def remove_all(self, item: T) -> None:
        """ Remove all occurrences of item from the list."""
        while item in self:
            self.remove(item)
        
    def index(self, item: T) -> Union[int, None]:
        """ Returns the index of the first occurrence of item in the list. """
        current = self.head
        index = 0
        while current is not None:
            if current.item == item:
                return index
            current = current.next
            index += 1
        return None
    
    def _get(self, index: int) -> Union[T, None]:
        """ Returns the item at the given index. """
        current = self.head
        for _ in range(index):
            if current is None:
                return None
            current = current.next
        return current.item if current is not None else None
    
    def _set(self, index: int, item: T) -> None:
        """ Sets the item at the given index. """
        current = self.head
        for _ in range(index):
            if current is None:
                return
            current = current.next
        if current is not None:
            current.item = item
    
    
    def shift_right(self, step: int = 1) -> None:
        """ Shift the items in the list to the right by some step number. """
        self.head = node.shift(self.head, self.length, step)
        
    def shift_left(self, step: int = 1) -> None:
        """ Shift the items in the list to the left by some step number. """
        self.head = node.shift(self.head, self.length, -step)
        
        
    def insert(self, index: int, item: T) -> None:
        """ Insert an item at a given position. """
        self.head = node.insert(self.head, index, item)
        self.length += 1
        
    def to_list(self) -> List[T]:
        """ Returns a list with the items in the linked list. """
        return [item for item in self]
            
    def reverse(self) -> None:
        self.head = node.reverse(self.head)
    
    @property
    def is_empty(self) -> bool:
        """ Returns True if the list is empty. """
        return self.head is None
    
    @property
    def size(self) -> int:
        """ Returns the number of items in the list. """
        return self.length
    
        
    def __contains__(self, item: T) -> bool:
        """ Returns True if the item is in the list. """
        return any(current_item == item for current_item in self)

    def __iter__(self) -> LinkedListIterator[T]:
        """ Magic method. Creates and returns an iterator for the list. """
        return LinkedListIterator(self.head)
    
    def __setitem__(self, index: int, item: T) -> None:
        return self._set(index, item)
    
    def __getitem__(self, index: int) -> T:
        return self._get(index)
        
    
    def __str__(self) -> str:
        return ' -> '.join(str(item) for item in self)

class LinkedListIterator(Generic[T]):
    """ A full-blown iterator for class LinkedList.

        Attributes:
            current (Node[T]): the node whose item will be returned next
    """
    def __init__(self, node: Node[T]) -> None:
        """ Initialises self.current to the node given as input. """
        self.current = node

    def __iter__(self) -> LinkedListIterator[T]:
        """ Returns itself, as required to be iterable. """
        return self

    def __next__(self) -> T:
        """ Returns the current item and moves to the next node.
            :raises StopIteration: if the current item does not exist
        """
        if self.current is None:
            raise StopIteration
        else:
            item = self.current.item
            self.current = self.current.next
            return item

if __name__ == '__main__':
    list = LinkedList()
    for i in range(5):
        list.append(2 * i)
    
    print("Initial list:")
    print(list)
    
    list.remove(2)
    print("After removing 2:")
    print(list)
    
    list.insert(1, 10)
    print("After inserting 10 at index 1:")
    print(list)
    
    list[0] = 100
    print("After setting 100 at index 0:")
    print(list)
    
    for i in range(list.length):
        print(f"Item at index {i}: {list[i]}")
        
    print("Now we shift right by 2:")
    list.shift_right(2)
    print(list)
    
    print("Now we shift left by 1:")
    list.shift_left(1)
    print(list)
