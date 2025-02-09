package com.MathLingCS.Stack;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;

/**
 * A stack implementation using a singly linked list.
 * @param <T>
 */
public class SLListStack<T extends Comparable<T>> implements Stack<T> {
    private final SingleLinkedList<T> list;

    /**
     * Constructs an empty stack.
     */
    public SLListStack() {
        list = new SingleLinkedList<>();
    }

    /**
     * Copy constructor.
     */
    public SLListStack(SLListStack<T> other) {
        list = new SingleLinkedList<>(other.list);
    }

    /**
     * Construct from a SingleLinkedList.
     */
    public SLListStack(SingleLinkedList<T> list) {
        this.list = new SingleLinkedList<>(list);
    }

    /**
     * Construct from a DynamicArray.
     */
    public SLListStack(DynamicArray<T> list) {
        this.list = new SingleLinkedList<>(list);
    }

    /**
     * Adds an element to the top of the stack (which corresponds to the end of the linked list).
     *
     * @param element the element to be added
     */
    @Override
    public void push(T element) {
        list.addLast(element);  // Add to the tail (top of stack)
    }

    /**
     * Removes the element at the top of the stack (which is at the front of the linked list) and returns it.
     *
     * @return the element at the top of the stack
     */
    @Override
    public T pop() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return list.removeLast();
    }

    /**
     * Returns the element at the top of the stack without removing it.
     *
     * @return the element at the top of the stack
     */
    @Override
    public T peek() {
        if (isEmpty()) {
            throw new IllegalStateException("Stack is empty");
        }
        return list.get(list.size()-1);  // Access the element at the end (top of stack) without removing it
    }

    /**
     * Returns the number of elements in the stack.
     *
     * @return the number of elements in the stack
     */
    @Override
    public int size() {
        return list.size();
    }

    /**
     * Returns whether the stack is empty or not.
     *
     * @return true if the stack is empty, false otherwise
     */
    @Override
    public boolean isEmpty() {
        return list.isEmpty();
    }

    /**
     * Removes all elements from the stack.
     */
    @Override
    public void clear() {
        list.clear();
    }
}
