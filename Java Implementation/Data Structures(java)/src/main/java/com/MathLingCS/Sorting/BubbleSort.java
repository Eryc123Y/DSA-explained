
package com.MathLingCS.Sorting;

@SuppressWarnings("unused")

public class BubbleSort implements Sort {

    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        boolean swapped;
        for (var i = 0; i < len - 1; i++) {
            swapped = false;
            for (var j = 0; j < len - i - 1; j++) {
                if (less(array[j + 1], array[j])) {
                    swap(array, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                break; // No elements were swapped, array is sorted
            }
        }
        return array;
    }
}