"""
This module provides an implementation of a splay tree, a self-adjusting
binary search tree with amortized O(log n) operations.
"""

from .base_tree import Tree


class SplayTree(Tree):
    """
    A self-adjusting binary search tree with amortized O(log n) operations.
    """
