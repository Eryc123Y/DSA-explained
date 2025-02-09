package com.MathLingCS.LinkedList;

public abstract class LinkedList<T> {

    /**
     * Adds an element to the end of the linked list.
     @param element the element to be added to the linked list
     */
    public abstract void addLast(T element);

    /**
     * Adds an element to the beginning of the linked list.
     @param element the element to be added to the linked list
     */
    public abstract void addFirst(T element);

    /**
     * Return the index of the first occurrence of the specified element in the linked list, or -1 if the linked list does not contain the element.
     * @param element the element to be searched for in the linked list
     */
    public abstract int indexOf(T element);

    /**
     * Replaces the element at the specified position in the linked list with the specified element.
     @param index the index of the element to be replaced
     @param element the element to be stored at the specified position
     */
    public abstract void set(int index, T element);

    /**
     * Removes the first occurrence of the specified element from the linked list, if it is present.
     @param element the element to be removed from the linked list
     */
    public abstract void remove(T element);

    /**
     * Removes the element at the specified position in the linked list.
     * @param index the index of the element to be removed
     */
    public abstract T removeAt(int index);

    public abstract int size();

    /**
     * Retrieves, but does not remove, the given element from the linked list.
     * @return the element at the specified position in the linked list
     */
    public abstract T get(int index);

    /**
     * return whether the linked list is empty or not
     * @return true if the linked list is empty, false otherwise
     */
    public abstract boolean isEmpty();


    /**
     * Reverse the linked list.
     */
    public abstract void reverse();



    /**
     * Checks if the linked list contains the specified element.
     * @param element the element to be checked for containment in the linked list
     * @return true if the linked list contains the specified element, false otherwise
     */
    public abstract boolean contains(T element);


    /**
     * Removes all elements from the linked list.
     */
    public abstract void clear();

    /**
     * Returns an iterator over the elements in the linked list.
     * @return an iterator over the elements in the linked list
     */
    public abstract java.util.Iterator<T> iterator();

    /**
     * Returns a string representation of the linked list.
     * @return a string representation of the linked list
     */
    public abstract String toString();

    /**
     * Returns a hash code value for the linked list.
     * @return a hash code value for the linked list
     */
    public abstract int hashCode();

    /**
     * Compares the specified object with the linked list for equality.
     * @param obj the object to be compared for equality with the linked list
     * @return true if the specified object is equal to the linked list, false otherwise
     */
    public abstract boolean equals(Object obj);
}
