from typing import TypeVar, Generic, List
from abc import ABC, abstractmethod

T = TypeVar('T')


def insertion_sort(a: List[T]) -> List[T]:
    """
    Implement insertion sort algorithm.
    """
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


class Sort(ABC, Generic[T]):
    @staticmethod
    def exchange(a: List[T], i: int, j: int):
        """
        Swap elements at indices i and j in list a.
        """
        a[i], a[j] = a[j], a[i]

    @staticmethod
    def is_sorted(a: List[T]) -> bool:
        """
        Check if the list a is sorted.
        """
        for i in range(1, len(a)):
            if a[i] < a[i - 1]:
                return False
        return True

    def bubble_sort(self, a: List[T]) -> List[T]:
        """
        Implement bubble sort algorithm.
        """
        n = len(a)
        for i in range(n):
            for j in range(n - i - 1):
                if a[j] > a[j + 1]:
                    self.exchange(a, j, j + 1)
        return a

    def merge_sort(self, a: List[T]) -> List[T]:
        """
        Implement merge sort algorithm.
        """

        def merge(first: List[T], last: List[T]) -> List[T]:
            result = []
            i = j = 0
            while i < len(first) and j < len(last):
                if first[i] < last[j]:
                    result.append(first[i])
                    i += 1
                else:
                    result.append(last[j])
                    j += 1
            result.extend(first[i:])
            result.extend(last[j:])
            return result

        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = self.merge_sort(a[:mid])
        right = self.merge_sort(a[mid:])
        return merge(left, right)

    def selection_sort(self, a: List[T]) -> List[T]:
        """
        Implement selection sort algorithm.
        """
        for i in range(len(a)):
            min_index = i
            for j in range(i + 1, len(a)):
                if a[j] < a[min_index]:
                    min_index = j
            if min_index != i:
                self.exchange(a, i, min_index)
        return a


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    sorter = Sort()

    sorted_data = sorter.merge_sort(data.copy())
    print(f"Merge Sorted: {sorted_data}")

    sorted_data = insertion_sort(data.copy())
    print(f"Insertion Sorted: {sorted_data}")

    sorted_data = sorter.selection_sort(data.copy())
    print(f"Selection Sorted: {sorted_data}")