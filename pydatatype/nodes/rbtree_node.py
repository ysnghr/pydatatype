"""
This module provides a Red-Black tree node implementation for use in a Red-Black
tree data structure.

A Red-Black tree is a type of self-balancing binary search tree that can be used
to store and retrieve data efficiently. It is commonly used in computer science
applications where efficient search and insertion of data is required.

This module defines the RedBlackTreeNode class, which represents a single node in a
Red-Black tree. Each node can hold a single key-value pair and has a color
(either red or black) that determines the balance of the tree.

"""

from .node import Node


class RBTreeNode(Node):
    """
    A Red-Black tree node class representing a single node in a Red-Black tree data structure.

    Each node can hold a single key-value pair and has a color (either red or black)
    that determines the balance of the tree.
    """
