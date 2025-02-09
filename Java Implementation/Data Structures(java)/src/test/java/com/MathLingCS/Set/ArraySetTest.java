package com.MathLingCS.Set;

import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;

import java.util.Iterator;

class ArraySetTest {

    private ArraySet<Integer> set1;
    private ArraySet<Integer> set2;

    @BeforeEach
    void setUp() {
        set1 = new ArraySet<>();
        set1.add(1);
        set1.add(2);
        set1.add(3);
        set1.add(4);

        set2 = new ArraySet<>();
        set2.add(3);
        set2.add(4);
        set2.add(5);
        set2.add(6);
    }

    @Test
    void testAdd() {
        assertTrue(set1.add(5));
        assertFalse(set1.add(1));
        assertEquals(5, set1.size());
    }

    @Test
    void testRemove() {
        assertTrue(set1.remove(3));
        assertFalse(set1.remove(10));
        assertEquals(3, set1.size());
    }

    @Test
    void testContains() {
        assertTrue(set1.contains(2));
        assertFalse(set1.contains(5));
    }

    @Test
    void testSize() {
        assertEquals(4, set1.size());
        set1.add(5);
        assertEquals(5, set1.size());
    }

    @Test
    void testIsEmpty() {
        assertFalse(set1.isEmpty());
        ArraySet<Integer> emptySet = new ArraySet<>();
        assertTrue(emptySet.isEmpty());
    }

    @Test
    void testClear() {
        set1.clear();
        assertTrue(set1.isEmpty());
        assertEquals(0, set1.size());
    }

    @Test
    void testUnion() {
        Set<Integer> union = set1.union(set2);
        assertEquals(6, union.size());
        assertTrue(union.contains(1));
        assertTrue(union.contains(2));
        assertTrue(union.contains(3));
        assertTrue(union.contains(4));
        assertTrue(union.contains(5));
        assertTrue(union.contains(6));
    }

    @Test
    void testIntersection() {
        Set<Integer> intersection = set1.intersection(set2);
        assertEquals(2, intersection.size());
        assertTrue(intersection.contains(3));
        assertTrue(intersection.contains(4));
    }

    @Test
    void testDifference() {
        Set<Integer> difference = set1.difference(set2);
        assertEquals(2, difference.size());
        assertTrue(difference.contains(1));
        assertTrue(difference.contains(2));
    }

    @Test
    void testIsSubset() {
        ArraySet<Integer> subset = new ArraySet<>();
        subset.add(1);
        subset.add(2);
        assertTrue(subset.isSubset(set1));
        assertFalse(set1.isSubset(set2));
    }

    @Test
    void testIsSuperset() {
        ArraySet<Integer> subset = new ArraySet<>();
        subset.add(1);
        subset.add(2);
        assertTrue(set1.isSuperset(subset));
        assertFalse(set1.isSuperset(set2));
    }

    @Test
    void testToDynamicArray() {
        DynamicArray<Integer> dynamicArray = set1.toDynamicArray();
        assertEquals(4, dynamicArray.size());
        assertTrue(dynamicArray.contains(1));
        assertTrue(dynamicArray.contains(2));
        assertTrue(dynamicArray.contains(3));
        assertTrue(dynamicArray.contains(4));
    }

    @Test
    void testToSingleLinkedList() {
        SingleLinkedList<Integer> linkedList = set1.toSingleLinkedList();
        assertEquals(4, linkedList.size());
        assertTrue(linkedList.contains(1));
        assertTrue(linkedList.contains(2));
        assertTrue(linkedList.contains(3));
        assertTrue(linkedList.contains(4));
    }

    @Test
    void testToString() {
        String setString = set1.toString();
        assertTrue(setString.contains("1"));
        assertTrue(setString.contains("2"));
        assertTrue(setString.contains("3"));
        assertTrue(setString.contains("4"));
    }

    @Test
    void testIterator() {
        Iterator<Integer> iterator = set1.iterator();
        int count = 0;
        while (iterator.hasNext()) {
            Integer element = iterator.next();
            assertTrue(set1.contains(element));
            count++;
        }
        assertEquals(4, count);
    }

    @Test
    void testCopyConstructor() {
        ArraySet<Integer> set3 = new ArraySet<>(set1);
        assertEquals(set1.size(), set3.size());
        for (Integer element : set1) {
            assertTrue(set3.contains(element));
        }
        set1.add(5);
        assertFalse(set3.contains(5));
    }
}