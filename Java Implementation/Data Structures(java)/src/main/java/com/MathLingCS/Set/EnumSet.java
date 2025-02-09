package com.MathLingCS.Set;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import org.jetbrains.annotations.NotNull;

import java.util.Iterator;
import java.util.NoSuchElementException;

@SuppressWarnings({"unused"})
public class EnumSet<E extends Enum<E> & Comparable<E>> implements Set<E> {

    private final Class<E> elementType;
    private long elements;

    public EnumSet(Class<E> elementType) {
        this.elementType = elementType;
        this.elements = 0;
    }

    private int ordinal(E e) {
        return e.ordinal();
    }

    @Override
    public boolean add(E e) {
        int ordinal = ordinal(e);
        if ((elements & (1L << ordinal)) != 0) {
            return false;
        }
        elements |= (1L << ordinal);
        return true;
    }

    @Override
    public boolean remove(E e) {
        int ordinal = ordinal(e);
        if ((elements & (1L << ordinal)) == 0) {
            return false;
        }
        elements &= ~(1L << ordinal);
        return true;
    }

    @SuppressWarnings("unchecked")
    @Override
    public boolean contains(Object e) {
        int ordinal = ordinal((E) e);
        return (elements & (1L << ordinal)) != 0;
    }

    @Override
    public int size() {
        return Long.bitCount(elements);
    }

    @Override
    public boolean isEmpty() {
        return elements == 0;
    }

    @Override
    public void clear() {
        elements = 0;
    }

    @Override
    public Set<E> union(Set<? extends E> other) {
        if (!(other instanceof EnumSet<?>)) {
            throw new IllegalArgumentException("Argument must be an EnumSet");
        }
        EnumSet<E> result = new EnumSet<>(this.elementType);
        result.elements = this.elements | ((EnumSet<?>) other).elements;
        return result;
    }

    @Override
    public Set<E> intersection(Set<? extends E> other) {
        if (!(other instanceof EnumSet<?>)) {
            throw new IllegalArgumentException("Argument must be an EnumSet");
        }
        EnumSet<E> result = new EnumSet<>(this.elementType);
        result.elements = this.elements & ((EnumSet<?>) other).elements;
        return result;
    }

    @Override
    public Set<E> difference(Set<? extends E> other) {
        if (!(other instanceof EnumSet<?>)) {
            throw new IllegalArgumentException("Argument must be an EnumSet");
        }
        EnumSet<E> result = new EnumSet<>(this.elementType);
        result.elements = this.elements & ~((EnumSet<?>) other).elements;
        return result;
    }

    @Override
    public boolean isSubset(Set<? extends E> other) {
        if (!(other instanceof EnumSet<?>)) {
            throw new IllegalArgumentException("Argument must be an EnumSet");
        }
        return (this.elements & ((EnumSet<?>) other).elements) == this.elements;
    }

    @Override
    public boolean isSuperset(Set<? extends E> other) {
        if (!(other instanceof EnumSet<?>)) {
            throw new IllegalArgumentException("Argument must be an EnumSet");
        }
        return (((EnumSet<?>) other).elements & this.elements) == ((EnumSet<?>) other).elements;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("[");
        boolean first = true;
        for (E e : this) {
            if (!first) {
                sb.append(", ");
            }
            first = false;
            sb.append(e.name());
        }
        sb.append("]");
        return sb.toString();
    }

    @Override
    public DynamicArray<E> toDynamicArray() {
        DynamicArray<E> array = new DynamicArray<>();
        for (E e : this) {
            array.add(e);
        }
        return array;
    }

    @Override
    public SingleLinkedList<E> toSingleLinkedList() {
        SingleLinkedList<E> list = new SingleLinkedList<>();
        for (E e : this) {
            list.addLast(e);
        }
        return list;
    }

    @Override
    public boolean equals(Set<? extends E> o) {
        if (!(o instanceof EnumSet<?>)) {
            return false;
        }
        return this.elements == ((EnumSet<?>) o).elements;
    }

    @Override
    @NotNull
    public Iterator<E> iterator() {
        return new Iterator<>() {
            private long bitVector = elements;
            private int nextIndex = 0;

            @Override
            public boolean hasNext() {
                return bitVector != 0;
            }

            @Override
            public E next() {
                if (!hasNext()) {
                    throw new NoSuchElementException();
                }
                while ((bitVector & (1L << nextIndex)) == 0) {
                    nextIndex++;
                }
                E result = elementType.getEnumConstants()[nextIndex];
                bitVector &= ~(1L << nextIndex);
                nextIndex++;
                return result;
            }
        };
    }
}
