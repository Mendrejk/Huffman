class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def insert_tree(self, tree):
        # assuming data is
        if tree.data < self.data:
            if self.left is None:
                self.left = tree
            else:
                self.left.insert_tree(tree)
        elif tree.data > self.data:
            if self.right is None:
                self.right = tree
            else:
                self.right.insert_tree(tree)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()
