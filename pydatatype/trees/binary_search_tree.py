"""
This module provides an implementation of a binary search tree, a type of
binary tree that maintains a strict ordering of its elements.

Binary search trees are designed for fast searching and retrieval, and are
used extensively in computer science for tasks such as maintaining a sorted
list of data.
"""

from .base_tree import Tree


class BinarySearchTree(Tree):
    """
    A binary search tree implementation.

    A binary search tree is a type of binary tree that maintains a strict
    ordering of its elements: each node has a value that is greater than all
    the values in its left subtree, and less than all  the values in its right
    subtree. This property allows binary search trees to be used for
    efficient searching and retrieval of data.

    """
