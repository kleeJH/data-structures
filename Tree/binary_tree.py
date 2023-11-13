""" Binary Tree Implementation. """

from typing import Callable


class Node[T]:
    def __init__(self, item: T = None) -> None:
        self.item = item
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return str(self.item)


class BinaryTree[T]:
    def __init__(self) -> None:
        self.root = None

    def __len__(self) -> int:
        return self.len_aux(self.root)

    def len_aux(self, current: T) -> int:
        if current is None:
            return 0
        else:
            return 1 + self.len_aux(current.left) + self.len_aux(current.right)

    def is_empty(self) -> bool:
        return self.root is None

    def preorder(self, f: Callable) -> None:
        """ Pre-order traversal using callable function. """
        self.preorder_aux(self.root, f)

    def preorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:
            f(current.item)
            self.preorder_aux(current.left, f)
            self.preorder_aux(current.right, f)

    def inorder(self, f: Callable) -> None:
        """ In-order traversal using callable function. """
        self.inorder_aux(self.root, f)

    def inorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:
            self.inorder_aux(current.left, f)
            f(current.item)
            self.inorder_aux(current.right, f)

    def postorder(self, f: Callable) -> None:
        """ Post-order traversal using callable function. """
        self.postorder_aux(self.root, f)

    def postorder_aux(self, current: T, f: Callable) -> None:
        if current is not None:
            self.postorder_aux(current.left, f)
            self.postorder_aux(current.right, f)
            f(current.item)
