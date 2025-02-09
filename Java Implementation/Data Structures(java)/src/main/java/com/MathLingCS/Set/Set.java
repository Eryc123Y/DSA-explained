package com.MathLingCS.Set;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;

@SuppressWarnings({"unused"})
/**
 * A collection that contains no duplicate elements.
 *
 * @param <T> the type of elements maintained by this set
 */
public interface Set<T extends Comparable<T>> extends Iterable<T> {

    /**
     * Adds the specified element to this set if it is not already present.
     *
     * @param t element to be added to this set
     * @return true if this set did not already contain the specified element
     */
    boolean add(T t);

    /**
     * Removes the specified element from this set if it is present.
     *
     * @param t element to be removed from this set, if present
     * @return true if this set contained the specified element
     */
    boolean remove(T t);

    /**
     * Returns true if this set contains the specified element.
     *
     * @param t element whose presence in this set is to be tested
     * @return true if this set contains the specified element
     */
    boolean contains(Object t);

    /**
     * Returns the number of elements in this set.
     *
     * @return the number of elements in this set
     */
    int size();

    /**
     * Returns true if this set contains no elements.
     *
     * @return true if this set contains no elements
     */
    boolean isEmpty();

    /**
     * Removes all of the elements from this set.
     * The set will be empty after this call returns.
     */
    void clear();

    /**
     * Returns a set containing all of the elements in this set and the specified set.
     *
     * @param other the set to be combined with this set
     * @return the union of this set and the specified set
     */
    Set<T> union(Set<? extends T> other);

    /**
     * Returns a set containing only the elements that are present in both this set and the specified set.
     *
     * @param other the set to be intersected with this set
     * @return the intersection of this set and the specified set
     */
    Set<T> intersection(Set<? extends T> other);

    /**
     * Returns a set containing the elements that are in this set but not in the specified set.
     *
     * @param other the set to be subtracted from this set
     * @return the difference of this set and the specified set
     */
    Set<T> difference(Set<? extends T> other);

    /**
     * Returns a set containing the elements that are in either this set or the specified set but not in both.
     *
     * @param other the set to be combined with this set
     * @return the symmetric difference of this set and the specified set
     */
    default Set<T> symmetricDifference(Set<? extends T> other) {
        return union(other).difference(intersection(other));
    }

    /**
     * Returns true if this set is a subset of the specified set.
     *
     * @param other the set to be compared with this set
     * @return true if this set is a subset of the specified set
     */
    boolean isSubset(Set<? extends T> other);

    /**
     * Returns true if this set is a superset of the specified set.
     *
     * @param other the set to be compared with this set
     * @return true if this set is a superset of the specified set
     */
    boolean isSuperset(Set<? extends T> other);

    /**
     * Returns a string representation of this set.
     * @return a string representation of this set
     */
    String toString();

    /**
     * Returns an array containing all the elements in this set.
     * @return an array containing all the elements in this set
     */
    DynamicArray<T> toDynamicArray();

    /**
     * Returns a single linked list containing all the elements in this set.
     * @return a single linked list containing all the elements in this set
     */
    SingleLinkedList<T> toSingleLinkedList();

    /**
     * Returns true if this set is equal to the specified object.
     * @param o the object to be compared with this set
     * @return true if this set is equal to the specified object
     */
    boolean equals(Set<? extends T> o);
}
