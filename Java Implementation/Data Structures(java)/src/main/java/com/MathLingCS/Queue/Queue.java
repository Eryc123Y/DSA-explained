package com.MathLingCS.Queue;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Set.ArraySet;

/**
 * Interface representing a Queue ADT.
 *
 * @param <T> the type of elements held in this queue
 */
public interface Queue<T extends Comparable<T>> extends Iterable<T> {

    /**
     * Adds the specified element to the end of the queue.
     *
     * @param t element to be added to the queue
     */
    void enqueue(T t);

    /**
     * Removes and returns the element at the front of the queue.
     * @return the element at the front of the queue
     */
    T dequeue();

    /**
     * Returns the element at the front of the queue without removing it.
     *
     * @return the element at the front of the queue
     */
    T peek();

    /**
     * Returns the number of elements in the queue.
     *
     * @return the number of elements in the queue
     */
    int size();

    /**
     * Returns true if the queue contains no elements.
     *
     * @return true if the queue contains no elements
     */
    boolean isEmpty();

    /**
     * Returns true if the queue is full.
     */
    boolean isFull();

    /**
     * Removes all the elements from this queue.
     * The queue will be empty after this call returns.
     */
    void clear();

    /**
     * Returns a string representation of the queue.
     *
     * @return a string representation of the queue
     */
    @Override
    String toString();

}
