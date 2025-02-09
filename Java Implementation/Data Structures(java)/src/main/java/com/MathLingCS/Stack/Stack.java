package com.MathLingCS.Stack;

@SuppressWarnings("unused")

// An abstract stack interface.
public interface Stack<T> {
    /**
     * Adds an element to the top of the stack.
     * @param element the element to be added
     */
    void push(T element);

    /**
     * Removes the element at the top of the stack and returns it.
     * @return the element at the top of the stack
     */
    T pop();

    /**
     * Returns the element at the top of the stack without removing it.
     * @return the element at the top of the stack
     */
    T peek();

    /**
     * Returns the number of elements in the stack.
     * @return the number of elements in the stack
     */
    int size();

    /**
     * Returns whether the stack is empty or not.
     * @return true if the stack is empty, false otherwise
     */
    boolean isEmpty();

    /**
     * Removes all elements from the stack.
     */
    void clear();
    
}
