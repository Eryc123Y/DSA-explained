package com.MathLingCS.LinkedList;

import com.MathLingCS.Array.DynamicArray;
import com.MathLingCS.Array.SortedArray;
import org.jetbrains.annotations.NotNull;


import java.util.Collection;
import java.util.Iterator;

@SuppressWarnings({"unused", "unchecked"})
public class CircularSLList<T extends Comparable<T>> extends SingleLinkedList<T> {

    public CircularSLList() {
        super();
        if (head != null) {
            tail.next = head;
        }
    }

    public CircularSLList(SingleLinkedList<T> other) {
        super(other);
        if (head != null) {
            tail.next = head;
        }
    }

    public CircularSLList(DynamicArray<T> array) {
        super(array);
        if (head != null) {
            tail.next = head;
        }
    }

    public CircularSLList(Collection<T> collection) {
        super(collection);
        if (head != null) {
            tail.next = head;
        }
    }

    public CircularSLList(SortedArray<T> array) {
        super(array);
        if (head != null) {
            tail.next = head;
        }
    }

    /**
     * Adds an element to the end of the linked list.
     */
    @Override
    public void addLast(T element){
        super.addLast(element);
        if (tail != null && tail.data != null) {
            tail.next = head;
        }
    }
    /**
     * Adds an element to the beginning of the linked list.
     */
    @Override
    public void addFirst(T element){
        super.addFirst(element);
        if (tail != null && tail.data != null) {
            tail.next = head;
        }
    }

    /**
     * Remove an element on the given index.
     */

    @Override
    public T removeAt(int index){
        T removed = super.removeAt(index);
        if (tail != null && tail.data != null) {
            tail.next = head;
        }
        return removed;
    }

    /**
     * Reverse the linked list.
     */
    @Override
    public void reverse() {
        if (head == null || head.next == head) {
            // 空列表或只有一个元素,无需反转
            return;
        }

        Node prev = null;
        Node current = head;
        Node next;
        do {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        } while (current != head);

        // 更新头尾指针
        tail = head;
        head = prev;

        // 恢复循环性
        tail.next = head;
    }

    @Override
    public void remove(T element) {
        if (head == null) {
            return; // 空列表，无需操作
        }

        Node current = head;
        Node prev = tail; // 在循环链表中，第一个节点的前一个是尾节点

        do {
            if (current.data.equals(element)) {
                // 找到要删除的元素
                if (current == head) {
                    // 删除的是头节点
                    head = head.next;
                    tail.next = head;
                    if (head == tail) {
                        // 只有一个元素的情况
                        head = null;
                        tail = null;
                    }
                } else {
                    // 删除的不是头节点
                    prev.next = current.next;
                    if (current == tail) {
                        // 删除的是尾节点
                        tail = prev;
                    }
                }
                size--;
                return; // 删除后退出
            }
            prev = current;
            current = current.next;
        } while (current != head);
    }

    public boolean isCircular() {
    if (head == null) return true;
    Node slow = head;
    Node fast = head.next;
    while (fast != null && fast.next != null) {
        if (slow == fast) return true;
        slow = slow.next;
        fast = fast.next.next;
    }
    return false;
}

    @Override
    public String toString() {
        if (head == null) return "[]";
        StringBuilder result = new StringBuilder("[");
        Node current = head;
        boolean first = true;
        while (current != head || first) {
            first = false;
            result.append(current.data);
            if (current.next != head) {
                result.append(" -> ");
            }
            current = current.next;
        }
        result.append("]");
        return result.toString();
    }

    public void rotateRight() {
        if (size > 1) {
            Node secondLast = head;
            while (secondLast.next != tail) {
                secondLast = secondLast.next;
            }
            tail.next = head;
            head = tail;
            tail = secondLast;
            tail.next = head;
        }
    }

    public void rotateLeft() {
        if (size > 1) {
            tail = head;
            head = head.next;
            tail.next = head;
        }

    }

    @Override
    public @NotNull Iterator<T> iterator() {
        return new Iterator<>() {
            private Node current = head;
            private boolean first = true;

            @Override
            public boolean hasNext() {
                return (current != head || first) && current != null;
            }

            @Override
            public T next() {
                if (!hasNext()) {
                    throw new IndexOutOfBoundsException("No more elements in the list.");
                }
                T data = current.data;
                current = current.next;
                first = false;
                return data;
            }
        };
    }

}
