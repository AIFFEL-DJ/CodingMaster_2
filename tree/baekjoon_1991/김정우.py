class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinaryTree(Node):
    def __init__(self):
        self.root = None
        self.N = 0

    def insert(self, input_list):
        self.root = self._insert_value(self.root, input_list)
        return self.root is not None

    def _insert_value(self, node, input_list):
        if node is None:
            node = Node(input_list[0])
            node.left = Node(input_list[1] if input_list[1] != '.' else None)
            node.right = Node(input_list[2] if input_list[2] != '.' else None)
        elif node.data == input_list[0]:
            node.left = Node(input_list[1] if input_list[1] != '.' else None)
            node.right = Node(input_list[2] if input_list[2] != '.' else None)
        else:
            if node.left is not None:
                self._insert_value(node.left, input_list)
            if node.right is not None:
                self._insert_value(node.right, input_list)
        return node

    # 전위순회
    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                print(root.data if root.data is not None else "", end='')
                _pre_order_traversal(root.left)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    # 중위순회
    def in_order_traversal(self):
        def _in_order_traversal(root):
            if root is None:
                pass
            else:
                _in_order_traversal(root.left)
                print(root.data if root.data is not None else "", end='')
                _in_order_traversal(root.right)
        _in_order_traversal(self.root)

    # 후위순회
    def post_order_traversal(self):
        def _post_order_traversal(root):
            if root is None:
                pass
            else:
                _post_order_traversal(root.left)
                _post_order_traversal(root.right)
                print(root.data if root.data is not None else "", end='')
        _post_order_traversal(self.root)

bt = BinaryTree()
bt.N = int(input())
for i in range(bt.N):
    bt.insert(list(input().split()))
bt.pre_order_traversal()
print()
bt.in_order_traversal()
print()
bt.post_order_traversal()
print()
