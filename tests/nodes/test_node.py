import pytest
from pydatatype.nodes import Node


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
