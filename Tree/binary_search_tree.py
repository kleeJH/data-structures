""" Binary Search Tree Implementation. """

import sys
from enum import Enum
from binary_tree import BinaryTree

sys.path.insert(0, "./Stack")
sys.path.insert(0, "./List")

from stack import LinkStack
from list import LinkList

class Node[K, I]:
    def __init__(self, key: K, item: I = None) -> None:
        self.key = key
        self.item = item
        self.left = None
        self.right = None

    def __str__(self):
        return " (" + str(self.key) + ", " + str(self.item) + " ) "

class TraversalType(Enum):
    PRE_ORDER = 0,
    IN_ORDER = 1,
    POST_ORDER = 2

class BSTTraversalIterator[K, I]:
    def __init__(self, root: Node[K, I], traversal_type: TraversalType = TraversalType.IN_ORDER) -> None:
        self.traversal_type = traversal_type

        # Intialize Stack
        self.stack = LinkStack()

        # Prepare 
        if self.traversal_type == TraversalType.PRE_ORDER:
            self.stack.push(root)
        elif self.traversal_type == TraversalType.IN_ORDER:
            cur = root
            while cur is not None:
                self.stack.push(cur)
                cur = cur.left
        else: # POST_ORDER
            self.visit = LinkStack()

            # Setup
            self.stack.push(root)
            self.visit.push(False)

    def __iter__(self) -> 'BSTTraversalIterator':
        return self

    def __next__(self) -> tuple((K, I)):
        """ Gets the next item in a specific traversal. """
        if self.stack.is_empty():
                raise StopIteration
        
        if self.traversal_type == TraversalType.PRE_ORDER:
            current = self.stack.pop()
            if current.right is not None:
                self.stack.push(current.right)
            if current.left is not None:
                self.stack.push(current.left)

        elif self.traversal_type == TraversalType.IN_ORDER:
            current = self.stack.pop()
            cur = current.right
            while cur is not None:
                self.stack.push(cur)
                cur = cur.left

        else: # POST_ORDER
            current = None

            while current is None:
                cur, visited = self.stack.pop(), self.visit.pop()

                if cur is not None:
                    if visited:
                        current = cur
                    else:
                        # Visited cur node 
                        self.stack.push(cur)
                        self.visit.push(True)

                        # Check left subtree, then right subtree. For stack, we push the right node first, then the left node (the order matters). We also have not visited the nodes yet!
                        if cur.right is not None:
                            self.stack.push(cur.right)
                            self.visit.push(False)
                        
                        if cur.left is not None:
                            self.stack.push(cur.left)
                            self.visit.push(False)

        return current.item


class BinarySearchTree[K, I](BinaryTree[K]):
    def __init__(self, traversal_type: TraversalType = TraversalType.IN_ORDER) -> None:
        self.root = None
        self.traversal_type = traversal_type

    def is_empty(self) -> bool:
        return self.root is None

    def __contains__(self, key: K) -> bool:
        """ Checks to see if the key is in the BST. """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: K) -> tuple((K, I)):
        """ Tries to retrieve the item from the tree using the Key. """
        return self.__getitem_aux(self.root, key)

    def __iter__(self) -> BSTTraversalIterator:
        return BSTTraversalIterator(self.root, self.traversal_type)

    def __getitem_aux(self, current: Node, key: K) -> tuple((K, I)):
        if current is None:  # base case: empty
            raise KeyError("Key not found")
        elif key == current.key:  # base case: found
            return (current.key, current.item)
        elif key < current.key:
            return self.__getitem_aux(current.left, key)
        else:  # key > current.key
            return self.__getitem_aux(current.right, key)

    def __setitem__(self, key: K, item: I) -> None:
        """ Tries to insert the item into the tree using the key. """
        self.root = self.__insert_aux(self.root, key, item)

    def __insert_aux(self, current: Node, key: K, item: I) -> Node:
        if current is None:  # base case: at the leaf
            current = Node(key, item)
        elif key < current.key:
            current.left = self.__insert_aux(current.left, key, item)
        elif key > current.key:
            current.right = self.__insert_aux(current.right, key, item)
        else:  # key == current.key
            raise ValueError("Inserting duplicate item")
        return current

    def get_leaves(self) -> LinkList:
        """ Retrieves all the items that are leaf nodes. """
        a_list = LinkList()
        self.__get_leaves_aux(self.root, a_list)
        return a_list

    def is_leaf(self, current: Node) -> bool:
        return current.left is None and current.right is None

    def __get_leaves_aux(self, current: Node, a_list: LinkList) -> None:
        if current is not None:
            if self.is_leaf(current):
                a_list.append(current.item)
            else:
                self.__get_leaves_aux(current.left, a_list)
                self.__get_leaves_aux(current.right, a_list)

    def get_max(self) -> tuple((K, I)):
        """ Get the maximum element in the BST. """
        if self.root is None:
            raise ValueError("Tree is empty")
        elif self.root.right is None:  # root has the max
            temp = (self.root.key, self.root.item)
            self.root = self.root.left  # delete root
            return temp
        else:
            return self.get_max_aux(self.root.right, self.root)

    def get_max_aux(self, current, parent) -> tuple((K, I)):
        if current.right is None:  # base case: at max
            parent.right = current.left
            return (current.key, current.item)
        else:
            return self.get_max_aux(current.right, current)