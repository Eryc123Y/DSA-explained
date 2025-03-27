import unittest
from Linear_Structures.Linked_list.LoopedSLList import LoopedSLList
from Linear_Structures.Queue.Queue import Queue
from typing import TypeVar, Generic, Optional, Collection, Iterator

T = TypeVar('T')


class CircularQ(Queue[T], Generic[T]):
    """
    A circular queue implementation using a looped singly linked list.
    """

    def __init__(self, elements: Optional[Collection[T]] = None) -> None:
        """Initialize a circular queue, optionally with initial elements."""
        super().__init__()
        # Option 1: Using LoopedSLList
        from Linear_Structures.Linked_list.LoopedSLList import LoopedSLList
        self._items = LoopedSLList(elements or [])
        self._size = len(self._items)

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
        self._items.clear()

    def __iter__(self) -> Iterator[T]:
        # using LHS as the front of the queue
        for item in self._items:
            yield item


class TestCircularQ(unittest.TestCase):
    def setUp(self):
        self.empty_queue = CircularQ()
        self.single_queue = CircularQ([42])
        self.multi_queue = CircularQ([1, 2, 3, 4, 5])

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

    def test_circular_behavior(self):
        # Create a queue with limited size
        queue = CircularQ([1, 2, 3])

        # Dequeue all elements
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)

        # Queue should be empty now
        self.assertTrue(queue.is_empty())

        # Add elements again to verify circular structure works
        queue.enqueue(10)
        queue.enqueue(20)
        queue.enqueue(30)

        # Check elements are added correctly
        self.assertEqual(queue.peek(), 10)
        self.assertEqual(len(queue), 3)

    def test_fifo_behavior(self):
        # Test First-In-First-Out behavior
        queue = CircularQ()
        for i in range(5):
            queue.enqueue(i)

        for i in range(5):
            self.assertEqual(queue.dequeue(), i)


if __name__ == '__main__':
    unittest.main()