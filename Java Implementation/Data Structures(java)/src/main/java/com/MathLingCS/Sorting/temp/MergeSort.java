package com.MathLingCS.Sorting.temp;

@SuppressWarnings("unchecked")

public class MergeSort extends AbstractSort{

    @Override
    public <T extends Comparable<T>> T[] sort(T[] array) {
        mergeSort(array, 0, array.length - 1);
        return array;
    }

    private <T extends Comparable<T>> void mergeSort(T[] array, int low, int high) {
        if (low < high) {
            int mid = (low + high) / 2;
            mergeSort(array, low, mid);
            mergeSort(array, mid + 1, high);
            merge(array, low, mid, high);
        }
    }

    private <T extends Comparable<T>> void merge(T[] array, int low, int mid, int high) {
        int n1 = mid - low + 1;
        int n2 = high - mid;
        T[] left = (T[]) new Comparable[n1];
        T[] right = (T[]) new Comparable[n2];
        System.arraycopy(array, low, left, 0, n1);
        for (int i = 0; i < n2; i++) {
            right[i] = array[mid + 1 + i];
        }
        int i = 0, j = 0, k = low;
        while (i < n1 && j < n2) {
            if (less(left[i], right[j])) {
                array[k] = left[i];
                i++;
            } else {
                array[k] = right[j];
                j++;
            }
            k++;
        }
        while (i < n1) {
            array[k] = left[i];
            i++;
            k++;
        }
        while (j < n2) {
            array[k] = right[j];
            j++;
            k++;
        }
    }
}
