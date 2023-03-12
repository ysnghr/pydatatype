"""
This module provides a Node class for use in tree data structures.
"""

from collections import deque
from typing import Union
from typing import TypeVar

T = TypeVar("T")


class Node:
    """A node in a tree data structure.

    A tree node consists of a value and references to its child nodes.
    If a node has no children, its child references will be None.

    Example Usage:
    ```
    node = Node(5)
    left_child = Node(3)
    right_child = Node(7)
    node.left = left_child
    node.right = right_child

    # or alternatively:
    node = Node(5, 3, 7)
    ```
    """

    def __init__(
        self,
        value: T,
        left: Union["Node", None] = None,
        right: Union["Node", None] = None,
    ):
        if left is not None and not isinstance(left, Node):
            raise TypeError(
                "The argument 'left' must be of \
                            type 'Node' or 'None'"
            )
        if right is not None and not isinstance(right, Node):
            raise TypeError(
                "The argument 'right' must be of \
                            type 'Node' or 'None'"
            )
        self.value = value
        self.left = left
        self.right = right

    @property
    def children(self):
        """
        Gets the children of the current node object
        """
        children = []
        if self.left:
            children.append(self.left)
        if self.right:
            children.append(self.right)
        return children

    def get_height(self):
        """
        Gets the height of the current tree object
        """
        # create an empty queue and enqueue the root node
        queue = deque()
        queue.append(self)

        height = 0

        # loop till queue is empty
        while queue:
            # calculate the total number of nodes at the current level
            size = len(queue)

            # process each node of the current level and enqueue their
            # non-empty left and right child
            while size > 0:
                front = queue.popleft()

                if front.left:
                    queue.append(front.left)

                if front.right:
                    queue.append(front.right)

                size = size - 1

            # increment height by 1 for each level
            height = height + 1

        return height
