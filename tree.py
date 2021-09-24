class Tree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, self.root)
            return

        self._insert(self.root, value)

    def _insert(self, current_node, value):

        if value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value, current_node)
                return
            else:
                return self._insert(current_node.right, value)

        else:
            if current_node.left is None:
                current_node.left = Node(value, current_node)
                return
            else:
                return self._insert(current_node.left, value)

    def delete(self, instance):
        pass

    def max_value(self):
        pass

    def min_value(self):
        pass

    def search(self, value: int):
        found_node = self._search(self.root, value)
        if found_node is None:
            return False
        return True

    def _search(self, node_to_check, value):
        if (node_to_check is None) or (node_to_check.value == value):
            return node_to_check

        if value > node_to_check.value:
            return self._search(node_to_check.right, value)
        else:
            return self._search(node_to_check.left, value)


class Node:
    def __init__(self, value, parent):
        self.right = None
        self.left = None
        self.parent = parent
        self.value = value


if __name__ == '__main__':
    tree = Tree()

    tree.insert(15)
    tree.insert(6)
    tree.insert(7)
    tree.insert(4)
    tree.insert(5)
    tree.insert(23)
    tree.insert(71)
    tree.insert(50)
