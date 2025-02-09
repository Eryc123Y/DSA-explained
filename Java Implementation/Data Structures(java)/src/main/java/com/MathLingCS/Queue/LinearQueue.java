package com.MathLingCS.Queue;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Set.ArraySet;
import org.jetbrains.annotations.NotNull;

import java.util.Iterator;


@SuppressWarnings("unused")

/*
  Implements a generic queue data structure using an dynamic array.
 */
public class LinearQueue<T extends Comparable<T>> implements Queue<T>{

    private final DynamicArray<T> array ;
    int front, rear, size;



    public LinearQueue() {
        array = new DynamicArray<>();
        front = 0;
        rear = 0;
        size = 0;
    }

    public LinearQueue(int initialCapacity) {
        array = new DynamicArray<>(initialCapacity);
        front = 0;
        rear = 0;
        size = 0;
    }

    // Copy constructor
    @SuppressWarnings("unchecked")
    public LinearQueue(LinearQueue<? extends T> other) {
        array = new DynamicArray<>(other.size());
        for (T element : other) {
            enqueue(element);
        }
        this.front = other.front;
        this.rear = other.rear;
        this.size = other.size;
    }



    /**
     * Adds the specified element to the end of the queue.
     *
     * @param t element to be added to the queue
     */
    @Override
    public void enqueue(T t) {
        array.insert(this.rear, t);
        this.rear += 1;
        this.size += 1;
    }

    /**
     * Removes and returns the element at the front of the queue.
     *
     * @return the element at the front of the queue
     */
    @Override
    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty: cannot dequeue.");
        }
        T element = array.get(this.front);
        this.front += 1;
        this.size -= 1;
        return element;
    }

    /**
     * Returns the element at the front of the queue without removing it.
     *
     * @return the element at the front of the queue
     */
    @Override
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty: cannot peek.");
        }
        return array.get(this.front);
    }

    /**
     * Returns the number of elements in the queue.
     *
     * @return the number of elements in the queue
     */
    @Override
    public int size() {
        return this.size;
    }

    /**
     * Returns true if the queue contains no elements.
     *
     * @return true if the queue contains no elements
     */
    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }

    /**
     * Returns true if the queue is full.
     */
    @Override
    public boolean isFull() {
        return this.size == array.capacity();
    }


    /**
     * Removes all the elements from this queue.
     * The queue will be empty after this call returns.
     */
    @Override
    public void clear() {
        array.clear();
        this.front = 0;
        this.rear = 0;
        this.size = 0;
    }


    /**
     * Returns a string representation of the queue.
     *
     * @return a string representation of the queue
     */
    @Override
    public String toString() {
        var sb = new StringBuilder();
        sb.append("[");
        for (T element : this) {
            sb.append(element);
            sb.append(",");
        }
        if (sb.length() > 1) {
            sb.deleteCharAt(sb.length() - 1);
        }
        sb.append("]");

        return sb.toString();
    }



    /**
     * Returns an iterator over elements of type {@code T}.
     *
     * @return an Iterator.
     */
    @NotNull
    @Override
    public Iterator<T> iterator() {
        return array.iterator();
    }
}
