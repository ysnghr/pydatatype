import pytest
from pydatatype.trees import BinaryTree
from pydatatype.node import Node


class TestBinaryTree:
    def test_binary_tree_creation(self):
        new_tree = BinaryTree()
        assert new_tree.root is None
        assert new_tree.size == 0

    def test_binary_tree_creation_with_root(self):
        new_tree = BinaryTree(Node(1))
        assert new_tree.root.value == 1
        assert new_tree.get_height() == 1

    def test_binary_tree_creation_with_invalid_root(self):
        with pytest.raises(TypeError):
            BinaryTree(1)

    def test_binary_tree_get_height(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.get_height() == 2

    def test_binary_tree_get_height_with_no_root(self):
        new_tree = BinaryTree()
        assert new_tree.get_height() == 0

    def test_binary_tree_insert(self):
        new_tree = BinaryTree()
        new_tree.insert(Node(1))
        assert new_tree.root.value == 1
        assert new_tree.get_height() == 1

    def test_binary_tree_insert_with_existing_root(self):
        new_tree = BinaryTree(Node(1))
        new_tree.insert(Node(2))
        assert new_tree.root.value == 1
        assert new_tree.root.left.value == 2
        assert new_tree.get_height() == 2

    def test_binary_tree_merge(self):
        new_tree = BinaryTree(Node(1))
        new_tree.merge(BinaryTree(Node(2)))
        assert new_tree.root.value == 1
        assert new_tree.root.left.value == 2
        assert new_tree.get_height() == 2

    def test_binary_tree_merge_with_no_root(self):
        new_tree = BinaryTree()
        new_tree.merge(BinaryTree(Node(2)))
        assert new_tree.root.value == 2
        assert new_tree.get_height() == 1

    def test_binary_tree_merge_with_no_root_and_no_root(self):
        new_tree = BinaryTree()
        new_tree.merge(BinaryTree())
        assert new_tree.root is None
        assert new_tree.get_height() == 0

    def test_binary_tree_merge_with_invalid_tree(self):
        new_tree = BinaryTree()
        with pytest.raises(TypeError):
            new_tree.merge(1)

    def test_binary_tree_travel_in_order(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.in_order == [2, 1, 3]

    def test_binary_tree_travel_pre_order(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.pre_order == [1, 2, 3]

    def test_binary_tree_travel_post_order(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.post_order == [2, 3, 1]

    def test_binary_tree_travel_level_order(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.level_order == [1, 2, 3]

    def test_binary_tree_clone(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        cloned_tree = new_tree.clone()
        assert cloned_tree.root.value == 1
        assert cloned_tree.root.left.value == 2
        assert cloned_tree.root.right.value == 3
        assert cloned_tree.get_height() == 2

    def test_binary_tree_equals(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        cloned_tree = new_tree.clone()
        assert new_tree.root.value == cloned_tree.root.value
        assert new_tree.root.left.value == cloned_tree.root.left.value
        assert new_tree.root.right.value == cloned_tree.root.right.value

    def test_binary_tree_not_equals(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        cloned_tree = new_tree.clone()
        cloned_tree.root.value = 2
        assert new_tree != cloned_tree

    def test_binary_tree_search(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert new_tree.search(2)

    def test_binary_tree_not_exists(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        assert not new_tree.search(4)

    def test_binary_tree_delete_existing_node(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        new_tree.delete(2)
        assert new_tree.root.value == 1
        assert new_tree.root.right is None
        assert new_tree.root.left.value == 3
        assert new_tree.get_height() == 2

    def test_binary_tree_delete_non_existing_node(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        new_tree.delete(4)
        assert new_tree.root.value == 1
        assert new_tree.root.left.value == 2
        assert new_tree.root.right.value == 3
        assert new_tree.get_height() == 2

    def test_binary_tree_delete_root(self):
        new_tree = BinaryTree(Node(1, Node(2), Node(3)))
        new_tree.delete(1)
        assert new_tree.root.value == 3
        assert new_tree.root.left.value == 2
        assert new_tree.root.right is None
        assert new_tree.get_height() == 2

    def test_binary_tree_delete_root_with_no_children(self):
        new_tree = BinaryTree(Node(1))
        new_tree.delete(1)
        assert new_tree.root is None
        assert new_tree.get_height() == 0
