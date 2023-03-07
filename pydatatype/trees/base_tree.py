"""
This module provides a base class for all tree implementations.
"""

from typing import Optional
from abc import ABC, abstractmethod
from pydatatype.node import Node
from pydatatype.utils.traversals import (
    PreOrderIterator,
    InOrderIterator,
    PostOrderIterator,
    LevelOrderIterator,
)


class Tree(ABC):
    """
    Abstract base class for all tree implementations.
    """

    def __init__(self, root: Optional[Node] = None):
        if root is not None and not isinstance(root, Node):
            raise TypeError("The argument 'root' must be of type 'Node'")
        self.root = root
        self.size = 0

    @property
    def right(self):
        """
        The right subtree of the tree.
        """

    @property
    def left(self):
        """
        The left subtree of the tree.
        """

    def preorder(self):
        """
        Returns an iterator that traverses the tree in pre-order.
        """
        return PreOrderIterator(self)

    def inorder(self):
        """
        Returns an iterator that traverses the tree in-order.
        """
        return InOrderIterator(self)

    def postorder(self):
        """
        Returns an iterator that traverses the tree in post-order.
        """
        return PostOrderIterator(self)

    def levelorder(self):
        """
        Returns an iterator that traverses the tree in level-order.
        """
        return LevelOrderIterator(self)

    @abstractmethod
    def get_height(self):
        """
        Returns the height of the tree.
        """

    @abstractmethod
    def insert(self, node: Node):
        """
        Inserts a node into the tree.
        """

    @abstractmethod
    def merge(self, tree: "Tree"):
        """
        Merges the given tree into the current tree.
        """

    @abstractmethod
    def search(self, value):
        """
        Searches for a node with the given value in the tree.
        """

    @abstractmethod
    def delete(self, value):
        """
        Deletes a node with the given value from the tree.
        """

    @abstractmethod
    def delete_tree(self):
        """
        Deletes the entire tree.
        """

    @abstractmethod
    def clone(self):
        """
        Returns a copy of the tree.
        """
