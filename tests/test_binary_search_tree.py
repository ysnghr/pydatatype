from pydatatype.trees import BinarySearchTree
from pydatatype.node import Node


class TestBinarySearchTree:
    def test_binary_search_tree_creation(self):
        new_tree = BinarySearchTree()
        assert new_tree.root is None
        assert new_tree.size == 0

    def test_binary_search_tree_creation_with_root(self):
        new_tree = BinarySearchTree(Node(1))
        assert new_tree.root.value == 1
        assert new_tree.get_height() == 1

    def test_binary_search_tree_insert(self):
        new_tree = BinarySearchTree()
        new_tree.insert(1)
        assert new_tree.root.value == 1
        assert new_tree.get_height() == 1

    def test_binary_search_tree_insert_with_existing_root(self):
        new_tree = BinarySearchTree(Node(1))
        new_tree.insert(2)
        assert new_tree.root.value == 1
        assert new_tree.root.right.value == 2
        assert new_tree.get_height() == 2

    def test_binary_search_tree_insert_with_existing_root_and_left(self):
        new_tree = BinarySearchTree(Node(1, Node(2)))
        new_tree.insert(3)
        assert new_tree.root.value == 1
        assert new_tree.root.right.value == 3
        assert new_tree.get_height() == 2

    def test_binary_search_tree_insert_with_existing_root_and_right(self):
        new_tree = BinarySearchTree(Node(1, None, Node(2)))
        new_tree.insert(3)
        assert new_tree.root.value == 1
        assert new_tree.root.right.value == 2
        assert new_tree.root.right.right.value == 3
        assert new_tree.get_height() == 3

    def test_binary_search_tree_merge(self):
        new_tree = BinarySearchTree(Node(1))
        new_tree.merge(BinarySearchTree(Node(2)))
        assert new_tree.root.value == 1
        assert new_tree.root.right.value == 2
        assert new_tree.get_height() == 2

    def test_binary_search_tree_merge_with_no_root(self):
        new_tree = BinarySearchTree()
        new_tree.merge(BinarySearchTree(Node(2)))
        assert new_tree.root.value == 2
        assert new_tree.get_height() == 1

    def test_binary_search_tree_merge_with_no_root_and_no_root(self):
        new_tree = BinarySearchTree()
        new_tree.merge(BinarySearchTree())
        assert new_tree.root is None
        assert new_tree.get_height() == 0

    def test_binary_search_tree_delete(self):
        new_tree = BinarySearchTree(Node(50, Node(5), Node(55)))
        new_tree.delete(5)
        assert new_tree.root.value == 50
        assert new_tree.root.right.value == 55
        assert new_tree.root.left is None
        assert new_tree.get_height() == 2

    def test_binary_search_tree_delete_with_no_root(self):
        new_tree = BinarySearchTree()
        new_tree.delete(2)
        assert new_tree.root is None
        assert new_tree.get_height() == 0

    def test_binary_search_tree_build(self):
        new_tree = BinarySearchTree.build([1, 2, 3])
        assert new_tree.root.value == 2
        assert new_tree.root.right.value == 3
        assert new_tree.root.left.value == 1
        assert new_tree.get_height() == 2
