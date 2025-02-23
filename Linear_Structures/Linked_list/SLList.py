from typing import TypeVar, Iterator, Optional, Iterable
from .Linked_list import Linked_list
import unittest

T = TypeVar('T')


class Node:
    """
    Node class for linked lists.
    """

    def __init__(self, data: T = None):
        """
        Initialize a node with a given data value.

        Parameters:
            data (T): The data value to store in the node.
        """
        self.data = data
        self.next = None


class SLList(Linked_list):

    def __init__(self, elements: Optional[Iterable[T]] = None):
        """
        Initialize a singly linked list with a list of elements.

        Parameters:
            elements (Optional[Iterable[T]]): A iterable of initial elements to populate the singly linked list.
        """
        super().__init__()
        if elements:
            for element in elements:
                self.append(element)
            self.size = len(elements)

    def append(self, element: T) -> None:
        """
        Append an element to the single linked list.
        """
        # Create a new node with the element.
        new_node = Node(element)
        # if is empty, set the head and tail to the new node.
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        # else, only append the new node to the tail and update the tail.
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("The singly linked list is empty.")
        elem = self.tail.data
        del self[-1]
        return elem

    def index(self, element: T) -> int:
        i = 0
        for item in self:
            if item == element:
                return i
            i += 1
        return -1

    def insert(self, index: int, element: T) -> None:
        """
        Insert an element at the given index.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range.")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            target = self._traverse_helper(index - 1)
            new_node.next = target.next
            target.next = new_node
        self.size += 1

    def __len__(self) -> int:
        return self.size

    def _traverse_helper(self, index: int) -> Node:
        """
        A built-in helper method to traverse the singly linked list and get the node at the given index.
        """
        if index < -self.size or index >= self.size:
            raise IndexError("Index out of range.")
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def __getitem__(self, index):
        if isinstance(index, slice):
            start, stop, step = index.indices(self.size)
            result = SLList()
            for i in range(start, stop, step):
                result.append(self._traverse_helper(i).data)
            return result
        if index < 0:
            index += self.size
        return self._traverse_helper(index).data

    def __setitem__(self, index: int, element: T) -> None:
        """
        Set the element at the given index.
        """
        if index < 0:
            index += self.size
        self._traverse_helper(index).data = element

    def __delitem__(self, index: int) -> None:
        if index < 0:
            index += self.size

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            target = self._traverse_helper(index - 1)
            target.next = target.next.next
            if target.next is None:
                self.tail = target
        self.size -= 1

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __contains__(self, element: T) -> bool:
        # the iterator returns the value of the nodes
        for item in self:
            if item == element:
                return True
        return False

    def __str__(self):
        return '[' + ', '.join(str(item) for item in self) + ']' if self.size > 0 else '[]'

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def reverse(self) -> None:
        if len(self) == 1 or self.is_empty():
            return
        prev = None
        current = self.head
        self.tail = current
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


class TestSLList(unittest.TestCase):

    def setUp(self):
        self.list = SLList([1, 2, 3])

    def test_append(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[-1], 4)

    def test_pop(self):
        value = self.list.pop()
        self.assertEqual(value, 3)
        self.assertEqual(len(self.list), 2)

    def test_index(self):
        self.assertEqual(self.list.index(2), 1)
        self.assertEqual(self.list.index(4), -1)

    def test_insert(self):
        self.list.insert(1, 5)
        self.assertEqual(self.list[1], 5)
        self.assertEqual(len(self.list), 4)

    def test_getitem(self):
        self.assertEqual(self.list[0], 1)
        self.assertEqual(self.list[2], 3)

    def test_setitem(self):
        self.list[1] = 6
        self.assertEqual(self.list[1], 6)

    def test_delitem(self):
        del self.list[1]
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[1], 3)

    def test_contains(self):
        self.assertTrue(2 in self.list)
        self.assertFalse(4 in self.list)

    def test_str(self):
        self.assertEqual(str(self.list), '[1, 2, 3]')

    def test_clear(self):
        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertEqual(str(self.list), '[]')

    def test_reverse(self):
        self.list.reverse()
        self.assertEqual(str(self.list), '[3, 2, 1]')


if __name__ == '__main__':
    unittest.main()
