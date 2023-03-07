from .base_tree import Tree
from pydatatype.node import Node
from collections import deque
import copy


class BinaryTree(Tree):
    @property
    def right(self):
        return self.root.right

    @property
    def left(self):
        return self.root.left

    def insert(self, node: Node):
        if self.root is None:
            self.root = node
        else:
            levels = [self.root]

            # Do level order traversal until we find
            # an empty place.
            while len(levels):
                temp = levels[0]
                levels.pop(0)
                if not temp.left:
                    temp.left = node
                    break
                else:
                    levels.append(temp.left)
                if not temp.right:
                    temp.right = node
                    break
                else:
                    levels.append(temp.right)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self.root.get_height()

    def delete_tree(self):
        self.root = None

    def merge(self, tree: "BinaryTree"):
        if tree is None or not isinstance(tree, BinaryTree):
            raise TypeError("The argument 'tree' must be of type 'BinaryTree'")
        if self.root is not None:
            self._merge(self.root, tree.root)
        else:
            self.root = tree.root

    def _merge(self, node, tree):
        if tree is not None:
            self._merge(node, tree.left)
            self._merge(node, tree.right)
            self.insert(Node(tree.value))

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
            else:
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
