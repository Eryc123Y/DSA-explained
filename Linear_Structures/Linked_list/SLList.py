from typing import TypeVar, Iterator, Optional, Iterable, Collection, Generic, Union
from .Linked_list import Linked_list
import unittest

T = TypeVar('T')


class Node(Generic[T]):
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


class SLList(Linked_list, Generic[T]):

    def __init__(self, elements: Optional[Collection[T]] = None):
        """
        Initialize a singly linked list with a list of elements.

        Parameters:
            elements (Optional[Iterable[T]]): A iterable of initial elements to populate the singly linked list.
        """
        super().__init__()
        if elements:
            for element in elements:
                self.append(element)
            self._size = len(elements)

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
        self._size += 1

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("The singly linked list is empty.")
        elem = self.tail.data
        del self[-1]
        return elem

    def index_of(self, element: T) -> int:
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
        if index < 0 or index > self._size:
            raise IndexError("Index out of range.")
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            target = self._traverse_helper(index - 1)
            new_node.next = target.next
            target.next = new_node
        self._size += 1

    def __len__(self) -> int:
        return self._size

    def _traverse_helper(self, index: int) -> Node:
        """
        A built-in helper method to traverse the singly linked list and get the node at the given index.
        """
        if index < -self._size or index >= self._size:
            raise IndexError("Index out of range.")
        current = self.head
        for i in range(index):
            current = current.next
        return current

    def __getitem__(self, interval: Union[int, slice]) -> Union[T, 'SLList[T]']:
        """
        Get an item or slice from the linked list.

        Args:
            interval: Integer index or slice object

        Returns:
            Single item or new linked list with sliced items

        Raises:
            IndexError: If index is out of range
        """
        # Handle slices
        if isinstance(interval, slice):
            start, stop, step = interval.indices(self._size)
            result = SLList()

            # Optimization for forward traversal with step=1
            if start < stop and step == 1:
                current = self.head
                # Skip to start position
                for _ in range(start):
                    current = current.next
                # Collect items sequentially
                for _ in range(stop - start):
                    result.append(current.data)
                    current = current.next
            else:
                # For reverse or stepped slices
                for i in range(start, stop, step):
                    result.append(self._traverse_helper(i).data)

            return result

        # Handle single index access
        if interval < 0:
            interval += self._size

        return self._traverse_helper(interval).data

    def __setitem__(self, index: int, element: T) -> None:
        """
        Set the element at the given index.
        """
        if index < 0:
            index += self._size
        self._traverse_helper(index).data = element

    def __delitem__(self, index: int) -> None:
        if index < 0:
            index += self._size

        if index == 0:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            target = self._traverse_helper(index - 1)
            target.next = target.next.next
            if target.next is None:
                self.tail = target
        self._size -= 1

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
        return '[' + ', '.join(str(item) for item in self) + ']' if self._size > 0 else '[]'

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._size = 0

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
        self.assertEqual(self.list.index_of(2), 1)
        self.assertEqual(self.list.index_of(4), -1)

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
