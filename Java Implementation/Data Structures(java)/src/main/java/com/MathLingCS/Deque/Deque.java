package com.MathLingCS.Deque;

import com.MathLingCS.Array.DynamicArray;
import java.util.Iterator;

/**
 * A deque interface.
 * @param <T> the type of elements in the deque
 */
public interface Deque<T extends Comparable<T>> {

    /**
     * Add an element to the front of the deque.
     * @param element the element to be added
     */
    void addFirst(T element);

    /**
     * Add an element to the back of the deque.
     * @param element the element to be added
     */
    void addLast(T element);

    /**
     * Return the Dynamic array copy of the deque.
     */
    DynamicArray<T> toDArray();

    /**
     * Return if the deque is empty.
     */
    boolean isEmpty();

    /**
     * Return the size of the deque.
     */
    int size();

    /**
     * Remove the front element of the deque.
     */
    T removeFirst();

    /**
     * Remove the back element of the deque.
     */
    T removeLast();

    /**
     * Get the element by index
     */
    T get(int index);

    /**
     * Whether the deque contains the element.
     * @param element the element to be checked
     * @return true if the element is in the deque, false otherwise
     */
    boolean contains(T element);

    /**
     * Clear the deque.
     */
    void clear();

    /**
     * Return an Iterator for the deque.
     */
    Iterator<T> iterator();
}
