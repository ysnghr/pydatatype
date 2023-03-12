"""
This module provides an implementation of a binary search tree, a type of
binary tree that maintains a strict ordering of its elements.

Binary search trees are designed for fast searching and retrieval, and are
used extensively in computer science for tasks such as maintaining a sorted
list of data.
"""

from .base_tree import Tree
from ..nodes import BSTreeNode as Node


class BinarySearchTree(Tree):
    """
    A binary search tree implementation.

    A binary search tree is a type of binary tree that maintains a strict
    ordering of its elements: each node has a value that is greater than all
    the values in its left subtree, and less than all  the values in its right
    subtree. This property allows binary search trees to be used for
    efficient searching and retrieval of data.

    """

    def insert(self, key):
        """
        Insert a node into the tree.

        Args:
            node: The node to insert into the tree.

        """
        # Create a new Node containing
        # the new element
        newnode = Node(key)

        # Pointer to start traversing from root
        # and traverses downward path to search
        # where the new node to be inserted
        x = self.root

        # Pointer y maintains the trailing
        # pointer of x
        y = None

        while x is not None:
            y = x
            if key < x.value:
                x = x.left
            else:
                x = x.right

        # If the root is None i.e the tree is
        # empty. The new node is the root node
        if y is None:
            self.root = newnode

        # If the new key is less than the leaf node key
        # Assign the new node to be its left child
        elif key < y.value:
            y.left = newnode

        # else assign the new node its
        # right child
        else:
            y.right = newnode

        # Returns the pointer where the
        # new node is inserted
        return y

    def search(self, key):
        """
        Search for a node in the tree.

        Args:
            key: The key to search for.

        Returns:
            The node with the given key, or None if the key is not found.

        """
        temp = self.root
        while temp is not None:
            if temp.val == key:
                return temp
            elif temp.val > key:
                temp = temp.left
            else:
                temp = temp.right
        return None

    def get_min_value_node(self):
        """
        Get the node with the minimum value in the tree.

        Args:
            node: The node to start searching from.

        Returns:
            The node with the minimum value in the tree.

        """
        if self.root is None:
            return None
        return self.root.get_min_value_node()

    def get_max_value_node(self):
        """
        Get the node with the maximum value in the tree.

        Args:
            node: The node to start searching from.

        Returns:
            The node with the maximum value in the tree.

        """
        if self.root is None:
            return None
        return self.root.get_max_value_node()

    def delete(self, key, inorder_method="successor"):
        """
        Delete a node from the tree.

        Args:
            key: The key of the node to delete.
            inorder_method: The method to use to find the inorder successor or predecessor
                of a node. Must be either "successor" or "predecessor".
        """
        parent = None
        curr = self.root
        while curr and curr.value != key:
            parent = curr
            if key < curr.value:
                curr = curr.left
            else:
                curr = curr.right

        if not curr:
            # Node with key not found
            return

        if not curr.left or not curr.right:
            # If curr has no children or only one child, set its parent's pointer
            # to its child (or None if curr has no children)
            if not curr.left:
                child = curr.right
            else:
                child = curr.left
            if not parent:
                self.root = child
            elif parent.left == curr:
                parent.left = child
            else:
                parent.right = child
        else:
            # If curr has two children, find its inorder successor or predecessor
            # and replace curr's value with that node's value
            if inorder_method == "successor":
                succ = curr.right
                while succ.left:
                    succ = succ.left
                curr.value = succ.value
                self.delete(succ.value, inorder_method="successor")
            elif inorder_method == "predecessor":
                pred = curr.left
                while pred.right:
                    pred = pred.right
                curr.value = pred.value
                self.delete(pred.value, inorder_method="predecessor")
            else:
                raise ValueError("Invalid inorder method")

    def create_tree(self, elements, start, end):
        """
        Create a tree from a list of elements.

        Args:
            elements: A list of elements to insert into the tree.

        """
        elements.sort()
        if start > end:
            return

        mid = (start + end) // 2
        self.insert(elements[mid])

        self._construct_bst(elements, new_tree, start, mid - 1)
        self._construct_bst(elements, new_tree, mid + 1, end)

    def merge(self, tree2):
        """
        Merges the given binary search tree into this tree in O(n + m) time and O(1) space,
        where n and m are the number of nodes in the two trees, respectively.
        """
        # If either tree is empty, return the other tree.
        if self.root is None:
            self.root = tree2.root
            return
        elif tree2.root is None:
            return

        # Traverse both trees in parallel using two iterators.
        node1, node2 = self.root, tree2.root
        parent = None
        while node1 is not None and node2 is not None:
            if node1.value <= node2.value:
                parent, node1 = node1, node1.right
            else:
                if parent is None:
                    # If the new root needs to change, make it the smaller node.
                    self.root = node2
                else:
                    # Otherwise, insert the smaller node as the right or left child of the parent.
                    if parent.value <= node2.value:
                        parent.right = node2
                    else:
                        parent.left = node2
                # Advance the iterator for the second tree.
                node2, node1 = node2.right, node1

        # If one of the iterators has reached the end of its tree, attach the rest of the other tree to the merged tree.
        if node2 is not None:
            if parent is None:
                # If the new root needs to change, make it the remaining node in the second tree.
                self.root = node2
            else:
                # Otherwise, attach the rest of the second tree to the last parent node.
                parent.right = node2
        elif node1 is not None:
            # No need to do anything if the first tree is not exhausted.
            pass

    def clone(self):
        pass

    def delete_tree(self):
        pass

    def _construct_bst(self, sorted_list, new_tree, start, end):
        if start > end:
            return

        mid = (start + end) // 2
        new_tree.insert(sorted_list[mid])

        self._construct_bst(sorted_list, new_tree, start, mid - 1)
        self._construct_bst(sorted_list, new_tree, mid + 1, end)

    @staticmethod
    def build(elements):
        # Create a stack to keep track of ranges
        stack = [(0, len(elements) - 1)]

        # Create a new node for the root
        new_tree = BinarySearchTree(Node(None))

        # Create a stack to keep track of nodes and their ranges
        node_stack = [(new_tree.root, 0, len(elements) - 1)]

        # Process the stack until all ranges have been processed
        while stack:
            # Pop the top range from the stack
            start, end = stack.pop()

            # Compute the middle index
            mid = (start + end) // 2
            # Get the node and range from the node stack
            node, node_start, node_end = node_stack.pop()

            # Set the value of the node to the middle element
            node.value = elements[mid]

            # Push the left range onto the stack and create a new node
            if start <= mid - 1:
                node.left = Node(None)
                stack.append((start, mid - 1))
                node_stack.append((node.left, start, mid - 1))

            # Push the right range onto the stack and create a new node
            if mid + 1 <= end:
                node.right = Node(None)
                stack.append((mid + 1, end))
                node_stack.append((node.right, mid + 1, end))

        return new_tree
