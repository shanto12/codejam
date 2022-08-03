class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root
        self.height = 1

    def pre_order(self, node="root"):
        if node == "root":
            node = self.root

        if node:
            print(f"{node.value}", end='')

            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node="root"):
        if node == "root":
            node = self.root

        if node:
            self.in_order(node.left)
            print(f"{node.value}", end='')
            self.in_order(node.right)

    def dfs(self, node="root"):
        if node == "root":
            node = self.root

        if node:
            self.dfs(node.right)
            print(f"{node.value}", end='')
            self.dfs(node.left)


counter = 1

Binary_Tree = Tree(Node("F"))
Binary_Tree.root.left = Node("B")
Binary_Tree.root.right = Node("G")
Binary_Tree.root.left.left = Node("A")
Binary_Tree.root.left.right = Node("D")
Binary_Tree.root.right.right = Node("I")
Binary_Tree.root.right.right.left = Node("H")
Binary_Tree.root.left.right.left = Node("C")
Binary_Tree.root.left.right.right = Node("E")

Binary_Tree.pre_order()
print()
Binary_Tree.in_order()
print()
Binary_Tree.dfs()

