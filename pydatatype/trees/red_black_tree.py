"""
This module provides an implementation of a Red-Black Tree, a type of
self-balancing binary search tree.

Red-Black Trees are designed to provide O(log n) search, insertion, and
deletion performance while ensuring that the tree remains balanced.
They are used extensively in computer science for tasks such as
maintaining a sorted list of data.
"""

from .base_tree import Tree


class RedBlackTree(Tree):
    """
    A Red-Black Tree implementation.

    A Red-Black Tree is a type of self-balancing binary search tree. It
    maintains a strict ordering of its elements like a binary search tree,
    but additionally enforces two rules to keep the tree balanced: no red node
    has a red parent, and every path from the root to a leaf node contains the
    same number of black nodes.
    """
