import java.util.Comparator;

public interface Sorting<T> {
    /**
     * Sorts the given array in ascending order.
     * @param arr the array to be sorted
     */
    void sort(T[] arr, Comparator<? super T> comparator);
    default void sort(T[] arr) {
        sort(arr, null);
    }

    /**
     * Checks if the given array is sorted in ascending order.
     * @param arr the array to be checked
     * @param comparator key function to compare the elements
     * @return
     */
    default boolean isSorted(T[] arr, Comparator<? super T> comparator) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (comparator.compare(arr[i], arr[i + 1]) > 0) {
                return false;
            }
        }
        return true;
    }

    /**
     * Overloaded method when no key function is provided.
     * @param arr the array to be checked
     * @return
     */
    default boolean isSorted(T[] arr) {
        return isSorted(arr, null);
    }

    default void exch(T[] arr, int i, int j) {
        if (i < 0 || j < 0 || i >= arr.length || j >= arr.length) {
            throw new IndexOutOfBoundsException("Invalid index");
        }
        T temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * Compares two elements using the provided key function.
     * @param a the first element
     * @param b the second element
     * @param comparator key function to compare the elements
     * @return
     */
    default boolean less(T a, T b, Comparator<? super T> comparator) {
        return comparator.compare(a, b) < 0;
    }

    /**
     * Overloaded method when no key function is provided.
     * @param a the first element
     * @param b the second element
     * @return
     */
    default boolean less(T a, T b) {
        return less(a, b, null);
    }

    /**
     * Prints the elements of the array.
     * @param arr the array to be printed
     */
    default void show(T[] arr) {
        StringBuilder sb = new StringBuilder();
        for (T element : arr) {
            sb.append(element).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}