package com.MathLingCS.Set;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Queue.LinearQueue;
import org.jetbrains.annotations.NotNull;

import java.util.Iterator;

@SuppressWarnings({"unused", "unchecked"})
/*
  Implements a generic set data structure using a dynamic array.
 */
public class ArraySet<T extends Comparable<T>> implements Set<T> {

    private final DynamicArray<T> array;

    public ArraySet() {
        array = new DynamicArray<>();
    }

    /**
     * Copy constructor.
     * @param other the set to copy elements from
     */
    public ArraySet(Set<? extends T> other) {
        array = new DynamicArray<>(other.size());
        for (T element : other) {
            add(element);
        }
    }

    public ArraySet(int initialCapacity) {
        array = new DynamicArray<>(initialCapacity);
    }

    public ArraySet(DynamicArray<T> dynamicArray) {
        array = new DynamicArray<>(dynamicArray.size());
        for (T element : dynamicArray) {
            add(element);
        }
    }

    /**
     * Constructor from ArrayQueue.
     */
    public ArraySet(LinearQueue<T> queue) {
        array = new DynamicArray<>(queue.size());
        for (T element : queue) {
            add(element);
        }
    }

    /**
     * Add an element to this set.
     * @param t element to be added to this set
     * @return true if this set did not already contain the specified element
     */
    @Override
    public boolean add(T t) {
        if (!array.contains(t)) {
            array.add(t);
            return true;
        }
        return false;
    }

    /**
     * Removes the specified element from this set if it is present.
     * @param t element to be removed from this set, if present
     * @return true if this set contained the specified element
     */
    @Override
    public boolean remove(T t) {
        if (array.contains(t)) {
            array.removeItem(t);
            return true;
        }
        return false;
    }

    @Override
    public boolean contains(Object t) {
        return array.contains((T) t);
    }

    @Override
    public int size() {
        return array.size();
    }

    @Override
    public boolean isEmpty() {
        return array.isEmpty();
    }

    @Override
    public void clear() {
        array.clear();
    }

    /**
     * A helper method to check if an element is contained in a set.
     * This method is used to handle wildcard capture in generic types.
     *
     * @param set the set to check for the element
     * @param element the element to look for in the set
     * @return true if the set contains the element, false otherwise
     */

    private boolean containsElem(Set<?> set, Object element) {
        return set.contains(element);
    }

    /**
     * Computes the union of this set and the specified set.
     * The resulting set contains all elements that are in either this set or the specified set.
     *
     * @param other the set to compute the union with
     * @return a new set containing the union of this set and the specified set
     */
    @Override
    public Set<T> union(Set<? extends T> other) {
        Set<T> newSet = new ArraySet<>(Integer.max(this.size(), other.size()));
        for (T element : this) {
            newSet.add(element);
        }
        for (T element : other) {
            newSet.add(element);
        }
        return newSet;
    }

    /**
     * Computes the intersection of this set and the specified set.
     * The resulting set contains only the elements that are in both this set and the specified set.
     *
     * @param other the set to compute the intersection with
     * @return a new set containing the intersection of this set and the specified set
     */
    @Override
    public Set<T> intersection(Set<? extends T> other) {
        Set<T> newSet = new ArraySet<>(Integer.min(this.size(), other.size()));
        for (T element : this) {
            if (containsElem(other, element)) {
                newSet.add(element);
            }
        }
        return newSet;
    }

    /**
     * Computes the difference between this set and the specified set.
     * The resulting set contains all elements that are in this set but not in the specified set.
     *
     * @param other the set to compute the difference with
     * @return a new set containing the difference between this set and the specified set
     */
    @Override
    public Set<T> difference(Set<? extends T> other) {
        Set<T> newSet = new ArraySet<>(this.size());
        for (T element : this) {
            if (!containsElem(other, element)) {
                newSet.add(element);
            }
        }
        return newSet;
    }

    /**
     * Determines if this set is a subset of the specified set.
     * A set A is a subset of set B if every element of A is also an element of B.
     *
     * @param other the set to check against
     * @return true if this set is a subset of the specified set, false otherwise
     */
    @Override
    public boolean isSubset(Set<? extends T> other) {
        for (T element : this) {
            if (!containsElem(other, element)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Determines if this set is a superset of the specified set.
     * A set A is a superset of set B if every element of B is also an element of A.
     *
     * @param other the set to check against
     * @return true if this set is a superset of the specified set, false otherwise
     */
    @Override
    public boolean isSuperset(Set<? extends T> other) {
        for (T element : other) {
            if (!this.contains(element)) {
                return false;
            }
        }
        return true;
    }

    /**
     * Returns an array containing all the elements in this set.
     *
     * @return an array containing all the elements in this set
     */
    @Override
    public DynamicArray<T> toDynamicArray() {
        DynamicArray<T> newDynamicArray = new DynamicArray<>(this.size());
        for (T element : this) {
            newDynamicArray.add(element);
        }
        return newDynamicArray;
    }

    /**
     * Returns a single linked list containing all the elements in this set.
     *
     * @return a single linked list containing all the elements in this set
     */
    @Override
    public SingleLinkedList<T> toSingleLinkedList() {
        return this.array.toSingleLinkedList();
    }

    /**
     * Returns true if this set is equal to the specified object.
     *
     * @param o the object to be compared with this set
     * @return true if this set is equal to the specified object
     */
    @Override
    public boolean equals(Set<? extends T> o) {
        if (o == this) {
            return true;
        }
        if (o == null || o.size() != this.size()) {
            return false;
        }
        for (T element : this) {
            if (!containsElem(o, element)) {
                return false;
            }
        }
        return true;
    }

    @Override
    public String toString() {
        return array.toString();
    }

    /**
     * Returns an iterator over the elements in this set.
     * The elements are returned in no particular order.
     *
     * @return an Iterator over the elements in this set
     */
    @Override
    @NotNull
    public Iterator<T> iterator() {
        return array.iterator();
    }

}
