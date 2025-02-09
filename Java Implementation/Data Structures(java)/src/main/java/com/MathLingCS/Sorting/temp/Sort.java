package com.MathLingCS.Sorting.temp;


public interface Sort {
    /**
     * Sorts an array of elements that extend Comparable.
     * @param array the array to be sorted
     * @param <T> the type of elements in the array
     * @return the sorted array
     */
    <T extends Comparable<T>> T[] sort(T[] array);
}

