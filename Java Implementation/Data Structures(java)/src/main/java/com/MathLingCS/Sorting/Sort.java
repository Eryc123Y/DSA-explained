package com.MathLingCS.Sorting;

public interface Sort {
    /**
     * Sorts an array of elements that extend Comparable.
     * @param array the array to be sorted
     * @param <T> the type of elements in the array
     * @return the sorted array
     */
    <T extends Comparable<T>> T[] sort(T[] array);

    /**
     * Swaps two elements in an array.
     * @param array the array containing the elements
     * @param i the index of the first element
     * @param j the index of the second element
     * @param <T> the type of elements in the array
     */
    default <T> void swap(T[] array, int i, int j) {
        T temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    /**
     * Prints the elements of an array.
     * @param array the array to be printed
     * @param <T> the type of elements in the array
     */
    default <T> void printArray(T[] array) {
        System.out.print("[");
        for (T element : array) {
            System.out.print(element + " ");
        }
        System.out.println("]");
    }

    /**
     * Check if the array is sorted.
     */
    default <T extends Comparable<T>> boolean isSorted(T[] array) {
        for (int i = 0; i < array.length - 1; i++) {
            if (array[i].compareTo(array[i + 1]) > 0) {
                return false;
            }
        }
        return true;
    }

    /**
     * Check if a is less than b.
     * @param a the first element
     * @param b the second element
     * @return true if a is less than b, false otherwise
     * @param <T> the type of elements to be compared
     */
    default  <T extends Comparable<T>> boolean less(T a, T b) {
        return a.compareTo(b) < 0;
    }
}