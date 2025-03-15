from typing import TypeVar, Optional, Collection, Generic
from .DLList import DLList, _DLNode
import unittest

T = TypeVar('T')


class LoopedDLList(DLList, Generic[T]):
    """
    Looped Doubly Linked List class.
    """

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """
        Initialize a looped doubly linked list.
        """
        super().__init__(elements)
        if not self.is_empty():
            self.tail.next = self.head
            self.head.prev = self.tail

    def append(self, element: T) -> None:
        """
        Append an element to the looped doubly linked list.
        """
        super().append(element)
        if not self.is_empty():
            self.tail.next = self.head
            self.head.prev = self.tail

    def insert(self, position: int, element: T) -> None:
        """
        Insert an element at the given index.
        """
        super().insert(position, element)
        if not self.is_empty():
            self.tail.next = self.head
            self.head.prev = self.tail

    def _traverse_helper(self, index: int) -> '_DLNode[T]':
        """
        Override to handle circular indexing for looped list.
        """
        if self.is_empty():
            raise IndexError("The looped list is empty")

        # Handle any integer index using modulo arithmetic
        if index < 0 or index >= self._size:
            index = index % self._size

        # Use the optimized traversal from the parent class
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

    def __delitem__(self, index: int) -> None:
        """
        Delete the element at the given index.
        """
        super().__delitem__(index)
        if not self.is_empty():
            self.tail.next = self.head
            self.head.prev = self.tail

    def reverse(self) -> None:
        """
        Reverse the looped doubly linked list.
        """
        super().reverse()
        if not self.is_empty():
            self.tail.next = self.head
            self.head.prev = self.tail

    def __str__(self) -> str:
        """
        Return a string representation of the looped doubly linked list.
        """
        if self.is_empty():
            return '[]'

        result = []
        current = self.head
        for _ in range(self._size):
            result.append(str(current.data))
            current = current.next
        return '[' + ', '.join(result) + ']'


class TestLoopedDLList(unittest.TestCase):
    def setUp(self):
        self.list = LoopedDLList([1, 2, 3])
        self.empty = LoopedDLList()
        self.single = LoopedDLList([5])

    def test_init(self):
        # Test normal initialization
        self.assertEqual(len(self.list), 3)
        self.assertEqual(self.list[0], 1)

        # Test loop integrity
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        # Test empty list
        self.assertEqual(len(self.empty), 0)

        # Test single element list loop integrity
        self.assertEqual(len(self.single), 1)
        self.assertEqual(self.single.head.prev, self.single.tail)
        self.assertEqual(self.single.tail.next, self.single.head)
        self.assertEqual(self.single.head, self.single.tail)

    def test_append(self):
        original_tail = self.list.tail
        self.list.append(4)

        # Test normal append functionality
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[3], 4)

        # Test loop integrity
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        # Test appending to empty list
        self.empty.append(1)
        self.assertEqual(len(self.empty), 1)
        self.assertEqual(self.empty.head, self.empty.tail)
        self.assertEqual(self.empty.head.prev, self.empty.tail)
        self.assertEqual(self.empty.tail.next, self.empty.head)

    def test_insert(self):
        self.list.insert(0, 0)  # Insert at beginning
        self.assertEqual(self.list[0], 0)
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        self.list.insert(2, 10)  # Insert in middle
        self.assertEqual(self.list[2], 10)
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

    def test_delitem(self):
        # Delete middle element
        del self.list[1]
        self.assertEqual(len(self.list), 2)
        self.assertEqual(str(self.list), '[1, 3]')
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        # Delete first element
        del self.list[0]
        self.assertEqual(len(self.list), 1)
        self.assertEqual(str(self.list), '[3]')
        self.assertEqual(self.list.head, self.list.tail)
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        # Delete last element
        del self.list[0]
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())

    def test_reverse(self):
        self.list.reverse()
        self.assertEqual(str(self.list), '[3, 2, 1]')
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)

        # Test edge cases
        self.single.reverse()
        self.assertEqual(str(self.single), '[5]')
        self.assertEqual(self.single.head.prev, self.single.tail)
        self.assertEqual(self.single.tail.next, self.single.head)

    def test_circular_traversal(self):
        # Create helper to test circular behavior
        def traverse_forward(steps):
            current = self.list.head
            result = []
            for _ in range(steps):
                result.append(current.data)
                current = current.next
            return result

        # Test traversing beyond list length
        self.assertEqual(traverse_forward(6), [1, 2, 3, 1, 2, 3])
        self.assertEqual(traverse_forward(4), [1, 2, 3, 1])

    def test_clear(self):
        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertTrue(self.list.is_empty())
        self.assertIsNone(self.list.head)
        self.assertIsNone(self.list.tail)

    def test_getitem_with_negative_indices(self):
        # Test negative indexing works properly in looped list
        self.assertEqual(self.list[-1], 3)
        self.assertEqual(self.list[-2], 2)
        self.assertEqual(self.list[-3], 1)

    def test_pop(self):
        value = self.list.pop()
        self.assertEqual(value, 3)
        self.assertEqual(len(self.list), 2)

        # Check loop integrity after pop
        self.assertEqual(self.list.head.prev, self.list.tail)
        self.assertEqual(self.list.tail.next, self.list.head)


if __name__ == '__main__':
    unittest.main()
