package com.MathLingCS.Stack;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import com.MathLingCS.LinkedList.SingleLinkedList;
import com.MathLingCS.Array.DynamicArray;

class SLListStackTest {

    private SLListStack<Integer> stack;

    @BeforeEach
    void setUp() {
        stack = new SLListStack<>();
    }

    @Test
    void testPushAndPop() {
        stack.push(10);
        stack.push(20);
        stack.push(30);

        assertEquals(30, stack.pop());  // Last pushed element should be popped first
        assertEquals(20, stack.pop());
        assertEquals(10, stack.pop());
    }

    @Test
    void testPeek() {
        stack.push(10);
        stack.push(20);
        stack.push(30);

        assertEquals(30, stack.peek());  // Top element should be 30
        assertEquals(30, stack.peek());  // Peek should not remove the element

        stack.pop();
        assertEquals(20, stack.peek());  // After popping, top should be 20
    }

    @Test
    void testIsEmpty() {
        assertTrue(stack.isEmpty());

        stack.push(10);
        assertFalse(stack.isEmpty());

        stack.pop();
        assertTrue(stack.isEmpty());
    }

    @Test
    void testSize() {
        assertEquals(0, stack.size());

        stack.push(10);
        assertEquals(1, stack.size());

        stack.push(20);
        stack.push(30);
        assertEquals(3, stack.size());

        stack.pop();
        assertEquals(2, stack.size());

        stack.clear();
        assertEquals(0, stack.size());
    }

    @Test
    void testClear() {
        stack.push(10);
        stack.push(20);
        stack.push(30);

        stack.clear();
        assertTrue(stack.isEmpty());
        assertEquals(0, stack.size());
    }

    @Test
    void testPopEmptyStack() {
        Exception exception = assertThrows(IllegalStateException.class, () -> {
            stack.pop();
        });

        assertEquals("Stack is empty", exception.getMessage());
    }

    @Test
    void testCopyConstructor() {
        stack.push(10);
        stack.push(20);

        SLListStack<Integer> copiedStack = new SLListStack<>(stack);
        assertEquals(20, copiedStack.pop());
        assertEquals(10, copiedStack.pop());
        assertTrue(copiedStack.isEmpty());
    }

    @Test
    void testConstructorWithList() {
        SingleLinkedList<Integer> list = new SingleLinkedList<>();
        list.addLast(30);
        list.addLast(20);
        list.addLast(10);

        SLListStack<Integer> stackFromList = new SLListStack<>(list);
        assertEquals(10, stackFromList.pop());  // The first element of list becomes the top of stack
        assertEquals(20, stackFromList.pop());
        assertEquals(30, stackFromList.pop());
        assertTrue(stackFromList.isEmpty());
    }

    @Test
    void testConstructorWithDynamicArray() {
        DynamicArray<Integer> array = new DynamicArray<>();
        array.add(10);
        array.add(20);
        array.add(30);

        SLListStack<Integer> stackFromArray = new SLListStack<>(array);
        assertEquals(30, stackFromArray.pop());  // The last element of array becomes the top of stack
        assertEquals(20, stackFromArray.pop());
        assertEquals(10, stackFromArray.pop());
        assertTrue(stackFromArray.isEmpty());
    }

    @Test
    void testPushPopWithMultipleTypes() {
        SLListStack<String> stringStack = new SLListStack<>();
        stringStack.push("A");
        stringStack.push("B");

        assertEquals("B", stringStack.pop());
        assertEquals("A", stringStack.pop());
    }
}
