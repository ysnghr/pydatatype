from abc import ABC, abstractmethod, abstractproperty
from pydatatype.node import Node
from pydatatype.utils.traversals import (
    PreOrderIterator,
    InOrderIterator,
    PostOrderIterator,
    LevelOrderIterator,
)
from typing import Optional


class Tree(ABC):
    def __init__(self, root: Optional[Node] = None):
        if root is not None and not isinstance(root, Node):
            raise TypeError("The argument 'root' must be of type 'Node'")
        self.root = root
        self.size = 0

    @abstractproperty
    def right(self):
        pass

    @abstractproperty
    def left(self):
        pass

    def preorder(self):
        return PreOrderIterator(self)

    def inorder(self):
        return InOrderIterator(self)

    def postorder(self):
        return PostOrderIterator(self)

    def levelorder(self):
        return LevelOrderIterator(self)

    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def insert(self, node: Node):
        pass

    @abstractmethod
    def merge(self, tree: "Tree"):
        pass

    @abstractmethod
    def search(self, value):
        pass

    @abstractmethod
    def delete(self, value):
        pass

    @abstractmethod
    def delete_tree(self):
        pass

    @abstractmethod
    def clone(self):
        pass
