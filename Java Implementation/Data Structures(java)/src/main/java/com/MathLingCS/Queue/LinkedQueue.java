package com.MathLingCS.Queue;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Set.ArraySet;
import org.jetbrains.annotations.NotNull;

import java.util.Iterator;

public class LinkedQueue<T extends Comparable<T>> implements Queue<T>{

    private final SingleLinkedList<T> list;

    public LinkedQueue(SingleLinkedList<T> list) {
        this.list = list;
    }

    public LinkedQueue() {
        list = new SingleLinkedList<>();
    }

    public LinkedQueue(DynamicArray<T> list) {
        this.list = new SingleLinkedList<>(list);
    }

    public LinkedQueue(LinkedQueue<T> other) {
        list = new SingleLinkedList<>(other.list);
    }


    /**
     * Adds the specified element to the end of the queue.
     *
     * @param t element to be added to the queue
     */
    @Override
    public void enqueue(T t) {
        list.addFirst(t);
    }

    /**
     * Removes and returns the element at the front of the queue.
     *
     * @return the element at the front of the queue
     */
    @Override
    public T dequeue() {
        return list.removeLast();
    }


    /**
     * Returns the element at the front of the queue without removing it.
     *
     * @return the element at the front of the queue
     */
    @Override
    public T peek() {
        return list.get(list.size() - 1);
    }

    /**
     * Returns the number of elements in the queue.
     *
     * @return the number of elements in the queue
     */
    @Override
    public int size() {
        return list.size();
    }

    /**
     * Returns true if the queue contains no elements.
     *
     * @return true if the queue contains no elements
     */
    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    /**
     * Returns true if the queue is full.
     */
    @Override
    public boolean isFull() {
        return false;
    }

    /**
     * Removes all the elements from this queue.
     * The queue will be empty after this call returns.
     */
    @Override
    public void clear() {
        list.clear();
    }


    /**
     * Returns an iterator over elements of type {@code T}.
     *
     * @return an Iterator.
     */
    @NotNull
    @Override
    public Iterator<T> iterator() {
        return list.iterator();
    }
}
