"""
This module provides a BinaryTreeNode class that can be used to build a binary tree.

A binary tree is a tree data structure where each node has at most two children. This
property makes binary trees useful for a variety of applications, such as searching,
sorting, and expression parsing.

Classes:
- BinaryTreeNode: A class that represents a node in a binary tree.
"""

from .node import Node


class BinaryTreeNode(Node):
    """
    A class that represents a node in a binary tree.

    Each node has a key-value pair, where the key is used for ordering the nodes in the
    tree, and the value is the data stored at that node.
    """

    def insert_right(self, new_node):
        """
        Inserts a node to the right of the current node
        """
        if self.right is None:
            self.right = new_node
        else:
            node = new_node
            node.right = self.right
            self.right = node

    def insert_left(self, new_node):
        """
        Inserts a node to the left of the current node
        """
        if self.left is None:
            self.left = new_node
        else:
            node = new_node
            node.left = self.left
            self.left = node

    def delete_left(self):
        """
        Deletes the left node of the current node
        """
        if self.left is not None:
            self.left = None

    def delete_right(self):
        """
        Deletes the right node of the current node
        """
        if self.right is not None:
            self.right = None
