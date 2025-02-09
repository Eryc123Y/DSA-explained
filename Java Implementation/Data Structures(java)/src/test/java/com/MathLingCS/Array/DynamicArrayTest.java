package com.MathLingCS.Array;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class DynamicArrayTest {

    @Test
    public void testAddAndGet() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        assertEquals(1, array.get(0));
        assertEquals(2, array.get(1));
        assertEquals(3, array.get(2));
    }

    @Test
    public void testRemove() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.remove(1);
        assertEquals(2, array.size());
        assertEquals(1, array.get(0));
        assertEquals(3, array.get(1));
    }

    @Test
    public void testIsEmpty() {
        DynamicArray<Integer> array = new DynamicArray<>();
        assertTrue(array.isEmpty());
        array.add(1);
        assertFalse(array.isEmpty());
    }

    @Test
    public void testContains() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        assertTrue(array.contains(2));
        assertFalse(array.contains(4));
    }

    @Test
    public void testClear() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.clear();
        assertTrue(array.isEmpty());
        assertEquals(0, array.size());
    }

    @Test
    public void testSet() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        array.set(1, 5);
        assertEquals(5, array.get(1));
    }

    @Test
    public void testResize() {
        DynamicArray<Integer> array = new DynamicArray<>(2);
        array.add(1);
        array.add(2);
        array.add(3);
        assertEquals(3, array.size());
        assertEquals(4, array.capacity()); // Capacity should double when resized
    }

    @Test
    public void testToArray() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        Integer[] expectedArray = {1, 2, 3};
        assertArrayEquals(expectedArray, array.toArray());
    }

    @Test
    public void testCapacity() {
        DynamicArray<Integer> array = new DynamicArray<>(10);
        assertEquals(10, array.capacity());
    }

    @Test
    public void testInitialCapacity() {
        DynamicArray<Integer> array = new DynamicArray<>();
        assertEquals(16, array.capacity());
    }
}