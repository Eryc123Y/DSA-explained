package com.MathLingCS.Queue;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Set.ArraySet;
import org.jetbrains.annotations.NotNull;

import java.util.Iterator;

@SuppressWarnings({"unused","unchecked"})
public class CircularQueue<T extends Comparable<T>> implements Queue<T> {

    private DynamicArray<T> array;
    private int front, rear, size;

    public CircularQueue() {
        this(10); // Default initial capacity
    }

    public CircularQueue(int initialCapacity) {
        if (initialCapacity <= 0) {
            throw new IllegalArgumentException("Initial capacity must be greater than zero.");
        }
        array = new DynamicArray<>(initialCapacity);
        front = 0;
        rear = 0;
        size = 0;
    }

    public CircularQueue(CircularQueue<? extends T> other) {
        array = new DynamicArray<>(other.size());
        for (T element : other) {
            enqueue(element);
        }
        this.front = other.front;
        this.rear = other.rear;
        this.size = other.size;
    }

    @Override
    public void enqueue(T t) {
        if (isFull()) {
            throw new IllegalStateException("Queue is full: cannot enqueue.");
        }
        array.insert(this.rear, t);
        this.rear = (this.rear + 1) % array.capacity();
        this.size += 1;
    }

    @Override
    public T dequeue() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty: cannot dequeue.");
        }
        T element = array.get(this.front);
        this.front = (this.front + 1) % array.capacity();
        this.size -= 1;
        return element;
    }

    @Override
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Queue is empty: cannot peek.");
        }
        return array.get(this.front);
    }

    @Override
    public int size() {
        return this.size;
    }

    @Override
    public boolean isEmpty() {
        return this.size == 0;
    }

    @Override
    public boolean isFull() {
        return this.size == array.capacity();
    }

    @Override
    public void clear() {
        array.clear();
        this.front = 0;
        this.rear = 0;
        this.size = 0;
    }


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

    @NotNull
    @Override
    public Iterator<T> iterator() {
        return new Iterator<T>() {
            private int currentIndex = front;
            private int elementsProcessed = 0;

            @Override
            public boolean hasNext() {
                return elementsProcessed < size;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new IllegalStateException("No more elements to iterate over.");
                }
                T element = array.get(currentIndex);
                currentIndex = (currentIndex + 1) % array.capacity();
                elementsProcessed++;
                return element;
            }
        };
    }

    private void resize(int newCapacity) {
        DynamicArray<T> newArray = new DynamicArray<>(newCapacity);
        for (int i = 0; i < size; i++) {
            newArray.insert(i, array.get((front + i) % array.capacity()));
        }
        array = newArray;
        front = 0;
        rear = size;
    }
}