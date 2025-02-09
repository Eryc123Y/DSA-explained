package com.MathLingCS.Sorting;

@SuppressWarnings("unused")

public class CocktailSort implements Sort {
    /**
     * Sorts an array of elements that extend Comparable.
     *
     * @param array the array to be sorted
     * @return the sorted array
     */
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        var swapped = true;
        var left = 0;
        var right = len - 1;
        for (int i = 0; i < len / 2; i++) {
            swapped = false;
            for (int j = left; j < right; j++) {
                if (less(array[j + 1], array[j])) {
                    swap(array, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
            swapped = false;
            right--;
            for (int j = right; j > left; j--) {
                if (less(array[j], array[j - 1])) {
                    swap(array, j, j - 1);
                    swapped = true;
                }
            }
            if (!swapped) {
                break;
            }
            left++;
        }
        return array;
    }
}
