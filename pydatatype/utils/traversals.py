from collections import deque


class PreOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.stack.append(root)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stack:
            raise StopIteration
        node = self.stack.pop()
        if node.right:
            self.stack.append(node.right)
        if node.left:
            self.stack.append(node.left)
        return node


class PostOrderIterator:
    def __init__(self, root):
        self.stack = [(root, False)]

    def __iter__(self):
        return self

    def __next__(self):
        while self.stack:
            node, visited = self.stack.pop()
            if visited:
                return node
            else:
                self.stack.append((node, True))
                if node.right:
                    self.stack.append((node.right, False))
                if node.left:
                    self.stack.append((node.left, False))
        raise StopIteration


class InOrderIterator:
    def __init__(self, root):
        self.stack = []
        self.current = root

    def __iter__(self):
        return self

    def __next__(self):
        while self.current is not None:
            self.stack.append(self.current)
            self.current = self.current.left

        if len(self.stack) > 0:
            self.current = self.stack.pop()
            node = self.current
            self.current = self.current.right
            return node
        else:
            raise StopIteration


class LevelOrderIterator:
    def __init__(self, root):
        self.queue = deque()
        self.queue.append(root)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.queue:
            raise StopIteration
        node = self.queue.popleft()
        if node.left:
            self.queue.append(node.left)
        if node.right:
            self.queue.append(node.right)
        return node
