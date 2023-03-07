"""
This module provides an implementation of an AVL tree,
a self-balancing binary search tree.

AVL trees are designed to maintain a balance between the height of
the left and right subtrees of each node, which ensures that the tree
remains relatively balanced and that the search, insertion, and deletion
operations can be performed in O(log n) time.
"""
from .base_tree import Tree


class AVLTree(Tree):
    """
    A self-balancing binary search tree implementation using the AVL algorithm.

    An AVL tree is a binary search tree that maintains a balance between the
    height of the left and right subtrees of each node, ensuring that the
    height difference between the left and right subtrees is at most one.
    This balance ensures that the search, insertion, and deletion operations
    can be performed in O(log n) time.
    """
