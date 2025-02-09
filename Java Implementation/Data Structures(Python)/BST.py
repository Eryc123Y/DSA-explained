from abc import ABC, abstractmethod

class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
        
        
    @property
    def is_leaf(self):
        return not self.left and not self.right
    
    @property
    def has_single_child(self):
        return bool(self.left) ^ bool(self.right)
    
    @property
    def has_both_children(self):
        return bool(self.left) and bool(self.right)
    
    def has_left_child(self):
        return self.left is not None
    
    def has_right_child(self):
        return self.right is not None
    
    def __repr__(self):
        return f"Node({self.value})"
    
    def __str__(self):
        return str(self.value)
    
    

class BinaryTree(ABC):
    def __init__(self):
        self.root = None

    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass

    @abstractmethod
    def inorder_traversal(self):
        pass

    @abstractmethod
    def preorder_traversal(self):
        pass

    @abstractmethod
    def postorder_traversal(self):
        pass
    

    def is_empty(self):
        return self.root is None

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))
        return _height(self.root)

    def size(self):
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)
        return _size(self.root)
    
    
class Binary_search_tree(BinaryTree):
    def __init__(self):
        super().__init__()
    
    def insert(self, value):
        def _insert_recursive(current, value):
            if current is None:
                return Node(value, value)
            if value < current.key:
                current.left = _insert_recursive(current.left, value)
                current.left.parent = current
            else:
                current.right = _insert_recursive(current.right, value)
                current.right.parent = current
            return current

        if not self.root:
            self.root = Node(value, value)
        else:
            self.root = _insert_recursive(self.root, value)

    def delete(self, value):
        def _find_min(node):
            while node.left:
                node = node.left
            return node

        def _delete_recursive(current, value):
            if current is None:
                return current
            if value < current.key:
                current.left = _delete_recursive(current.left, value)
            elif value > current.key:
                current.right = _delete_recursive(current.right, value)
            else:
                if current.left is None:
                    temp = current.right
                    current = None
                    return temp
                elif current.right is None:
                    temp = current.left
                    current = None
                    return temp
                temp = _find_min(current.right)
                current.key, current.val = temp.key, temp.val
                current.right = _delete_recursive(current.right, temp.key)
            return current

        self.root = _delete_recursive(self.root, value)

    def search(self, value):
        def _search_recursive(current, value):
            if current is None or current.key == value:
                return current
            if value < current.key:
                return _search_recursive(current.left, value)
            return _search_recursive(current.right, value)

        return _search_recursive(self.root, value)
    
    def inorder_traversal(self):
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.key
                yield from _inorder(node.right)
        
        return list(_inorder(self.root))
    
    def preorder_traversal(self):
        def _preorder(node):
            if node:
                yield node.key
                yield from _preorder(node.left)
                yield from _preorder(node.right)
        
        return list(_preorder(self.root))
    
    def postorder_traversal(self):
        def _postorder(node):
            if node:
                yield from _postorder(node.left)
                yield from _postorder(node.right)
                yield node.key
        
        return list(_postorder(self.root))

# Test cases
def run_tests():
    bst = Binary_search_tree()
    
    # Test insert
    bst.insert(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(3)
    bst.insert(7)
    bst.insert(12)
    bst.insert(18)
    
    assert bst.inorder_traversal() == [3, 5, 7, 10, 12, 15, 18], "Inorder traversal failed"
    assert bst.preorder_traversal() == [10, 5, 3, 7, 15, 12, 18], "Preorder traversal failed"
    assert bst.postorder_traversal() == [3, 7, 5, 12, 18, 15, 10], "Postorder traversal failed"
    
    # Test search
    assert bst.search(15) is not None, "Search failed for value 15"
    assert bst.search(100) is None, "Search failed for value 100"
    
    # Test delete
    bst.delete(15)
    assert bst.inorder_traversal() == [3, 5, 7, 10, 12, 18], "Delete failed for value 15"
    bst.delete(5)
    assert bst.inorder_traversal() == [3, 7, 10, 12, 18], "Delete failed for value 5"
    bst.delete(10)
    assert bst.inorder_traversal() == [3, 7, 12, 18], "Delete failed for value 10"
    
    print("All tests passed.")

run_tests()