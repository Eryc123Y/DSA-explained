from ..Vector import Vector
from .Stack import Stack
from typing import TypeVar, Generic, Iterator, Optional, Collection
import unittest

T = TypeVar('T')


class List_stack(Stack, Generic[T]):
    """
    Stack class implemented using a list (vector).
    """

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """
        Initializes a stack with an optional iterable.
        We treat the rhs as the top
        """
        super().__init__()
        # Initialize with a non-empty Vector to ensure it has capacity
        if elements is None:
            # Use a dummy element to create capacity, then remove it
            self.stack = Vector([None])
            self.stack.pop()
        else:
            self.stack = Vector(elements)
            self.size = len(elements)

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

    def append(self, element: T) -> None:
        return self.push(element)

    def index_of(self, element: T) -> int:
        for i in range(self.size):
            if self.stack[i] == element:
                return i
        return -1

    def insert(self, position: int, element: T) -> None:
        raise NotImplementedError("Insert method is not supported in stacks.")

    def __len__(self) -> int:
        return len(self.stack)

    def __getitem__(self, index: int) -> T:
        return self.stack[index]

    def __setitem__(self, index: int, element: T) -> None:
        raise NotImplementedError("Insert method is not supported in stacks.")

    def __delitem__(self, index: int) -> None:
        raise NotImplementedError("Delete method is not supported in stacks.")

    def __iter__(self) -> Iterator[T]:
        return iter(self.stack)

    def __contains__(self, element: T) -> bool:
        return element in self.stack

    def __str__(self) -> str:
        return str(self.stack)

    def clear(self) -> None:
        """
        Clears the stack.
        """
        self.stack.clear()
        self.size = 0

    def reverse(self) -> None:
        self.stack.reverse()


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

    def test_append(self):
        self.empty_stack.append(1)
        self.assertEqual(len(self.empty_stack), 1)
        self.assertEqual(self.empty_stack.peek(), 1)

    def test_index_of(self):
        self.assertEqual(self.stack.index_of(1), 0)
        self.assertEqual(self.stack.index_of(2), 1)
        self.assertEqual(self.stack.index_of(3), 2)
        self.assertEqual(self.stack.index_of(4), -1)

    def test_unsupported_operations(self):
        with self.assertRaises(NotImplementedError):
            self.stack.insert(0, 4)

        with self.assertRaises(NotImplementedError):
            self.stack[0] = 4

        with self.assertRaises(NotImplementedError):
            del self.stack[0]

    def test_getitem(self):
        self.assertEqual(self.stack[0], 1)
        self.assertEqual(self.stack[1], 2)
        self.assertEqual(self.stack[2], 3)

    def test_iter(self):
        items = [item for item in self.stack]
        self.assertEqual(items, [1, 2, 3])

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

    def test_reverse(self):
        self.stack.reverse()
        self.assertEqual(str(self.stack), "[3, 2, 1]")
        self.assertEqual(self.stack.peek(), 1)


if __name__ == '__main__':
    unittest.main()