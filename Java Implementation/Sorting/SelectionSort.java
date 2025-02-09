import java.util.Comparator;

public class SelectionSort<T extends Comparable<T>> implements Sorting<T> {
    /**
     * Sorts the given array in ascending order using selection sort.
     */
    @Override
    public void sort(T[] arr, Comparator<? super T> comparator) {
        // Loop through the array, double pointer approach
        for (int i = 0; i < arr.length - 1; i++) {
            int min = i; // Index of the minimum element
            // Find the index of the minimum element
            for (int j = i + 1; j < arr.length; j++) {
                if (comparator.compare(arr[j], arr[min]) < 0) {
                    min = j;
                }
            }
            // Swap the minimum element with the current element
            exch(arr, i, min);
        }
    }
}


