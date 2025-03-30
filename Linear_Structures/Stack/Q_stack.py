from Linear_Structures.Stack.Stack import Stack
from Linear_Structures.Queue.SimpleQ import SimpleQ
from typing import TypeVar, Generic
import unittest

T = TypeVar('T')


class Q_stack(Stack, Generic[T]):

    def __init__(self) -> None:
        """
        Initializes an empty stack.
        """
        # the queue for major stack operations
        self.Q1 = SimpleQ()
        # the auxiliary queue
        self.Q2 = SimpleQ()
        self._size = 0

    def push(self, item: T) -> None:
        """
        Pushes an item to the stack.
        """
        # Add the new item to the auxiliary queue
        self.Q2.enqueue(item)
        # Move all items from the main queue to the auxiliary queue
        while not self.Q1.is_empty():
            self.Q2.enqueue(self.Q1.dequeue())
        # now the auxiliary queue has the new item at the front and old items at the back
        # Swap the names of the two queues
        self.Q1, self.Q2 = self.Q2, self.Q1
        self._size += 1

    def pop(self) -> T:
        """
        Removes and returns the top item from the stack.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        self._size -= 1
        return self.Q1.dequeue()

    def peek(self) -> T:
        """
        Returns the top item from the stack.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.Q1.peek()

    def is_empty(self) -> bool:
        """
        Returns True if the stack is empty, False otherwise.
        """
        return self.Q1.is_empty()

    def __len__(self) -> int:
        """
        Returns the number of items in the stack.
        """
        return self._size

    def __contains__(self, item0: T) -> bool:
        """
        Checks if an item is in the stack.
        """
        return item0 in self.Q1

    def clear(self) -> None:
        """
        Removes all items from the stack.
        """
        self.Q1.clear()
        self.Q2.clear()
        self._size = 0


class TestQStack(unittest.TestCase):
    def setUp(self):
        self.empty_stack = Q_stack()
        self.stack = Q_stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        # Now stack should be [3, 2, 1] with 3 at top

    def test_initialization(self):
        stack = Q_stack()
        self.assertEqual(len(stack), 0)
        self.assertTrue(stack.is_empty())

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

        val = self.stack.pop()
        self.assertEqual(val, 2)

        with self.assertRaises(IndexError):
            self.empty_stack.pop()

    def test_peek(self):
        self.assertEqual(self.stack.peek(), 3)
        self.assertEqual(len(self.stack), 3)  # Ensure peek doesn't change size

        with self.assertRaises(IndexError):
            self.empty_stack.peek()

    def test_lifo_behavior(self):
        stack = Q_stack()
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

    def test_clear(self):
        self.stack.clear()
        self.assertEqual(len(self.stack), 0)
        self.assertTrue(self.stack.is_empty())

    def test_size_tracking(self):
        stack = Q_stack()

        # Push elements and verify size
        for i in range(5):
            stack.push(i)
            self.assertEqual(len(stack), i + 1)

        # Pop elements and verify size decreases
        for i in range(5):
            stack.pop()
            self.assertEqual(len(stack), 4 - i)


if __name__ == '__main__':
    unittest.main()
