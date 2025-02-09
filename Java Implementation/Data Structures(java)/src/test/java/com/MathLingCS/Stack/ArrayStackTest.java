package com.MathLingCS.Stack;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ArrayStackTest {

    @Test
    public void testPush() {
        ArrayStack<Integer> stack = new ArrayStack<>();
        stack.push(1);
        assertEquals(1, stack.size());
        assertEquals(1, stack.peek());
    }

    @Test
    public void testPop() {
        ArrayStack<Integer> stack = new ArrayStack<>();
        stack.push(1);
        stack.push(2);
        assertEquals(2, stack.pop());
        assertEquals(1, stack.size());
        assertEquals(1, stack.peek());
    }

    @Test
    public void testPeek() {
        ArrayStack<Integer> stack = new ArrayStack<>();
        stack.push(1);
        assertEquals(1, stack.peek());
    }

    @Test
    public void testIsEmpty() {
        ArrayStack<Integer> stack = new ArrayStack<>();
        assertTrue(stack.isEmpty());
        stack.push(1);
        assertFalse(stack.isEmpty());
    }

    @Test
    public void testClear() {
        ArrayStack<Integer> stack = new ArrayStack<>();
        stack.push(1);
        stack.push(2);
        stack.clear();
        assertTrue(stack.isEmpty());
    }
}