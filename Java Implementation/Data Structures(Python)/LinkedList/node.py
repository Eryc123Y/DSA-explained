from typing import TypeVar, Generic, Optional, Tuple

T = TypeVar('T')

__author__ = 'Maria Garcia de la Banda and Brendon Taylor. Modified by Alexey Ignatiev'
__docformat__ = 'reStructuredText'

class Node(Generic[T]):
    """ Simple linked node. It contains an item and has a reference to next node. """

    def __init__(self, item: T = None) -> None:
        """ Node initialiser. """
        self.item = item
        self.next = None

def remove(head: Optional[Node[T]], item: T) -> Tuple[Optional[Node[T]], bool]:
    """Remove the first occurrence of item from the list.
       Returns the possibly updated head and a boolean indicating
       whether the item was successfully removed."""
    if head is None:
        return None, False
    
    if head.item == item:
        return head.next, True
    
    current = head
    while current.next is not None and current.next.item != item:
        current = current.next
    
    if current.next is not None:
        current.next = current.next.next
        return head, True
    
    return head, False

def insert(head: Optional[Node[T]], index: int, item: T) -> Optional[Node[T]]:
    """Insert item at index in the list.
       Returns the possibly updated head."""
    
    # if index is 0, we need to insert at the beginning
    if index == 0:
        new_node = Node(item)
        new_node.next = head
        return new_node
    
    # if index is not 0, we need to find the node at index - 1
    current = head
    for _ in range(index - 1):
        # if current is None, we cannot insert at index
        if current is None:
            return head
        current = current.next
    
    # if current is None, we cannot insert at index
    if current is None:
        return head
    
    new_node = Node(item)
    new_node.next = current.next
    current.next = new_node
    return head

def reverse(head: Optional[Node[T]]) -> Optional[Node[T]]:
    """Reverse the linked list."""
    current = head
    previous = None
    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def shift(head: Optional[Node[T]], length: int, step: int = 1) -> Optional[Node[T]]:
    """Shift the items in the list. Positive step shifts right, negative step shifts left."""
    if head is None or step == 0:
        return head
    
    step = step % length
    
    if step == 0:
        return head
    
    if step < 0:  # Negative step for left shift
        step = -step
    else:  # Positive step for right shift
        step = length - step
    
    current = head
    for _ in range(step - 1):
        current = current.next
    
    new_head = current.next
    current.next = None
    
    current = new_head
    while current.next is not None:
        current = current.next
    
    current.next = head
    return new_head