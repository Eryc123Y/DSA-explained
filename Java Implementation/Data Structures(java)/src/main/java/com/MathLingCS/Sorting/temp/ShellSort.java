package com.MathLingCS.Sorting.temp;

public class ShellSort extends AbstractSort {
    /**
     * @param array the array to be sorted
     * @param <T> the type of elements in the array
     * @return the sorted array
     */
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        int n = array.length;
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                T temp = array[i];
                int j;
                for (j = i; j >= gap && less(temp, array[j - gap]); j -= gap) {
                    array[j] = array[j - gap];
                }
                array[j] = temp;
            }
        }
        return array;
    }
}
