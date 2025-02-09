import java.util.Comparator;

public class CocktailSort<T extends Comparable<T>> implements Sorting<T> {
    /**
     * Sorts the given array in ascending order using cocktail shaker sort with a custom comparator.
     * Cocktail shaker sort is a variation of bubble sort that sorts in both directions on each pass through the list.
     * This method first iterates through the array from the beginning to the end, like bubble sort,
     * comparing each pair of adjacent items and swapping them if they are in the wrong order.
     * After reaching the end of the array, the algorithm then iterates in reverse order, from the end to the beginning,
     * performing the same swapping process. This bidirectional process is repeated until no more swaps are needed,
     * indicating that the array is sorted.
     *
     * @param arr The array to be sorted.
     * @param comparator A comparator to determine the order of the elements. It is used to compare two elements to determine their ordering with respect to each other.
     */
    public void sort(T[] arr, Comparator<? super T> comparator) {
        boolean swapped = true; // Flag to keep track of whether any swaps have occurred in the current pass
        int start = 0; // Starting index for the forward pass
        int end = arr.length - 1; // Ending index for the backward pass

        while (swapped) { // Continue looping until no swaps occur in a complete pass
            swapped = false; // Reset swap flag for the forward pass
            for (int i = start; i < end; i++) { // Forward pass through the array
                if (comparator.compare(arr[i], arr[i + 1]) > 0) { // Compare adjacent elements
                    exch(arr, i, i + 1); // Swap if elements are in the wrong order
                    swapped = true; // Mark that a swap has occurred
                }
            }
            if (!swapped) { // If no swaps occurred in the forward pass, the array is sorted
                break;
            }
            swapped = false; // Reset swap flag for the backward pass
            end--; // Decrement end index since the last element is now in its correct position
            for (int i = end; i > start; i--) { // Backward pass through the array
                if (comparator.compare(arr[i - 1], arr[i]) > 0) { // Compare adjacent elements
                    exch(arr, i, i - 1); // Swap if elements are in the wrong order
                    swapped = true; // Mark that a swap has occurred
                }
            }
            start++; // Increment start index since the first element is now in its correct position
        }
    }
}