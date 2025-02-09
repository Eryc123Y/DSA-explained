package com.MathLingCS.Array;

@SuppressWarnings("unused")
public class SortedArray<T extends Comparable<T>> extends DynamicArray<T> {

    // Constructors
    public SortedArray() {
        super();
    }

    public SortedArray(int capacity) {
        super(capacity);
    }

    /**
     * Find the index for insertion of an element using binary search.
     */
    private int findIndexToAdd(T item) {
        int low = 0;
        int high = size();
        while (low < high) {
            int mid = low + (high - low) / 2;
            if (item.compareTo(get(mid)) > 0) {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        return low;
    }

    /**
     * Adds the specified element to the array in sorted order.
     * @param item the element to be added
     */
    @Override
    public void add(T item) {
        int index = findIndexToAdd(item);
        super.insert(index, item);
    }

    /**
     * Inserts the specified element at the correct position to maintain sorted order.
     * @param index ignored in this implementation
     * @param item the element to be inserted
     */
    @Override
    public void insert(int index, T item) {
        add(item);  // Ignore the index, insert in sorted order
    }

    /**
     * Unsupported operation in SortedArray.
     * @throws UnsupportedOperationException always
     */
    @Override
    public void set(int index, T element) {
        throw new UnsupportedOperationException("Cannot set element at specific index in a sorted array");
    }

    @Override
    public int find(T item) {
        int low = 0;
        int high = size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            int cmp = item.compareTo(get(mid));
            if (cmp < 0) {
                high = mid - 1;
            } else if (cmp > 0) {
                low = mid + 1;
            } else {
                return mid;
            }
        }
        return -1;
    }

    @Override
    public boolean contains(T item) {
        return find(item) != -1;
    }

    /**
     * Does nothing as the array is always sorted.
     */
    @Override
    public void sort() {
        // Do nothing, the array is always sorted
    }

    // The remove methods from DynamicArray can be used as-is,
    // as they don't disrupt the sorted order
}