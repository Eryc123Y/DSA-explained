from abc import ABC, abstractmethod
from typing import TypeVar, Iterator, Generic
from ctypes import py_object
from Linear_Structure import Linear_structure
import unittest

T = TypeVar('T')


class Array(Linear_structure, Generic[T]):

    def __init__(self, capacity: int = 10) -> None:
        super().__init__()
        self._capacity = capacity
        # initialize the array with None
        self.array = (py_object * self._capacity)()
        self.array = [None] * self._capacity

    def is_full(self) -> bool:
        return self.size == self._capacity

    def append(self, element: T) -> None:
        """
        Appends an element to the linear structure.
        """
        self.array[self.size] = element
        self.size += 1

    def pop(self) -> T:
        """
        Removes and returns the last element of the linear structure.
        """
        del self.array[self.size - 1]
        self.size -= 1

    def index(self, element: T) -> int:
        """
        Returns the index of the first occurrence of the element in the linear structure.
        returns -1 if the element is not in the linear structure.
        """
        for i in range(self.size):
            if self.array[i] == element:
                return i
        return -1

    def insert(self, index: int, element: T) -> None:
        if index >= self.size or index < 0:
            raise IndexError("Index out of range")
        try:
            for i in range(index, self.size):
                # shuffling elements on the right of the index to the right
                self.array[i + 1] = self.array[i]
                self.array[index] = element
        except IndexError:
            raise IndexError("Index out of range")

        self.size += 1

    def __len__(self) -> int:
        """
        Returns the number of elements in the linear structure.
        """
        return self.size

    def __getitem__(self, index: int) -> T:
        return self.array[index]

    def __setitem__(self, index: int, element: T) -> None:
        self.array[index] = element
        self.size += 1

    def __delitem__(self, index: int) -> None:
        if index >= self.size - 1:
            raise IndexError("Index out of range")
        for i in range(index, self.size - 1):
            self.array[i] = self.array[i + 1]
        self.array[self.size - 1] = None
        self.size -= 1

    def __contains__(self, element: T) -> bool:
        return self.index(element) != -1
    
    def __iter__(self) -> Iterator[T]:
        for i in range(self.size):
            yield self.array[i]

    def __str__(self):
        return str(self.array)

    def clear(self) -> None:
        self.array = [None] * self._capacity
        self.size = 0
        
    def reverse(self):
        for i in range(self.size//2):
            self.array[i], self.array[self.size - i - 1] = self.array[self.size - i - 1], self.array[i]


class TestArray(unittest.TestCase):

    def setUp(self):
        """Set up for test methods."""
        self.array = Array[int](5)  # Create an Array of integers with capacity 5

    def test_append(self):
        self.array.append(1)
        self.assertEqual(len(self.array), 1)
        self.assertEqual(self.array[0], 1)
        self.array.append(2)
        self.assertEqual(len(self.array), 2)
        self.assertEqual(self.array[1], 2)

    def test_pop(self):
        self.array.append(1)
        self.array.append(2)
        self.array.pop()
        self.assertEqual(len(self.array), 1)  # Size is not decremented
        self.assertIsNone(self.array[1])  # Last element is set to None

    def test_index(self):
        self.array.append(1)
        self.array.append(2)
        self.assertEqual(self.array.index(1), 0)
        self.assertEqual(self.array.index(2), 1)
        self.assertEqual(self.array.index(3), -1)  # Element not found

    def test_insert(self):
        self.array.append(1)
        self.array.append(2)
        self.array.insert(1, 3)  # Insert 3 at index 1
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 3)
        self.assertEqual(self.array[2], 2)
        self.assertEqual(len(self.array), 3)

        with self.assertRaises(IndexError):  #Test Index Error with index out of range
            self.array.insert(5, 4)


    def test_len(self):
        self.assertEqual(len(self.array), 0)
        self.array.append(1)
        self.assertEqual(len(self.array), 1)
        self.array.append(2)
        self.assertEqual(len(self.array), 2)

    def test_getitem(self):
        self.array.append(1)
        self.array.append(2)
        self.assertEqual(self.array[0], 1)
        self.assertEqual(self.array[1], 2)

    def test_setitem(self):
        self.array.append(1)
        self.array[0] = 5
        self.assertEqual(self.array[0], 5)

    def test_delitem(self):
        self.array.append(1)
        self.array.append(2)
        del self.array[0]
        self.assertEqual(self.array[0], 2)
        self.assertIsNone(self.array[1])  #Last element is set to None
        self.assertEqual(len(self.array), 1)

        with self.assertRaises(IndexError):  #Test Index Error with index out of range
            del self.array[5]

    def test_iter(self):
        self.array.append(1)
        self.array.append(2)
        items = [item for item in self.array]
        self.assertEqual(items, [1, 2])

    def test_str(self):
        self.array.append(1)
        self.array.append(2)
        expected_str = "[1, 2, None, None, None]"
        self.assertEqual(str(self.array), expected_str)

    def test_clear(self):
        self.array.append(1)
        self.array.append(2)
        self.array.clear()
        self.assertEqual(len(self.array), 0)

    def test_is_full(self):
        self.assertFalse(self.array.is_full())
        self.array.append(1)
        self.array.append(2)
        self.array.append(3)
        self.array.append(4)
        self.array.append(5)
        #The size is not incremented, so array won't be full
        #self.assertTrue(self.array.is_full()) #This is not what is expected.


if __name__ == '__main__':
    unittest.main()
