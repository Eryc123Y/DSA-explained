package com.MathLingCS.Sorting.temp;



public class InsertionSort extends AbstractSort {
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        for (int i = 1; i < len; i++) {
            var key = array[i];
            var j = i - 1;
            while (j >= 0 && less(key, array[j])) {
                array[j + 1] = array[j];
                j--;
            }
            array[j + 1] = key;
        }
        return array;
    }
}
