"""
This module contains the AVLTreeNode class.
"""

from .node import Node


class AVLTreeNode(Node):
    """
    A node in an AVL tree.

    Attributes:
        value: The value held by the node.
        left: The node's left child.
        right: The node's right child.
        height: The node's height in the tree.
    """
