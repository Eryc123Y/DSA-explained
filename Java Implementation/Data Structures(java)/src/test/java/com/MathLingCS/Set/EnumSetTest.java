package com.MathLingCS.Set;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Iterator;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

enum TestEnum {
    ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT
}

class EnumSetTest {

    private EnumSet<TestEnum> enumSet;

    @BeforeEach
    void setUp() {
        enumSet = new EnumSet<>(TestEnum.class);
    }

    @Test
    void testAdd() {
        assertTrue(enumSet.add(TestEnum.ONE));
        assertFalse(enumSet.add(TestEnum.ONE));
        assertTrue(enumSet.contains(TestEnum.ONE));
        assertEquals(1, enumSet.size());
    }

    @Test
    void testRemove() {
        assertFalse(enumSet.remove(TestEnum.ONE));
        enumSet.add(TestEnum.ONE);
        assertTrue(enumSet.remove(TestEnum.ONE));
        assertFalse(enumSet.contains(TestEnum.ONE));
        assertEquals(0, enumSet.size());
    }

    @Test
    void testContains() {
        assertFalse(enumSet.contains(TestEnum.ONE));
        enumSet.add(TestEnum.ONE);
        assertTrue(enumSet.contains(TestEnum.ONE));
    }

    @Test
    void testSize() {
        assertEquals(0, enumSet.size());
        enumSet.add(TestEnum.THREE);
        assertEquals(1, enumSet.size());
        enumSet.add(TestEnum.FOUR);
        assertEquals(2, enumSet.size());
        enumSet.remove(TestEnum.THREE);
        assertEquals(1, enumSet.size());
        enumSet.clear();
        assertEquals(0, enumSet.size());
    }

    @Test
    void testIsEmpty() {
        assertTrue(enumSet.isEmpty());
        enumSet.add(TestEnum.ONE);
        assertFalse(enumSet.isEmpty());
    }

    @Test
    void testClear() {
        enumSet.add(TestEnum.TWO);
        enumSet.add(TestEnum.THREE);
        assertEquals(2, enumSet.size());
        enumSet.clear();
        assertTrue(enumSet.isEmpty());
        assertEquals(0, enumSet.size());
    }

    @Test
    void testUnion() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        enumSet.add(TestEnum.ONE);
        otherSet.add(TestEnum.TWO);
        Set<TestEnum> unionSet = enumSet.union(otherSet);
        assertTrue(unionSet.contains(TestEnum.ONE));
        assertTrue(unionSet.contains(TestEnum.TWO));
        assertEquals(2, unionSet.size());
    }

    @Test
    void testIntersection() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.THREE);
        Set<TestEnum> intersectionSet = enumSet.intersection(otherSet);
        assertTrue(intersectionSet.contains(TestEnum.TWO));
        assertFalse(intersectionSet.contains(TestEnum.ONE));
        assertFalse(intersectionSet.contains(TestEnum.THREE));
        assertEquals(1, intersectionSet.size());
    }

    @Test
    void testDifference() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.THREE);
        Set<TestEnum> differenceSet = enumSet.difference(otherSet);
        assertTrue(differenceSet.contains(TestEnum.ONE));
        assertFalse(differenceSet.contains(TestEnum.TWO));
        assertFalse(differenceSet.contains(TestEnum.THREE));
        assertEquals(1, differenceSet.size());
    }

    @Test
    void testIsSubset() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.ONE);
        otherSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.THREE);
        assertTrue(enumSet.isSubset(otherSet));
        assertFalse(otherSet.isSubset(enumSet));
    }

    @Test
    void testIsSuperset() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        otherSet.add(TestEnum.ONE);
        assertTrue(enumSet.isSuperset(otherSet));
        assertFalse(otherSet.isSuperset(enumSet));
    }

    @Test
    void testToString() {
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        assertEquals("[ONE, TWO]", enumSet.toString());
    }

    @Test
    void testIterator() {
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.THREE);
        Iterator<TestEnum> iterator = enumSet.iterator();
        assertTrue(iterator.hasNext());
        assertEquals(TestEnum.ONE, iterator.next());
        assertTrue(iterator.hasNext());
        assertEquals(TestEnum.THREE, iterator.next());
        assertFalse(iterator.hasNext());
    }

    @Test
    void testIteratorNoSuchElementException() {
        enumSet.add(TestEnum.ONE);
        Iterator<TestEnum> iterator = enumSet.iterator();
        iterator.next();
        assertThrows(NoSuchElementException.class, iterator::next);
    }

    @Test
    void testEquals() {
        EnumSet<TestEnum> otherSet = new EnumSet<>(TestEnum.class);
        assertTrue(enumSet.equals(otherSet));
        enumSet.add(TestEnum.ONE);
        assertFalse(enumSet.equals(otherSet));
        otherSet.add(TestEnum.ONE);
        assertTrue(enumSet.equals(otherSet));
    }

    @Test
    void testToDynamicArray() {
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        DynamicArray<TestEnum> array = enumSet.toDynamicArray();
        assertEquals(2, array.size());
        assertEquals(TestEnum.ONE, array.get(0));
        assertEquals(TestEnum.TWO, array.get(1));
    }

    @Test
    void testToSingleLinkedList() {
        enumSet.add(TestEnum.ONE);
        enumSet.add(TestEnum.TWO);
        SingleLinkedList<TestEnum> list = enumSet.toSingleLinkedList();
        assertEquals(2, list.size());
        assertEquals(TestEnum.ONE, list.get(0));
        assertEquals(TestEnum.TWO, list.get(1));
    }
}
