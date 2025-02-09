import java.util.Comparator;

public class BubbleSort<T extends Comparable<T>> implements Sorting<T> {

    /**
     * Sorts the given array in ascending order using bubble sort with a custom comparator.
     * This method iterates over the array multiple times, comparing adjacent elements and swapping them if they are in the wrong order.
     * The process is repeated until the array is sorted.
     * 
     * @param arr The array to be sorted.
     * @param comparator A comparator to determine the order of the elements. It is used to compare two elements to determine their ordering with respect to each other.
     */
    public void sort(T[] arr, Comparator<? super T> comparator) {
        for (int i = 0; i < arr.length - 1; i++) { // Outer loop to control the number of passes
            boolean swapped = false; // Flag to check if any swapping happened in the inner loop
            for (int j = 0; j < arr.length - i - 1; j++) { // Inner loop for comparing adjacent elements
                if (comparator.compare(arr[j], arr[j + 1]) > 0) { // Use comparator to check if elements are in wrong order
                    exch(arr, j, j + 1); // Swap elements if they are in the wrong order
                    swapped = true; // Set flag to true indicating a swap occurred
                }
            }
            if (!swapped && isSorted(arr)) { // If no swaps occurred and array is sorted, exit early
                break;
            }
        }
    }
}

