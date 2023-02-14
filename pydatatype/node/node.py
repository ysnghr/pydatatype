from collections import deque
from typing import Union


class Node:
    """Item in Tree Structured Data"""

    def __init__(
        self,
        value: int,
        left: Union["Node", None] = None,
        right: Union["Node", None] = None,
    ):
        if value is not None and not isinstance(value, int):
            raise TypeError("The argument 'value' must be of \
                            type 'int'")
        if left is not None and not isinstance(left, Node):
            raise TypeError("The argument 'left' must be of \
                            type 'Node' or 'None'")
        if right is not None and not isinstance(right, Node):
            raise TypeError("The argument 'right' must be of \
                            type 'Node' or 'None'")
        self.value = value
        self.left = left
        self.right = right

    def get_children(self):
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

    def insert_right(self, value):
        """
        Inserts a node to the right of the current node
        """
        if self.right is None:
            self.right = Node(value)
        else:
            node = Node(value)
            node.right = self.right
            self.right = node

    def insert_left(self, value):
        """
        Inserts a node to the left of the current node
        """
        if self.left is None:
            self.left = Node(value)
        else:
            node = Node(value)
            node.left = self.left
            self.left = node

    def delete_left(self):
        """
        Deletes the left node of the current node
        """
        if self.left is not None:
            self.left = None

    def delete_right(self):
        """
        Deletes the right node of the current node
        """
        if self.right is not None:
            self.right = None
