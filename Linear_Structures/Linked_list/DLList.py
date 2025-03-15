from typing import TypeVar, Iterator, Optional, Collection, Generic, Union, Any, Generator
from .Linked_list import Linked_list
import unittest

T = TypeVar('T')


class _DLNode(Generic[T]):
    """
    Node class for doubly linked lists.
    """

    def __init__(self, data: T = None):
        """
        Initialize a node with a given data value.
        """
        self.data = data
        self.next = None
        self.prev = None


class DLList(Linked_list, Generic[T]):
    """
    Doubly Linked List class.
    """

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """
        Initialize a doubly linked list.
        """
        super().__init__()
        if elements:
            for element in elements:
                self.append(element)
            self._size = len(elements)

    def append(self, element: T) -> None:
        """
        Append an element to the doubly linked list.
        """
        new_node = _DLNode(element)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def pop(self) -> T:
        """
        Remove and return the last element of the doubly linked list.
        """
        if self.is_empty():
            raise IndexError("The doubly linked list is empty.")
        elem = self.tail.data
        del self[-1]
        return elem

    def _traverse_helper(self, index: int) -> _DLNode[T]:
        """
        A built-in helper method to traverse the singly linked list and get the node at the given index.
        Optimised for double linked list, chooses the direction of traversal based on the index.
        """
        if abs(index) >= self._size:
            raise IndexError("Index out of range")
        if index < 0:
            index += self._size

            # Optimize traversal by choosing direction
        if index <= self._size // 2:
            # Traverse from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                current = current.prev

        return current

    def _traverse_helper_yield(self, index: int) -> Generator[Union[_DLNode[Any], Any], Any, Union[_DLNode[Any], Any]]:
        if abs(index) >= self._size:
            raise IndexError("Index out of range")
        if index < 0:
            index += self._size

        # Optimize traversal by choosing direction
        if index <= self._size // 2:
            # Traverse from head
            current = self.head
            for _ in range(index):
                yield current
                current = current.next
        else:
            # Traverse from tail
            current = self.tail
            for _ in range(self._size - 1 - index):
                yield current
                current = current.prev
        return current

    def index_of(self, element: T) -> int:
        """
        Returns the index of the first occurrence of the element in the doubly linked list.
        """
        i = 0
        for item in self:
            if item == element:
                return i
            i += 1
        return -1

    def insert(self, position: int, element: T) -> None:
        """
        Insert an element at the given index.
        """
        if abs(position) > self._size:
            raise IndexError("Index out of range.")
        new_node = _DLNode(element)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.is_empty():
                self.tail = new_node
        else:
            target = self._traverse_helper(position)
            new_node.prev = target.prev
            new_node.next = target
            target.prev.next = new_node
            target.prev = new_node

        self._size += 1

    def __len__(self) -> int:
        return self._size

    def __getitem__(self, interval: Union[int, slice]) -> Union[T, 'DLList[T]']:
        """
        Returns the element at the given index.
        """
        if isinstance(interval, slice):
            start, stop, step = interval.indices(self._size)
            result = DLList()

            # Optimization for forward traversal with step=1
            if start < stop and step == 1:
                current = self._traverse_helper(start)
                for _ in range(stop - start):
                    result.append(current.data)
                    current = current.next
            elif start > stop and step == -1:
                current = self._traverse_helper(start)
                for _ in range(start - stop):
                    result.append(current.data)
                    current = current.prev
            else:
                for i in range(start, stop, step):
                    result.append(self._traverse_helper(i).data)

            return result

        # Handle single index
        return self._traverse_helper(interval).data

    def __setitem__(self, index: int, element: T) -> None:
        """
        Sets the element at the given index.
        """
        if abs(index) >= self._size:
            raise IndexError("Index out of range.")
        self._traverse_helper(index).data = element

    def __delitem__(self, index: int) -> None:
        if self.is_empty():
            raise IndexError("The doubly linked list is empty.")
        if abs(index) >= self._size:
            raise IndexError("Index out of range.")
        if index < 0:
            index += self._size

        if self._size == 1:
            self.clear()
            return

        node = self._traverse_helper(index)
        if node is self.head:
            self.head = node.next
            if self.head:
                self.head.prev = None
        elif node is self.tail:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self._size -= 1

    def __iter__(self) -> Iterator[T]:
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __contains__(self, element: T) -> bool:
        for item in self:
            if item == element:
                return True
        return False

    def __str__(self) -> str:
        """
        Returns a string representation of the doubly linked list.
        """
        return '[' + ', '.join(str(item) for item in self) + ']' if self._size > 0 else '[]'

    def clear(self) -> None:
        self._size = 0
        self.head = None
        self.tail = None

    def reverse(self) -> None:
        if self.is_empty() or self._size == 1:
            return
        current = self.head
        prev = None
        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head


