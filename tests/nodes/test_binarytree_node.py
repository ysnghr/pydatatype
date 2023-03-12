from pydatatype.nodes import BinaryTreeNode as Node


class BinaryTreeNodeTest:
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
