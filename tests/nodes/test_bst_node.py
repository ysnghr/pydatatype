from pydatatype.nodes import BSTreeNode as Node


class BSTreeNodeTest:
    def test_node_get_inorder_successor(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.get_inorder_successor().value == 3

    def test_node_get_inorder_successor_with_no_right(self):
        new_node = Node(1, Node(2), None)
        assert new_node.get_inorder_successor() is None

    def test_node_get_inorder_successor_with_no_children(self):
        new_node = Node(1)
        assert new_node.get_inorder_successor() is None

    def test_node_get_inorder_predecessor(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.get_inorder_predecessor().value == 2

    def test_node_get_inorder_predecessor_with_no_left(self):
        new_node = Node(1, None, Node(3))
        assert new_node.get_inorder_predecessor() is None

    def test_node_get_inorder_predecessor_with_no_children(self):
        new_node = Node(1)
        assert new_node.get_inorder_predecessor() is None

    def test_node_get_max(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.get_max().value == 3

    def test_node_get_min(self):
        new_node = Node(1, Node(2), Node(3))
        assert new_node.get_min().value == 2
