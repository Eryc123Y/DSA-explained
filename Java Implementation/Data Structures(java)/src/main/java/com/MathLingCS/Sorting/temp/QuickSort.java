package com.MathLingCS.Sorting.temp;

public class QuickSort extends AbstractSort {
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        quickSort(array, 0, array.length - 1);
        return array;
    }

    private <T extends Comparable<T>> void quickSort(T[] array, int low, int high) {
        if (low < high) {
            int pi = partition(array, low, high);
            quickSort(array, low, pi - 1);
            quickSort(array, pi + 1, high);
        }
    }

    private <T extends Comparable<T>> int partition(T[] array, int low, int high) {
        T pivot = array[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (less(array[j], pivot)) {
                i++;
                swap(array, i, j);
            }
        }
        swap(array, i + 1, high);
        return i + 1;
    }
}
