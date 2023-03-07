import pytest
from pydatatype.node import Node


class TestNode:
    def test_node_creation(self):
        new_node = Node(1)
        assert new_node.value == 1
        assert new_node.right is None
        assert new_node.left is None

    def test_node_creation_with_left(self):
        new_node = Node(1, Node(2))
        assert new_node.value == 1
        assert new_node.right is None
        assert new_node.left.value == 2

    def test_node_creation_with_right(self):
        new_node = Node(1, None, Node(2))
        assert new_node.value == 1
        assert new_node.right.value == 2
        assert new_node.left is None

    def test_node_creation_with_both(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.value == 1
        assert new_node.right.value == 3
        assert new_node.left.value == 2

    def test_node_creation_with_invalid_left(self):
        with pytest.raises(TypeError):
            Node(1, 2)

    def test_node_creation_with_invalid_right(self):
        with pytest.raises(TypeError):
            Node(1, None, 2)

    def test_node_creation_with_invalid_both(self):
        with pytest.raises(TypeError):
            Node(1, 2, 3)

    def test_node_creation_with_invalid_value_and_left(self):
        with pytest.raises(TypeError):
            Node("1", 2)

    def test_node_creation_with_invalid_value_and_right(self):
        with pytest.raises(TypeError):
            Node("1", None, 2)

    def test_node_creation_with_invalid_value_and_both(self):
        with pytest.raises(TypeError):
            Node("1", 2, 3)

    def test_node_get_children(self):
        second_node = Node(2)
        third_node = Node(3)
        new_node = Node(1, second_node, third_node)
        assert new_node.children == [second_node, third_node]

    def test_node_get_children_with_no_children(self):
        new_node = Node(1)
        assert new_node.children == []

    def test_node_get_height(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.get_height() == 2

    def test_node_get_height_with_no_children(self):
        new_node = Node(1)
        assert new_node.get_height() == 1

    def test_node_delete_left(self):
        new_node = Node(1, Node(2), Node(3))
        new_node.delete_left()
        assert new_node.left is None

    def test_node_delete_left_with_no_left(self):
        new_node = Node(1, None, Node(3))
        new_node.delete_left()
        assert new_node.left is None

    def test_node_delete_right(self):
        new_node = Node(1, Node(2), Node(3))
        new_node.delete_right()
        assert new_node.right is None

    def test_node_delete_right_with_no_right(self):
        new_node = Node(1, Node(2), None)
        new_node.delete_right()
        assert new_node.right is None

    def test_node_insert_left(self):
        new_node = Node(1, Node(2), Node(3))
        new_node.insert_left(Node(4))
        assert new_node.left.value == 4
        assert new_node.left.left.value == 2

    def test_node_insert_left_with_no_left(self):
        new_node = Node(1, None, Node(3))
        new_node.insert_left(Node(4))
        assert new_node.left.value == 4
        assert new_node.left.left is None

    def test_node_insert_right(self):
        new_node = Node(1, Node(2), Node(3))
        new_node.insert_right(Node(4))
        assert new_node.right.value == 4
        assert new_node.right.right.value == 3

    def test_node_insert_right_with_no_right(self):
        new_node = Node(1, Node(2), None)
        new_node.insert_right(Node(4))
        assert new_node.right.value == 4
        assert new_node.right.right is None
