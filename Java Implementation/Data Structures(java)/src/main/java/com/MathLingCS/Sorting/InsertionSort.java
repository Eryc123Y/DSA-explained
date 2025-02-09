package com.MathLingCS.Sorting;

@SuppressWarnings("unused")

public class InsertionSort implements Sort {
    /**
     * Sorts an array of elements that extend Comparable.
     *
     * @param array the array to be sorted
     * @return the sorted array
     */
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        for (int i = 1; i < len; i++) {
            var key = array[i];
            var j = i - 1;
            while (j >= 0 && array[j].compareTo(key) > 0) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
        return array;
    }
}
