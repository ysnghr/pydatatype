from abc import ABC, abstractmethod, abstractproperty
from pydatatype.node import Node
from typing import Optional


class Tree(ABC):
    def __init__(self, root: Optional[Node] = None):
        if root is not None and not isinstance(root, Node):
            raise TypeError("The argument 'root' must be of type 'Node'")
        self.root = root
        self.size = 0

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
    def pre_order(self):
        pass

    @abstractproperty
    def in_order(self):
        pass

    @abstractproperty
    def post_order(self):
        pass

    @abstractproperty
    def level_order(self):
        pass

    @abstractmethod
    def delete_tree(self):
        pass

    @abstractmethod
    def clone(self):
        pass
