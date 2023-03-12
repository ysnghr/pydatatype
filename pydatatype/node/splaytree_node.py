"""
This module provides a SplayTreeNode class that can be used to build a splay tree.

A splay tree is a self-adjusting binary search tree that provides fast access to
recently accessed nodes. When a node is accessed, it is moved to the root of the tree
using a series of rotations called splaying. This makes the tree more balanced and
improves the performance of subsequent accesses to nearby nodes.

Classes:
- SplayTreeNode: A class that represents a node in a splay tree.
"""

from .node import Node


class SplayTreeNode(Node):
    """
    A class that represents a node in a splay tree.

    Each node has a key-value pair, where the key is used for ordering the nodes in the
    tree, and the value is the data stored at that node.
    """
