"""
This module provides a BinarySearchTreeNode class that can be used to build
a binary search tree.

A binary search tree is a binary tree where each node has at most two children,
and the key value of each node is greater than or equal to the key value of all
nodes in its left subtree, and less than or equal to the key value of all nodes
in its right subtree. This property makes searching, insertion, and deletion
operations efficient in the tree.

Classes:
- BinarySearchTreeNode: A class that represents a node in a binary search tree.
"""

from .node import Node


class BSTreeNode(Node):
    """
    A class that represents a node in a binary search tree.

    Each node has a key-value pair, where the key is used for ordering the nodes
    in the tree, and the value is the data stored at that node.
    """

    def get_min(self):
        """
        Returns the minimum value node in the tree.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current

    def get_max(self):
        """
        Returns the maximum value node in the tree.
        """
        current = self
        while current.right is not None:
            current = current.right
        return current

    def get_inorder_successor(self):
        """
        Returns the inorder successor of a given node in the tree.
        """
        if self.right is not None:
            return self.right.get_min()

        successor = None
        ancestor = self
        while ancestor != self:
            if self.value < ancestor.value:
                successor = ancestor
                ancestor = ancestor.left
            else:
                ancestor = ancestor.right
        return successor

    def get_inorder_predecessor(self):
        """
        Returns the inorder predecessor of a given node in the tree.
        """
        if self.left is not None:
            return self.left.get_max()

        predecessor = None
        ancestor = self
        while ancestor != self:
            if self.value > ancestor.value:
                predecessor = ancestor
                ancestor = ancestor.right
            else:
                ancestor = ancestor.left
        return predecessor
