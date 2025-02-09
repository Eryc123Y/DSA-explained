import java.util.Comparator;

public class InsertionSort<T extends Comparable<T>> implements Sorting<T> {
    /**
     * Sorts the given array in ascending order using insertion sort.
     */
    public void sort(T[] arr, Comparator<? super T> comparator) {
        // Loop through the array, double pointer approach
        for (int i = 1; i < arr.length; i++) {
            // Move the element to the left until it is in the correct position
            for (int j = i; j > 0 && less(arr[j], arr[j - 1], comparator); j--) {
                exch(arr, j, j - 1);
            }
        }
    }
}
