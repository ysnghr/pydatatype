"""
Module for tree traversal algorithms.
"""

from collections import deque


class PreOrderIterator:
    """
    Iterator for performing pre-order traversal on a tree.

    Pre-order traversal visits the root node, followed by
    the left subtree, and then the right subtree. This iterator supports both
    binary and n-ary trees.

    Example usage:
    ```
    # create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    # create an iterator and traverse the tree
    iterator = PreOrderIterator(root)
    for node in iterator:
        print(node)
    ```
    """

    def __init__(self, tree):
        """
        Initializes the PreOrderIterator.

        Parameters:
        - tree: Tree data structure.
        """
        self.stack = []
        if tree.root is not None:
            self.stack.append(tree.root)

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next node in the pre-order traversal.

        Raises StopIteration if there are no more nodes to traverse.
        """
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
        return node


class PostOrderIterator:
    """
    Iterator for performing post-order traversal on a tree.

    Post-order traversal visits the left subtree, followed by
    the right subtree, and then the root node. This iterator
    supports both binary and n-ary trees.

    Example usage:
    ```
    # create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    # create an iterator and traverse the tree
    iterator = PostOrderIterator(root)
    for node in iterator:
        print(node)
    ```
    """

    def __init__(self, tree):
        """
        Initializes the PostOrderIterator.

        Parameters:
        - tree: Tree data structure.
        """
        self.stack = []
        if tree.root is not None:
            self.stack.append((tree.root, False))

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next node in the post-order traversal.

        Raises StopIteration if there are no more nodes to traverse.
        """
        while self.stack:
            node, visited = self.stack.pop()
            if visited:
                return node
            self.stack.append((node, True))
            if node.right:
                self.stack.append((node.right, False))
            if node.left:
                self.stack.append((node.left, False))
        raise StopIteration


class InOrderIterator:
    """
    Iterator for performing in-order traversal on a binary tree.

    In-order traversal visits the left subtree, followed by the
    root node, and then the right subtree.

    Example usage:
    ```
    # create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    # create an iterator and traverse the tree
    iterator = InOrderIterator(root)
    for node in iterator:
        print(node)
    ```
    """

    def __init__(self, tree):
        self.stack = []
        self.current = tree.root

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next node in the in-order traversal.

        Raises StopIteration if there are no more nodes to traverse.
        """
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left

        if len(self.stack) > 0:
            self.current = self.stack.pop()
            node = self.current
            self.current = self.current.right
            return node
        raise StopIteration


class LevelOrderIterator:
    """
    Iterator for performing level-order traversal on a tree.

    Level-order traversal visits the nodes in each level of
    the tree, starting from the root level and moving down.This
    iterator supports both binary and n-ary trees.

    Example usage:
    ```
    # create a binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)

    # create an iterator and traverse the tree
    iterator = LevelOrderIterator(root)
    for node in iterator:
        print(node)
    ```
    """

    def __init__(self, tree):
        self.queue = deque()
        if tree.root is not None:
            self.queue.append(tree.root)

    def __iter__(self):
        """
        Returns the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Returns the next node in the level-order traversal.

        Raises StopIteration if there are no more nodes to traverse.
        """
        if not self.queue:
            raise StopIteration
        node = self.queue.popleft()
        if node.left:
            self.queue.append(node.left)
        if node.right:
            self.queue.append(node.right)
        return node
