import unittest
from typing import TypeVar, Generic, Iterator, Optional, Collection

from Linear_Structures.Vector import Vector
from Linear_Structures.Queue.Queue import Queue

T = TypeVar('T')


class SimpleQ(Queue[T], Generic[T]):
    """
    Simple queue implementation using a list.
    """

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """Initialize a simple queue, optionally with initial elements."""
        super().__init__()
        # Create Vector directly - it now has a default capacity
        self._items = Vector(elements)

        # Update size based on elements
        if elements:
            self._size = len(elements)

    def enqueue(self, item: T) -> None:
        # using RHS as the end of the queue, LHS as the front
        self._size += 1
        self._items.append(item)

    def dequeue(self) -> T:
        # using LHS as the front of the queue
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        self._size -= 1
        item = self._items[0]
        del self._items[0]
        return item

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def clear(self) -> None:
        self._size = 0
        self._items.clear()  # Remove the return statement

    def __iter__(self) -> Iterator[T]:
        # using LHS as the front of the queue
        for item in self._items:
            yield item


class TestSimpleQ(unittest.TestCase):

    def setUp(self):
        self.empty_queue = SimpleQ()
        self.single_queue = SimpleQ([42])
        self.multi_queue = SimpleQ([1, 2, 3, 4, 5])

    def test_initialization(self):
        self.assertEqual(len(self.empty_queue), 0)
        self.assertEqual(len(self.single_queue), 1)
        self.assertEqual(len(self.multi_queue), 5)

    def test_enqueue(self):
        # Test enqueue to empty queue
        self.empty_queue.enqueue(10)
        self.assertEqual(len(self.empty_queue), 1)
        self.assertEqual(self.empty_queue.peek(), 10)

        # Test enqueue to non-empty queue
        self.single_queue.enqueue(99)
        self.assertEqual(len(self.single_queue), 2)
        items = list(self.single_queue)
        self.assertEqual(items, [42, 99])

    def test_dequeue(self):
        # Test dequeue from single item queue
        item = self.single_queue.dequeue()
        self.assertEqual(item, 42)
        self.assertTrue(self.single_queue.is_empty())

        # Test multiple dequeues
        items = []
        for _ in range(3):
            items.append(self.multi_queue.dequeue())
        self.assertEqual(items, [1, 2, 3])
        self.assertEqual(len(self.multi_queue), 2)

        # Test dequeue from empty queue
        with self.assertRaises(IndexError):
            self.empty_queue.dequeue()

    def test_peek(self):
        self.assertEqual(self.single_queue.peek(), 42)
        self.assertEqual(self.multi_queue.peek(), 1)

        # Peek shouldn't change queue
        self.assertEqual(len(self.single_queue), 1)

        # Peek on empty queue
        with self.assertRaises(IndexError):
            self.empty_queue.peek()

    def test_clear(self):
        self.multi_queue.clear()
        self.assertTrue(self.multi_queue.is_empty())
        self.assertEqual(len(self.multi_queue), 0)

    def test_iteration(self):
        items = list(self.multi_queue)
        self.assertEqual(items, [1, 2, 3, 4, 5])

        # Iteration shouldn't alter queue
        self.assertEqual(len(self.multi_queue), 5)

    def test_is_empty(self):
        self.assertTrue(self.empty_queue.is_empty())
        self.assertFalse(self.single_queue.is_empty())

        self.single_queue.dequeue()
        self.assertTrue(self.single_queue.is_empty())

    def test_size_and_len(self):
        self.assertEqual(self.empty_queue.size(), 0)
        self.assertEqual(self.multi_queue.size(), 5)

        # Verify size() matches __len__()
        self.assertEqual(self.multi_queue.size(), len(self.multi_queue))

    def test_str(self):
        self.assertEqual(str(self.empty_queue), "[]")
        self.assertEqual(str(self.single_queue), "[42]")
        self.assertEqual(str(self.multi_queue), "[1, 2, 3, 4, 5]")

    def test_fifo_behavior(self):
        # Test First-In-First-Out behavior
        queue = SimpleQ()
        for i in range(5):
            queue.enqueue(i)

        for i in range(5):
            self.assertEqual(queue.dequeue(), i)


if __name__ == '__main__':
    unittest.main()
