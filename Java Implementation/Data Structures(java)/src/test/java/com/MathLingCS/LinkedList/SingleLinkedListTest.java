package com.MathLingCS.LinkedList;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.util.NoSuchElementException;
import java.util.Iterator;
import static org.junit.jupiter.api.Assertions.*;

class SingleLinkedListTest {

    private SingleLinkedList<Integer> list;

    @BeforeEach
    void setUp() {
        list = new SingleLinkedList<>();
    }

    @Test
    void testAddLast() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertEquals(3, list.size());
        assertEquals(1, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(3, list.get(2));
    }

    @Test
    void testAddLastFirst() {
        list.addFirst(1);
        list.addFirst(2);
        list.addFirst(3);
        assertEquals(3, list.size());
        assertEquals(3, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(1, list.get(2));
    }

    @Test
    void testSet() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.set(1, 5);
        assertEquals(5, list.get(1));
        assertThrows(IndexOutOfBoundsException.class, () -> list.set(5, 10));
    }

    @Test
    void testIndexOf() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertEquals(1, list.indexOf(2));
        assertEquals(-1, list.indexOf(5));
    }

    @Test
    void testRemove() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.remove(2);
        assertEquals(2, list.size());
        assertEquals(-1, list.indexOf(2));
        list.remove(1);
        assertEquals(1, list.size());
        assertEquals(3, list.get(0));
    }

    @Test
    void testRemoveAt() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.removeAt(1);
        assertEquals(2, list.size());
        assertEquals(3, list.get(1));
        assertThrows(IndexOutOfBoundsException.class, () -> list.removeAt(5));
    }

    @Test
    void testSize() {
        assertEquals(0, list.size());
        list.addLast(1);
        assertEquals(1, list.size());
    }

    @Test
    void testGet() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertEquals(2, list.get(1));
        assertThrows(IndexOutOfBoundsException.class, () -> list.get(5));
    }

    @Test
    void testIsEmpty() {
        assertTrue(list.isEmpty());
        list.addLast(1);
        assertFalse(list.isEmpty());
    }

    @Test
    void testReverse() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.reverse();
        assertEquals(3, list.get(0));
        assertEquals(2, list.get(1));
        assertEquals(1, list.get(2));
    }

    @Test
    void testContains() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertTrue(list.contains(2));
        assertFalse(list.contains(5));
    }

    @Test
    void testClear() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.clear();
        assertEquals(0, list.size());
        assertTrue(list.isEmpty());
    }

    @Test
    void testIterator() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        Iterator<Integer> iterator = list.iterator();
        assertTrue(iterator.hasNext());
        assertEquals(1, iterator.next());
        assertEquals(2, iterator.next());
        assertEquals(3, iterator.next());
        assertFalse(iterator.hasNext());
        assertThrows(NoSuchElementException.class, iterator::next);
    }

    @Test
    void testToString() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertEquals("[1 -> 2 -> 3]", list.toString());
    }

    @Test
    void testEqualsAndHashCode() {
        SingleLinkedList<Integer> list2 = new SingleLinkedList<>();
        list.addLast(1);
        list.addLast(2);
        list2.addLast(1);
        list2.addLast(2);
        assertTrue(list.equals(list2) && list2.equals(list));
        assertEquals(list.hashCode(), list2.hashCode());
    }
}
