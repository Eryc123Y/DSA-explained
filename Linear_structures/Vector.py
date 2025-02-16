from typing import TypeVar, Optional, Iterable, Generic
from Array import Array
import unittest

T = TypeVar('T')

class Vector(Array, Generic[T]):
    """
    Vector class for dynamic arrays.
    """
    
    def __init__(self, elements: Optional[Iterable[T]] = None):
        """
        Initialize a Vector with a list of elements.
        
        Parameters:
            elements (Optional[list[T]]): A list of initial elements to populate the vector.
        """
        super().__init__(elements = elements)
        
    def _expand(self) -> None:
        """
        Expands the capacity of the vector, when it is full.
        """
        new_capacity = self._capacity * 2
        # Pass only the valid elements instead of self.array directly.
        new_elements = self.array[:self.size] # exclude None values
        self.array = Array(new_capacity, elements=new_elements)
        self._capacity = new_capacity

    def _shrink(self) -> None:
        """
        Shrinks the capacity of the vector, when it is less than half full.
        """
        new_capacity = self._capacity // 2
        new_elements = self.array[:self.size] # exclude None values
        self.array = Array(new_capacity, elements=new_elements)
        self._capacity = new_capacity
        
    def append(self, element: T) -> None:
        """
        Appends an element to the vector.
        """
        if self.is_full():
            self._expand()
        super().append(element)
        
    def pop(self) -> T:
        """
        Removes and returns the last element of the vector.
        """
        if self.size <= self._capacity // 4:
            self._shrink()
        return super().pop()
    
    def insert(self, index: int, element: T) -> None:
        """
        Inserts an element at the given index.
        """
        if self.is_full():
            self._expand()
        super().insert(index, element)
        
    def __str__(self) -> str:
        """
        Returns a string representation of the vector.
        """
        return str([self.array[i] for i in range(self.size) if self.array[i] is not None])
    
        


class TestVector(unittest.TestCase):

    def setUp(self) -> None:
        # Instead of using the default (empty) constructor—which would yield a capacity of 0—
        # we initialize with some elements so that capacity is nonzero.
        # In your design, when elements are passed, capacity is set to len(elements).
        self.vector = Vector(elements=[1, 2, 3])

    def test_append(self):
        # Append an element and check that the element is added and size increases
        old_capacity = self.vector._capacity
        self.vector.append(4)
        self.assertEqual(self.vector.size, 4)
        self.assertEqual(self.vector[3], 4)
        # If the vector was full before appending, _expand() should have been called
        if old_capacity == 3:
            self.assertGreater(self.vector._capacity, 3, 
                               "Expected capacity expansion when appending to a full vector.")

    def test_pop(self):
        # Test that pop returns the last element and decrements size.
        last_elem = self.vector.pop()
        self.assertEqual(last_elem, 3)
        self.assertEqual(self.vector.size, 2)
        # Optionally, if vector down-sizing (_shrink) is triggered, capacity will decrease.
        # You could force that scenario by appending many elements and then popping many.

    def test_insert(self):
        # Insert a new element in the middle and verify that new element exists at that index.
        self.vector.insert(1, 99)
        self.assertEqual(self.vector[1], 99)
        self.assertEqual(self.vector.size, 4)

    def test_str(self):
        # Test string representation
        self.assertEqual(str(self.vector), "[1, 2, 3]")

    def test_expand_shrink(self):
        # Start with a vector with several elements to have a non-trivial initial capacity.
        vect = Vector(elements=[10, 20, 30, 40])
        original_capacity = vect._capacity
        # Append enough elements to trigger expansion.
        for i in range(50, 70):
            vect.append(i)
        self.assertGreater(vect._capacity, original_capacity,
                           "Expected capacity to expand after appending numerous elements.")

        # Now, pop elements to potentially trigger shrinking.
        # (Depending on your threshold, this loop should eventually reduce capacity.)
        while vect.size > 1:
            vect.pop()
        # Check that capacity was reduced. (This isn't a precise check,
        # but assumes that for a very reduced vector, capacity has shrunk.)
        self.assertLess(vect._capacity, original_capacity * 2,
                        "Expected capacity to shrink after many pops.")

if __name__ == '__main__':
    unittest.main()
    