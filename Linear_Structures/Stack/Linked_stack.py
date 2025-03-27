from Linear_Structures.Linked_list.SLList import SLList
from Linear_Structures.Stack.Stack import Stack
from typing import TypeVar, Generic, Iterator, Optional, Collection, Union
import unittest

T = TypeVar('T')


class Linked_stack(Stack[T], Generic[T]):

    def __init__(self, elems: Optional[Collection[T]] = None) -> None:
        """
        Initializes a stack with an optional iterable.
        """
        super().__init__()
        if elems:
            self.stack = SLList(elems)
        else:
            self.stack = SLList()
        self._size = 0 if not elems else len(elems)

    def push(self, item: T) -> None:
        self.stack.append(item)
        self._size += 1

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self._size -= 1
        return self.stack.pop()

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

    def append(self, element: T) -> None:
        return self.push(element)

    def index_of(self, element: T) -> int:
        return self.stack.index_of(element)

    def insert(self, position: int, element: T) -> None:
        raise NotImplementedError("insert not implemented for stack")

    def __len__(self) -> int:
        return len(self.stack)

    def __getitem__(self, subscript: Union[int, slice]) -> T:
        return self.stack[subscript]

    def __setitem__(self, subscript: int, element: T) -> None:
        self.stack[subscript] = element

    def __delitem__(self, index: int) -> None:
        del self.stack[index]

    def __iter__(self) -> Iterator[T]:
        return iter(self.stack)

    def __contains__(self, element: T) -> bool:
        return element in self.stack

    def __str__(self) -> str:
        return str(self.stack)

    def clear(self) -> None:
        self._size = 0
        self.stack.clear()

    def reverse(self) -> None:
        self.stack.reverse()


class TestLinkedStack(unittest.TestCase):

    def setUp(self):
        self.empty_stack = Linked_stack()
        self.stack = Linked_stack([1, 2, 3])

    def test_constructor(self):
        # Test empty constructor
        stack = Linked_stack()
        self.assertEqual(len(stack), 0)
        self.assertTrue(stack.is_empty())

        # Test constructor with iterable
        stack = Linked_stack([1, 2, 3])
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
        stack = Linked_stack()
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

    def test_insertion_operations(self):
        with self.assertRaises(NotImplementedError):
            self.stack.insert(0, 4)

    def test_getitem(self):
        self.assertEqual(self.stack[0], 1)
        self.assertEqual(self.stack[1], 2)
        self.assertEqual(self.stack[2], 3)
        self.assertEqual(self.stack[-1], 3)  # Test negative indexing

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
        self.assertEqual(self.stack[0], 3)
        self.assertEqual(self.stack[1], 2)
        self.assertEqual(self.stack[2], 1)
        self.assertEqual(self.stack.peek(), 1)

    def test_size_tracking(self):
        stack = Linked_stack()
        self.assertEqual(stack._size, 0)

        stack.push(1)
        self.assertEqual(stack._size, 1)

        stack.push(2)
        self.assertEqual(stack._size, 2)

        stack.pop()
        self.assertEqual(stack._size, 1)

        stack.clear()
        self.assertEqual(stack._size, 0)


if __name__ == '__main__':
    unittest.main()
