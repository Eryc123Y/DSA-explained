package com.MathLingCS.Sorting.temp;

public class HeapSort extends AbstractSort{
    /**
     * Sorts an array of elements that extend Comparable.
     *
     * @param array the array to be sorted
     * @return the sorted array
     */
    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        int n = array.length;
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(array, n, i);
        }
        for (int i = n - 1; i > 0; i--) {
            swap(array, 0, i);
            heapify(array, i, 0);
        }
        return array;
    }

    private <T extends Comparable<T>> void heapify(T[] array, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        if (left < n && less(array[largest], array[left])) {
            largest = left;
        }
        if (right < n && less(array[largest], array[right])) {
            largest = right;
        }
        if (largest != i) {
            swap(array, i, largest);
            heapify(array, n, largest);
        }
    }


}
