package com.MathLingCS.Sorting;

@SuppressWarnings("unused")

public class SelectionSort implements Sort {
    /**
     * Sorts an array of elements that extend Comparable.
     *
     * @param array the array to be sorted
     * @return the sorted array
     */
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        for (int i = 0; i < len - 1; i++) {
            // Find the minimum element in the unsorted part of the array
            int minIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (less(array[j], array[minIndex])) {
                    minIndex = j;
                }
            }
            // Swap the found minimum element with the first element
            if (minIndex != i) {
                swap(array, i, minIndex);
            }
        }
        return array;
    }
}
