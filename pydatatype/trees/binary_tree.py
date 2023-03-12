"""
This module provides an implementation of a binary tree, a simple tree data
structure where each node has at most two children.

Binary trees are designed for fast searching and traversal, and can be used
to implement more complex data structures like binary search trees and heaps.
"""

import copy
from collections import deque
from ..node import BinaryTreeNode as Node
from .base_tree import Tree


class BinaryTree(Tree):
    """
    A simple binary tree implementation.

    A binary tree is a tree data structure where each node has at most two
    children, referred to as the left and right children. Binary trees can
    be used to implement more complex data structures like binary search
    trees and heaps, and are designed for fast searching and traversal.
    """

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            levels = [self.root]

            # Do level order traversal until we find
            # an empty place.
            while len(levels) > 0:
                temp = levels[0]
                levels.pop(0)
                if not temp.left:
                    temp.left = Node(value)
                    break
                levels.append(temp.left)
                if not temp.right:
                    temp.right = Node(value)
                    break
                levels.append(temp.right)

    def delete_tree(self):
        self.root = None

    def merge(self, tree: "BinaryTree"):
        if tree is None or not isinstance(tree, BinaryTree):
            raise TypeError("The argument 'tree' must be of type 'BinaryTree'")
        if self.root is not None:
            self._merge(self.root, tree.root)
        else:
            self.root = tree.root

    def _merge(self, first_node, second_node):
        if second_node is not None:
            self._merge(first_node, second_node.left)
            self._merge(first_node, second_node.right)
            self.insert(second_node.value)

    def clone(self):
        return copy.deepcopy(self)

    def search(self, value):
        stack = deque()
        stack.append(self.root)
        while stack:
            curr = stack.pop()
            if curr.value == value:
                return True
            if curr.right is not None:
                stack.append(curr.right)
            if curr.left is not None:
                stack.append(curr.left)
        return False

    def delete(self, value):
        if self.root is None:
            return
        if self.root.left is None and self.root.right is None:
            if self.root.value == value:
                self.root = None
            return

        key_node = None
        temp = None
        last = None
        stack = []
        stack.append(self.root)
        # Do level order traversal to find deepest
        # node(temp), node to be deleted (key_node)
        # and parent of deepest node(last)
        while stack:
            temp = stack.pop(0)

            if temp.value == value:
                key_node = temp
            if temp.left:
                last = temp  # storing the parent node
                stack.append(temp.left)

            if temp.right:
                last = temp  # storing the parent node
                stack.append(temp.right)

        if key_node is not None:
            key_node.value = (
                temp.value
            )  # replacing key_node's data to deepest node's data
            if last.right == temp:
                last.right = None
            else:
                last.left = None

        return
