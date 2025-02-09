package com.MathLingCS.LinkedList;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.Array.SortedArray;
import org.jetbrains.annotations.NotNull;

import java.util.Collection;
import java.util.Iterator;
import java.util.NoSuchElementException;

@SuppressWarnings({"unused"})
/*
  Implements a generic single linked list data structure.
  No circle from tail to head.
 */
public class SingleLinkedList<T extends Comparable<T>> extends LinkedList<T> implements Iterable<T> {

    protected class Node {
        T data;
        Node next;

        Node(T data) {
            this.data = data;
            this.next = null;
        }
    }

    protected Node head;
    protected Node tail;
    protected int size;


    /**
     * Constructs an empty linked list.
     */
    public SingleLinkedList() {
        head = null;
        tail = null;
        size = 0;
    }


    /**
     * Copy constructor.
     */
    public SingleLinkedList(SingleLinkedList<T> other) {
        head = null;
        tail = null;
        size = 0;
        for (T element : other) {
            addLast(element);
        }
    }

    /**
     * Construct from an DynamicArray.
     */
    public SingleLinkedList(DynamicArray<T> array) {
        head = null;
        tail = null;
        size = 0;
        for (T element : array) {
            addLast(element);
        }
    }

    public SingleLinkedList(Collection<T> collection){
        head = null;
        tail = null;
        size = 0;
        for (T element : collection) {
            addLast(element);
        }
    }

    public SingleLinkedList(SortedArray<T> array) {
        head = null;
        tail = null;
        size = 0;
        for (T element : array) {
            addLast(element);
        }
    }


    /**
     * Adds an element to the end of the linked list.
     */
    @Override
    public void addLast(T element) {
        size++;
        Node newNode = new Node(element);
        if (head == null) {
            head = newNode;
        } else {
            tail.next = newNode;
        }
        tail = newNode;
    }


    /**
     * Adds an element to the beginning of the linked list.
     */
    public void addFirst(T element) {
        size++;
        // create a new node
        Node newNode = new Node(element);
        // if the linked list is empty, set the head and tail to the new node
        if (head == null) {
            head = newNode;
            tail = newNode;
        } else {
            newNode.next = head;
            head = newNode;
        }
    }



    /**
     * Replaces the element at the specified position in the linked list with the specified element.
     *
     * @param index   the index of the element to be replaced
     * @param element the element to be stored at the specified position
     */
    @Override
    public void set(int index, T element) {
        if (index < 0 || index >= size) {
            throw new IndexOutOfBoundsException();
        }
        Node current = head;
        for (int i = 0; i < index; i++) {
            current = current.next;
        }
        current.data = element;
    }


    /**
     * Get the index of the first occurrence of the specified element in the linked list.
     */
    @Override
    public int indexOf(T element) {
        Node current = head;
        int index = 0;
        while (current != null) {
            if (current.data.equals(element)) {
                return index;
            }
            current = current.next;
            index++;
        }
        return -1;
    }

    /**
     * Removes the first occurrence of the specified element from the linked list, if it is present.
     */
    @Override
    public void remove(T element) {
        // if the linked list is empty, return
        if (head == null) {
            return;
        }
        // if the element to be removed is the head of the linked list
        if (head.data.equals(element)) {
            size--;
            head = head.next;
            // if the linked list is empty after removing the element, set the tail to null
            if (head == null) {
                tail = null;
            }
            return;
        }
        // iterate through the linked list to find the element to be removed
        Node current = head;
        while (current.next != null) {
            if (current.next.data.equals(element)) {
                size--;
                current.next = current.next.next;
                // if the element to be removed is the tail of the linked list, set the tail to the current node
                if (current.next == null) {
                    tail = current;
                }
                return;
            }
            current = current.next;
        }
    }

    /**
     * Removes the element at the specified position in the linked list.
     *
     * @param index the index of the element to be removed
     */
@Override
public T removeAt(int index) {
    if (index < 0 || index >= size) {
        throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + size);
    }

    Node current = head;

    if (index == 0) {
        head = head.next;
        if (head == null) { // if the list is now empty, update the tail
            tail = null;
        }
        size--;
        return current.data;
    }

    for (int i = 0; i < index - 1; i++) {
        current = current.next;
    }

    T result = current.next.data;

    current.next = current.next.next;

    if (index == size - 1) { // If the last element was removed, update the tail
        tail = current;
    }

    size--;
    return result;
}


    /**
     * remove the first element of the linked list.
     * @return the first element of the linked list
     */
    public T removeFirst(){
        return removeAt(0);
    }

    /**
     * remove the last element of the linked list.
     * @return the last element of the linked list
     */
    public T removeLast() {
        return removeAt(size - 1);
    }



    @Override
    public int size() {
        return size;
    }

    /**
     * Retrieves, but does not remove, the given element from the linked list.
     * @return the element at the specified position in the linked list
     * @throws IndexOutOfBoundsException if the index is out of range
     * @param index the index of the element to be retrieved
     */
    @Override
    public T get(int index) {
        if (index >= size || index < 0) {
            throw new IndexOutOfBoundsException();
        }else if (index == 0){
            return head.data;
        }else if (index == size - 1){
            return tail.data;
        }

        Node current = head;

        for (int i = 0; i < index; i++) {
            current = current.next;
        }

        return current.data;
    }

    @Override
    public boolean isEmpty() {
        return size == 0;
    }

    /**
     * Reverse the linked list.
     */
    @Override
    public void reverse() {
        Node prev = null;
        Node current = head;
        Node next = null;
        tail = head; // update tail
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev; // update head
    }


    /**
     * Checks if the linked list contains the specified element.
     * @param element the element to be checked for containment in the linked list
     * @return true if the linked list contains the specified element, false otherwise
     */
    @Override
    public boolean contains(T element) {
        Node current = head;
        while (current != null) {
            if (current.data.equals(element)) {
                return true;
            }
            current = current.next;
        }
        return false;
    }

    /**
     * Removes all elements from the linked list.
     */
    @Override
    public void clear() {
        head = null;
        tail = null;
        size = 0;
    }

    /**
     * Returns an iterator over the elements in the linked list.
     * @return an iterator over the elements in the linked list
     */
    @Override
    public @NotNull Iterator<T> iterator() {
        return new Iterator<>() {
            private Node current = head;

            @Override
            public boolean hasNext() {
                return current != null;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                T data = current.data;
                current = current.next;
                return data;
            }
        };
    }

    @Override
    public String toString() {
        StringBuilder result = new StringBuilder();
        result.append("[");
        Node current = head;
        while (current != null) {
            result.append(current.data);
            if (current.next != null) {
                result.append(" -> ");
            }
            current = current.next;
        }
        result.append("]");
        return result.toString();
    }


    @Override
    public int hashCode() {
        int result = 1;
        Node current = head;
        while (current != null) {
            result = 31 * result + (current.data == null ? 0 : current.data.hashCode());
            current = current.next;
        }
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (!(obj instanceof SingleLinkedList)) return false;
        SingleLinkedList<?> that = (SingleLinkedList<?>) obj;
        if (size != that.size) return false;
        Node currentThis = this.head;
        SingleLinkedList<?>.Node currentThat = that.head;
        while (currentThis != null) {
            if (!currentThis.data.equals(currentThat.data)) {
                return false;
            }
            currentThis = currentThis.next;
            currentThat = currentThat.next;
        }
        return true;
    }
}
