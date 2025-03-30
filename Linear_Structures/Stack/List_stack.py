from ..Vector import Vector
from .Stack import Stack
from typing import TypeVar, Generic, Iterator, Optional, Collection
import unittest

T = TypeVar('T')


class List_stack(Stack, Generic[T]):
    """
    Stack class implemented using a list (vector).
    """

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.
        """
        return len(self.stack)

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """
        Initializes a stack with an optional iterable.
        We treat the rhs as the top
        """
        # Initialize with a non-empty Vector to ensure it has capacity
        if elements is None:
            # Use a dummy element to create capacity, then remove it
            self.stack = Vector()
            self._size = 0
        else:
            self.stack = Vector(elements)
            self._size = len(elements)

    def push(self, item: T) -> None:
        """
        Pushes an item to the top of the stack.
        """
        self.stack.append(item)

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.
        """
        # check is already done in vector
        try:
            res = self.stack.pop()
        except IndexError:
            raise IndexError("pop from empty stack")
        return res

    def is_empty(self) -> bool:
        return self.stack.is_empty()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def __contains__(self, element: T) -> bool:
        return element in self.stack

    def __str__(self) -> str:
        return str(self.stack)

    def clear(self) -> None:
        """
        Clears the stack.
        """
        self.stack.clear()
        self._size = 0


class TestListStack(unittest.TestCase):

    def setUp(self):
        self.empty_stack = List_stack()
        self.stack = List_stack([1, 2, 3])

    def test_constructor(self):
        # Test empty constructor
        stack = List_stack()
        self.assertEqual(len(stack), 0)
        self.assertTrue(stack.is_empty())

        # Test constructor with iterable
        stack = List_stack([1, 2, 3])
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.peek(), 3)

    def test_push(self):
        self.empty_stack.push(1)
        self.assertEqual(len(self.empty_stack), 1)
        self.assertEqual(self.empty_stack.peek(), 1)

        self.empty_stack.push(2)
        self.assertEqual(len(self.empty_stack), 2)
        self.assertEqual(self.empty_stack.peek(), 2)

    def test_pop(self):
        val = self.stack.pop()
        self.assertEqual(val, 3)
        self.assertEqual(len(self.stack), 2)

        with self.assertRaises(IndexError):
            self.empty_stack.pop()

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(len(self.stack), 3)

        with self.assertRaises(IndexError):
            self.empty_stack.peek()

    def test_lifo_behavior(self):
        stack = List_stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())

    def test_contains(self):
        self.assertTrue(1 in self.stack)
        self.assertTrue(2 in self.stack)
        self.assertTrue(3 in self.stack)
        self.assertFalse(4 in self.stack)

    def test_str(self):
        self.assertEqual(str(self.stack), "[1, 2, 3]")

    def test_clear(self):
        self.stack.clear()
        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