class TestDLList(unittest.TestCase):

    def setUp(self):
        self.list = DLList([1, 2, 3])

    def test_init(self):
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[0], 1)

        empty_list = DLList()
        self.assertEqual(len(empty_list), 0)

    def test_append(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[3], 4)

    def test_pop(self):
        value = self.list.pop()
        self.assertEqual(value, 3)
        self.assertEqual(len(self.list), 2)

        with self.assertRaises(IndexError):
            empty = DLList()
            empty.pop()

    def test_index_of(self):
        self.assertEqual(self.list.index_of(1), 0)
        self.assertEqual(self.list.index_of(4), -1)  # Not in list

    def test_insert(self):
        self.list.insert(0, 0)  # At beginning
        self.assertEqual(self.list[0], 0)

        self.list.insert(2, 10)  # In middle
        self.assertEqual(self.list[2], 10)

        with self.assertRaises(IndexError):
            self.list.insert(10, 30)

    def test_getitem(self):
        # Positive indexing
        self.assertEqual(self.list[0], 1)

        # Negative indexing
        self.assertEqual(self.list[-1], 3)

        with self.assertRaises(IndexError):
            _ = self.list[3]

    def test_slice(self):
        long_list = DLList([1, 2, 3, 4, 5, 6])

        # Positive step
        slice_result = long_list[1:4]
        self.assertEqual(len(slice_result), 3)
        self.assertEqual(slice_result[0], 2)

        # Negative step
        slice_result = long_list[4:1:-1]
        self.assertEqual(len(slice_result), 3)
        self.assertEqual(slice_result[0], 5)

        # Step > 1
        slice_result = long_list[0:6:2]
        self.assertEqual(len(slice_result), 3)
        self.assertEqual(slice_result[1], 3)

    def test_setitem(self):
        self.list[1] = 20
        self.assertEqual(self.list[1], 20)

        self.list[-1] = 30
        self.assertEqual(self.list[2], 30)

    def test_delitem(self):
        # Delete middle element
        del self.list[1]
        self.assertEqual(len(self.list), 2)
        self.assertEqual(str(self.list), '[1, 3]')

        # Delete using negative index
        del self.list[-1]
        self.assertEqual(len(self.list), 1)

    def test_contains(self):
        self.assertTrue(1 in self.list)
        self.assertFalse(4 in self.list)

        self.list[1] = 20
        self.assertTrue(20 in self.list)
        self.assertFalse(2 in self.list)

    def test_str(self):
        self.assertEqual(str(self.list), '[1, 2, 3]')

        empty = DLList()
        self.assertEqual(str(empty), '[]')

    def test_clear(self):
        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())

    def test_reverse(self):
        self.list.reverse()
        self.assertEqual(str(self.list), '[3, 2, 1]')

        # Test edge cases
        single = DLList([5])
        single.reverse()
        self.assertEqual(str(single), '[5]')

        empty = DLList()
        empty.reverse()
        self.assertEqual(str(empty), '[]')

    def test_iterator(self):
        items = [item for item in self.list]
        self.assertEqual(items, [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
