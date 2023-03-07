"""
This module provides an implementation of a B-Tree, a self-balancing tree
with variable numbers of keys per node.

B-Trees are designed to maintain a balance between the height of the tree
and the number of keys per node, ensuring that the tree remains relatively
balanced and that the search, insertion, and deletion operations can be
performed in O(log n) time.
"""
from .base_tree import Tree


class BTree(Tree):
    """
    A self-balancing tree implementation using the B-Tree algorithm.

    A B-Tree is a tree data structure with variable numbers of keys per node,
    designed to maintain a balance between the height of the tree and the
    number of keys per node, ensuring that the tree remains relatively
    balanced and that the search, insertion, and deletion operations
    can be performed in O(log n) time.
    """
