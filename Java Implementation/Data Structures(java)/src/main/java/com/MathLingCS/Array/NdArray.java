package com.MathLingCS.Array;

import org.jetbrains.annotations.NotNull;

import java.util.Iterator;

public class NdArray<T extends Comparable<T>> extends DynamicArray<T> implements Iterable<T> {

    /**
     * Returns an iterator over elements of type {@code T}.
     *
     * @return an Iterator.
     */
    @Override
    public @NotNull Iterator<T> iterator() {
        return null;
    }
}
