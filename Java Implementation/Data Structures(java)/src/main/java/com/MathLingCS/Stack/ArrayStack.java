package com.MathLingCS.Stack;

import com.MathLingCS.Array.DynamicArray;

public class ArrayStack<T extends Comparable<T>> implements Stack<T>{
    private final DynamicArray<T> array;
    private int size;

    public ArrayStack() {
        array = new DynamicArray<>();
        size = 0;
    }

    @Override
    public void push(T element) {
        array.add(element);
        size++;
    }

    @Override
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        T top = array.get(size - 1);
        array.remove(size - 1);
        size--;
        return top;
    }

    @Override
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return array.get(size - 1);
    }

    @Override
    public int size() {
        return size;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    @Override
    public void clear() {
        size = 0;
        array.clear();

    }
}
