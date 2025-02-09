package com.MathLingCS.LinkedList;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.Array.SortedArray;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Arrays;
import java.util.Iterator;
import java.util.NoSuchElementException;

import static org.junit.jupiter.api.Assertions.*;

public class CircularSLListTest {

    private CircularSLList<Integer> list;

    @BeforeEach
    void setUp() {
        list = new CircularSLList<>();
    }

    @Test
    void testConstructor() {
        assertTrue(list.isEmpty());
        assertEquals(0, list.size());
    }

    @Test
    void testAddLast() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        assertEquals(3, list.size());
        assertEquals("[1 -> 2 -> 3]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testAddFirst() {
        list.addFirst(1);
        list.addFirst(2);
        list.addFirst(3);
        assertEquals(3, list.size());
        assertEquals("[3 -> 2 -> 1]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testRemoveAt() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        Integer removed = list.removeAt(1);
        assertEquals(2, removed);
        assertEquals(2, list.size());
        assertEquals("[1 -> 3]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testRemove() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.remove(2);
        assertEquals(2, list.size());
        assertEquals("[1 -> 3]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testReverse() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.reverse();
        assertEquals("[3 -> 2 -> 1]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testIsCircular() {
        assertTrue(list.isCircular());  // Empty list is considered circular
        list.addLast(1);
        assertTrue(list.isCircular());
        list.addLast(2);
        assertTrue(list.isCircular());
    }

    @Test
    void testRotateRight() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.rotateRight();
        assertEquals("[3 -> 1 -> 2]", list.toString());
        assertTrue(list.isCircular());
    }

    @Test
    void testRotateLeft() {
        list.addLast(1);
        list.addLast(2);
        list.addLast(3);
        list.rotateLeft();
        assertEquals("[2 -> 3 -> 1]", list.toString());
        assertTrue(list.isCircular());
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
    }

    @Test
    void testIteratorEmptyList() {
        Iterator<Integer> iterator = list.iterator();
        assertFalse(iterator.hasNext());
        assertThrows(IndexOutOfBoundsException.class, iterator::next);
    }

    @Test
    void testConstructorWithSingleLinkedList() {
        SingleLinkedList<Integer> singleList = new SingleLinkedList<>();
        singleList.addLast(1);
        singleList.addLast(2);
        singleList.addLast(3);
        CircularSLList<Integer> circularList = new CircularSLList<>(singleList);
        assertEquals("[1 -> 2 -> 3]", circularList.toString());
        assertTrue(circularList.isCircular());
    }

    @Test
    void testConstructorWithDynamicArray() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(1);
        array.add(2);
        array.add(3);
        CircularSLList<Integer> circularList = new CircularSLList<>(array);
        assertEquals("[1 -> 2 -> 3]", circularList.toString());
        assertTrue(circularList.isCircular());
    }

    @Test
    void testConstructorWithCollection() {
        CircularSLList<Integer> circularList = new CircularSLList<>(Arrays.asList(1, 2, 3));
        assertEquals("[1 -> 2 -> 3]", circularList.toString());
        assertTrue(circularList.isCircular());
    }

    @Test
    void testConstructorWithSortedArray() {
        SortedArray<Integer> sortedArray = new SortedArray<>();
        sortedArray.add(3);
        sortedArray.add(1);
        sortedArray.add(2);
        CircularSLList<Integer> circularList = new CircularSLList<>(sortedArray);
        assertEquals("[1 -> 2 -> 3]", circularList.toString());
        assertTrue(circularList.isCircular());
    }

    @Test
    void testEdgeCases() {
        // Test with one element
        list.addLast(1);
        assertEquals("[1]", list.toString());
        assertTrue(list.isCircular());
        list.rotateRight();
        assertEquals("[1]", list.toString());
        list.rotateLeft();
        assertEquals("[1]", list.toString());

        // Test removing the last element
        list.remove(1);
        assertTrue(list.isEmpty());
        assertEquals("[]", list.toString());
        assertTrue(list.isCircular());

        // Test adding after removing all elements
        list.addLast(2);
        assertEquals("[2]", list.toString());
        assertTrue(list.isCircular());
    }
}