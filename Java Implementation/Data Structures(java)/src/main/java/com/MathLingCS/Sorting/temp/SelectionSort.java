package com.MathLingCS.Sorting.temp;


public class SelectionSort extends AbstractSort {
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        for (int i = 0; i < len - 1; i++) {
            int minIndex = i;
            for (int j = i + 1; j < len; j++) {
                if (less(array[j], array[minIndex])) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                swap(array, i, minIndex);
            }
        }
        return array;
    }
}

