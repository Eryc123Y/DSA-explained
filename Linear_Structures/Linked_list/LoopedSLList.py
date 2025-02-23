from typing import TypeVar
from .SLList import SLList
import unittest

T = TypeVar('T')


class LoopedSLList(SLList):
    def append(self, element: T) -> None:
        super().append(element)
        self.tail.next = self.head  # Maintain the loop

    def __delitem__(self, index: int) -> None:
        super().__delitem__(index)
        if not self.is_empty():
            self.tail.next = self.head  # Maintain the loop

    def clear(self) -> None:
        super().clear()
        self.tail = None  # Clear the loop

    def __str__(self):
        if self.is_empty():
            return '[]'
        result = []
        current = self.head
        for _ in range(self.size):
            result.append(str(current.data))
            current = current.next
        return '[' + ', '.join(result) + ']'


class TestLoopedSLList(unittest.TestCase):

    def setUp(self):
        self.list = LoopedSLList([1, 2, 3])

    def test_append(self):
        self.list.append(4)
        self.assertEqual(len(self.list), 4)
        self.assertEqual(self.list[-1], 4)
        self.assertEqual(self.list.tail.next, self.list.head)

    def test_delitem(self):
        del self.list[1]
        self.assertEqual(len(self.list), 2)
        self.assertEqual(self.list[1], 3)
        self.assertEqual(self.list.tail.next, self.list.head)

    def test_clear(self):
        self.list.clear()
        self.assertEqual(len(self.list), 0)
        self.assertIsNone(self.list.tail)

    def test_str(self):
        self.assertEqual(str(self.list), '[1, 2, 3]')
        self.list.append(4)
        self.assertEqual(str(self.list), '[1, 2, 3, 4]')

    def test_loop(self):
        current = self.list.head
        for _ in range(len(self.list) * 2):  # Traverse twice the length to ensure looping
            current = current.next
        self.assertEqual(current, self.list.head)


if __name__ == '__main__':
    unittest.main()
