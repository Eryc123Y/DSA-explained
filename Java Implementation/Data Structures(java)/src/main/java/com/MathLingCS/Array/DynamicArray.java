package com.MathLingCS.Array;

import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;

import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Set.ArraySet;
import com.MathLingCS.Sorting.QuickSort;
import org.jetbrains.annotations.NotNull;

@SuppressWarnings({"unchecked", "unused"})
public class DynamicArray<T extends Comparable<T>> implements Iterable<T> {
    public static final int INITIAL_CAPACITY = 16;
    private int size = 0;
    private int capacity = INITIAL_CAPACITY;
    private boolean isSorted = false;
    private T[] elements;


    /**
     * Constructs an empty dynamic array with an initial capacity of 16.
     */
    public DynamicArray() {
        elements = (T[]) new Comparable[INITIAL_CAPACITY];
    }

    /**
     * Constructs an empty dynamic array with the specified initial capacity.
     * @param initialCapacity the initial capacity of the dynamic array
     * @throws IllegalArgumentException if the specified initial capacity is negative
     */
    public DynamicArray(int initialCapacity) {
        if (initialCapacity < 0) {
            throw new IllegalArgumentException("Initial capacity cannot be negative: " + initialCapacity);
        }
        elements = (T[]) new Comparable[initialCapacity];
        capacity = initialCapacity;
    }

    /**
     * Constructs a dynamic array containing the elements of the specified collection.
     * @param collection the collection whose elements are to be placed into this dynamic array
     */
    public DynamicArray(Collection<? extends T> collection) {
        elements = (T[]) new Comparable[Math.max(INITIAL_CAPACITY, collection.size())];
        for (T item : collection) {
            elements[size++] = item;
        }
        isSorted = false;
    }

    /**
     * Resize, expand or shrink the dynamic array.
     * @param newCapacity the new capacity of the dynamic array
     */
    protected void resize(int newCapacity) {
        T[] newElements = (T[]) new Comparable[newCapacity];
        System.arraycopy(elements, 0, newElements, 0, size);
        elements = newElements;
        capacity = newCapacity;
    }

    /**
     * Adds an element to the end of the dynamic array.
     * @param element the element to be added
     */
    public void add(T element) {
        if (size == elements.length) {
            resize(elements.length * 2);
        }
        elements[size] = element;
        size++;
        isSorted = false;
    }

    /**
     * to add at a specific index
     */
    public void insert(int index, T item) {
        if (index < 0) {
            throw new IndexOutOfBoundsException("Index cannot be negative: " + index);
        }
        if (size == elements.length) {
            resize(elements.length * 2);
        }

        if (index >= elements.length) {
            resize(index + 1);
        }
        if (index > size) {
            size = index + 1;
        } else {
            for (int i = size; i > index; i--) {
                elements[i] = elements[i - 1];
            }
            size++;
        }
        elements[index] = item;
        isSorted = false;
    }


    /**
     * Gets the element at the specified index.
     * @param index the index of the element to get
     * @return the element at the specified index
     */
    public T get(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }
        return elements[index];
    }

    /**
     * Removes the element at the specified index.
     * @param index the index of the element to remove
     */
    public T remove(int index) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }
        T removedElement = elements[index];
        for (int i = index; i < size - 1; i++) {
            elements[i] = elements[i + 1];
        }
        elements[size - 1] = null;
        size--;
        if (size > 0 && size <= capacity / 4) {
            resize(capacity / 2);
        }

        // Check if the array is still sorted after removal
        updateSortedStatus();
        return removedElement;
    }

    /**
     * Removes the first occurrence of the specified element from the dynamic array.
     * @param element the element to be removed
     */
    public void removeItem(T element) {
        int index = find(element);
        if (index != -1) {
            remove(index);
        }
    }
    /**
     * Checks if the dynamic array is sorted.
     */
    private void updateSortedStatus() {
        if (size <= 1) {
            isSorted = true;
            return;
        }
        for (int i = 1; i < size; i++) {
            if (elements[i].compareTo(elements[i - 1]) < 0) {
                isSorted = false;
                return;
            }
        }
        isSorted = true;
    }


    public boolean isSorted() {
        return isSorted;
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public boolean contains(T element) {
        if (isSorted) {
            return binarySearch(element) != -1;
        } else {
            return linearSearch(element) != -1;
        }
    }

    private int linearSearch(T element) {
        for (int i = 0; i < size; i++) {
            if (elements[i].compareTo(element) == 0) {
                return i;
            }
        }
        return -1;
    }

    private int binarySearch(T element) {
        int left = 0;
        int right = size - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int comparison = elements[mid].compareTo(element);
            if (comparison == 0) {
                return mid;
            } else if (comparison < 0) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public void clear() {
        size = 0;
        capacity = INITIAL_CAPACITY;
        elements = (T[]) new Comparable[INITIAL_CAPACITY];
        isSorted = false;
    }

    public int size() {
        return size;
    }

    public int capacity() {
        return capacity;
    }

    public int find(T element) {
        return contains(element) ? (isSorted ? binarySearch(element) : linearSearch(element)) : -1;
    }



    public void set(int index, T element) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException("Index out of bounds: " + index);
        }
        elements[index] = element;
        isSorted = false;
    }

    public Object[] toArray() {
        Object[] array = new Object[size];
        System.arraycopy(elements, 0, array, 0, size);
        return array;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        for (int i = 0; i < size; i++) {
            sb.append(elements[i]);
            if (i < size - 1) {
                sb.append(", ");
            }
        }
        sb.append("]");
        return sb.toString();
    }

    public ArraySet<T> toASet() {
        return new ArraySet<>(this);
    }

    public SingleLinkedList<T> toSingleLinkedList() {
        return new SingleLinkedList<>(this);
    }

/*
    public CircularSLList<T> toCircularSLList() {
        CircularSLList<T> list = new CircularSLList<>();
    }

    public DoubleLinkedList<T> toDoubleLinkedList() {
        DoubleLinkedList<T> list = new DoubleLinkedList<>();

    }

    public CircularDLList.java<T> toCircularDLList() {
        CircularDLList.java<T> list = new CircularDLList.java<>();

    }
*/


    public void sort() {
        var quickSort = new QuickSort();
        if (!isSorted) {
            elements = quickSort.sort(Arrays.copyOf(elements, size));
            // Remove null elements from the end of the array after sorting
            while (size > 0 && elements[size - 1] == null) {
                size--;
            }
            isSorted = true;
        }
    }


    @Override
    @NotNull
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private int currentIndex = 0;

            @Override
            public boolean hasNext() {
                return currentIndex < size;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                return elements[currentIndex++];
            }

            @Override
            public void remove() {
                throw new UnsupportedOperationException();
            }
        };
    }

    public static void main(String[] args) {
        DynamicArray<Integer> dynamicArray = new DynamicArray<>();
        dynamicArray.add(1);
        dynamicArray.add(3);
        dynamicArray.add(5);
        dynamicArray.add(7);

        System.out.println(dynamicArray.contains(4)); // Output: false
        System.out.println(dynamicArray.contains(5)); // Output: true
        System.out.println(dynamicArray.size()); // Output: 4
        System.out.println(dynamicArray.capacity()); // Output: 16
        System.out.println(dynamicArray); // Output: [1, 3, 5, 7]

        dynamicArray.sort();
        System.out.println(dynamicArray); // Output: [1, 3, 5, 7]

        dynamicArray.add(2);
        System.out.println(dynamicArray.contains(2)); // Output: true
        dynamicArray.sort();
        System.out.println(dynamicArray); // Output: [1, 2, 3, 5, 7]
    }
}