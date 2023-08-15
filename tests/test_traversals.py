from pydatatype.trees import BinaryTree
from pydatatype.utils.traversals import (
    PreOrderIterator,
    InOrderIterator,
    PostOrderIterator,
    LevelOrderIterator,
)


class TestPreOrderIterator:
    def test_preorder_iterator_from_tree(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in new_tree.preorder():
            result.append(node)
        expected_result = [1, 2, 4, 5, 3, 6, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]

    def test_preorder_iterator_from_tree_with_no_root(self):
        new_tree = BinaryTree()
        result = []
        for node in new_tree.preorder():
            result.append(node)
        assert result == []

    def test_preorder_iterator(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in PreOrderIterator(new_tree):
            result.append(node)
        expected_result = [1, 2, 4, 5, 3, 6, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]


class TestInOrderIterator:
    def test_inorder_iterator_from_tree(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in new_tree.inorder():
            result.append(node)
        expected_result = [4, 2, 5, 1, 6, 3, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]

    def test_inorder_iterator_from_tree_with_no_root(self):
        new_tree = BinaryTree()
        result = []
        for node in new_tree.inorder():
            result.append(node)
        assert result == []

    def test_inorder_iterator(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in InOrderIterator(new_tree):
            result.append(node)
        expected_result = [4, 2, 5, 1, 6, 3, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]


class TestPostOrderIterator:
    def test_postorder_iterator_from_tree(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in new_tree.postorder():
            result.append(node)
        expected_result = [4, 5, 2, 6, 7, 3, 1]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]

    def test_postorder_iterator_from_tree_with_no_root(self):
        new_tree = BinaryTree()
        result = []
        for node in new_tree.postorder():
            result.append(node)
        assert result == []

    def test_postorder_iterator(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in PostOrderIterator(new_tree):
            result.append(node)
        expected_result = [4, 5, 2, 6, 7, 3, 1]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]


class TestLevelOrderIterator:
    def test_levelorder_iterator_from_tree(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in new_tree.levelorder():
            result.append(node)
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]

    def test_levelorder_iterator_from_tree_with_no_root(self):
        new_tree = BinaryTree()
        result = []
        for node in new_tree.levelorder():
            result.append(node)
        assert result == []

    def test_levelorder_iterator(self):
        new_tree = BinaryTree()
        for value in range(1, 8):
            new_tree.insert(value)
        result = []
        for node in LevelOrderIterator(new_tree):
            result.append(node)
        expected_result = [1, 2, 3, 4, 5, 6, 7]
        for node in range(len(result)):
            assert result[node].value == expected_result[node]
