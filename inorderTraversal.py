class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)

root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)


print("Inorder Traversal: ")
inorder(root)
