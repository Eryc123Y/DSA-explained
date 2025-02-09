package com.MathLingCS.Queue;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.LinkedList.SingleLinkedList;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class LinkedQueueTest {

    private LinkedQueue<Integer> queue;

    @BeforeEach
    void setUp() {
        queue = new LinkedQueue<>();
    }

    @Test
    void testEnqueue() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        assertEquals(3, queue.size());
        assertEquals(10, queue.peek());
    }

    @Test
    void testDequeue() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);
        assertEquals(10, queue.dequeue());
        assertEquals(20, queue.peek());
        assertEquals(2, queue.size());
    }

    @Test
    void testPeek() {
        queue.enqueue(10);
        assertEquals(10, queue.peek());
        queue.enqueue(20);
        assertEquals(10, queue.peek());
        queue.dequeue();
        assertEquals(20, queue.peek());
    }

    @Test
    void testSize() {
        assertEquals(0, queue.size());
        queue.enqueue(10);
        assertEquals(1, queue.size());
        queue.enqueue(20);
        assertEquals(2, queue.size());
    }

    @Test
    void testIsEmpty() {
        assertTrue(queue.isEmpty());
        queue.enqueue(10);
        assertFalse(queue.isEmpty());
        queue.dequeue();
        assertTrue(queue.isEmpty());
    }

    @Test
    void testClear() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.clear();
        assertTrue(queue.isEmpty());
        assertEquals(0, queue.size());
    }

    @Test
    void testIterator() {
        queue.enqueue(10);
        queue.enqueue(20);
        queue.enqueue(30);

        int sum = 0;
        for (int value : queue) {
            sum += value;
        }

        assertEquals(60, sum);
    }

    @Test
    void testIsFull() {
        assertFalse(queue.isFull());  // isFull should always return false
    }

    @Test
    void testConstructorWithSingleLinkedList() {
        SingleLinkedList<Integer> linkedList = new SingleLinkedList<>();
        linkedList.addFirst(10);
        linkedList.addFirst(20);
        LinkedQueue<Integer> newQueue = new LinkedQueue<>(linkedList);

        assertEquals(10, newQueue.peek());
        assertEquals(2, newQueue.size());
    }

    @Test
    void testConstructorWithDynamicArray() {
        DynamicArray<Integer> dynamicArray = new DynamicArray<>();
        dynamicArray.add(10);
        dynamicArray.add(20);
        LinkedQueue<Integer> newQueue = new LinkedQueue<>(dynamicArray);

        assertEquals(20, newQueue.peek());
        assertEquals(2, newQueue.size());
    }

    @Test
    void testCopyConstructor() {
        queue.enqueue(10);
        queue.enqueue(20);
        LinkedQueue<Integer> copiedQueue = new LinkedQueue<>(queue);

        assertEquals(10, copiedQueue.peek());
        assertEquals(2, copiedQueue.size());
    }

    @Test
    void testEnqueueDequeueSequence() {
        queue.enqueue(10);
        queue.enqueue(20);
        assertEquals(10, queue.dequeue());
        queue.enqueue(30);
        assertEquals(20, queue.dequeue());
        assertEquals(30, queue.peek());
    }
}
