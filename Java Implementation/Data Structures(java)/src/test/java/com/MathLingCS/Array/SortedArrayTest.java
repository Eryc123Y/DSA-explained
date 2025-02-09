package com.MathLingCS.Array;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class SortedArrayTest {

    private SortedArray<Integer> sortedArray;

    @BeforeEach
    void setUp() {
        sortedArray = new SortedArray<>();
    }

    @Test
    void testConstructor() {
        assertEquals(0, sortedArray.size());
        assertTrue(sortedArray.isEmpty());
    }

    @Test
    void testAddAndSize() {
        sortedArray.add(3);
        sortedArray.add(1);
        sortedArray.add(4);
        sortedArray.add(1);
        sortedArray.add(5);

        assertEquals(5, sortedArray.size());
        assertFalse(sortedArray.isEmpty());
    }

    @Test
    void testAddMaintainsSortedOrder() {
        sortedArray.add(3);
        sortedArray.add(1);
        sortedArray.add(4);
        sortedArray.add(1);
        sortedArray.add(5);

        assertEquals(1, sortedArray.get(0));
        assertEquals(1, sortedArray.get(1));
        assertEquals(3, sortedArray.get(2));
        assertEquals(4, sortedArray.get(3));
        assertEquals(5, sortedArray.get(4));
    }

    @Test
    void testFind() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        assertEquals(0, sortedArray.find(1));
        assertEquals(1, sortedArray.find(3));
        assertEquals(2, sortedArray.find(5));
        assertEquals(-1, sortedArray.find(2));
        assertEquals(-1, sortedArray.find(6));
    }

    @Test
    void testContains() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        assertTrue(sortedArray.contains(1));
        assertTrue(sortedArray.contains(3));
        assertTrue(sortedArray.contains(5));
        assertFalse(sortedArray.contains(2));
        assertFalse(sortedArray.contains(6));
    }

    @Test
    void testInsert() {
        sortedArray.insert(0, 3);
        sortedArray.insert(0, 1);
        sortedArray.insert(2, 5);

        assertEquals(3, sortedArray.size());
        assertEquals(1, sortedArray.get(0));
        assertEquals(3, sortedArray.get(1));
        assertEquals(5, sortedArray.get(2));
    }

    @Test
    void testSet() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        assertThrows(UnsupportedOperationException.class, () -> sortedArray.set(1, 4));
    }

    @Test
    void testSort() {
        sortedArray.add(3);
        sortedArray.add(1);
        sortedArray.add(4);

        sortedArray.sort();

        assertEquals(1, sortedArray.get(0));
        assertEquals(3, sortedArray.get(1));
        assertEquals(4, sortedArray.get(2));
    }

    @Test
    void testRemove() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        sortedArray.remove(1);

        assertEquals(2, sortedArray.size());
        assertEquals(1, sortedArray.get(0));
        assertEquals(5, sortedArray.get(1));
    }

    @Test
    void testClear() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        sortedArray.clear();

        assertEquals(0, sortedArray.size());
        assertTrue(sortedArray.isEmpty());
    }

    @Test
    void testToArray() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        Object[] array = sortedArray.toArray();

        assertEquals(3, array.length);
        assertEquals(1, array[0]);
        assertEquals(3, array[1]);
        assertEquals(5, array[2]);
    }

    @Test
    void testIterator() {
        sortedArray.add(1);
        sortedArray.add(3);
        sortedArray.add(5);

        int sum = 0;
        for (Integer i : sortedArray) {
            sum += i;
        }

        assertEquals(9, sum);
    }

    @Test
    void testAddDuplicates() {
        sortedArray.add(1);
        sortedArray.add(1);
        sortedArray.add(2);
        sortedArray.add(2);

        assertEquals(4, sortedArray.size());
        assertEquals(1, sortedArray.get(0));
        assertEquals(1, sortedArray.get(1));
        assertEquals(2, sortedArray.get(2));
        assertEquals(2, sortedArray.get(3));
    }

    @Test
    void testAddAndRemoveMultiple() {
        for (int i = 0; i < 1000; i++) {
            sortedArray.add(i);
        }

        assertEquals(1000, sortedArray.size());

        for (int i = 0; i < 500; i++) {
            sortedArray.remove(0);
        }

        assertEquals(500, sortedArray.size());
        assertEquals(500, sortedArray.get(0));
    }
}