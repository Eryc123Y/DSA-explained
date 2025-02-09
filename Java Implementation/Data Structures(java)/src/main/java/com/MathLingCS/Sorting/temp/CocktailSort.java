package com.MathLingCS.Sorting.temp;



public class CocktailSort extends AbstractSort {
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        var len = array.length;
        var swapped = true;
        var left = 0;
        var right = len - 1;
        while (swapped) {
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
            left++;
        }
        return array;
    }
}
