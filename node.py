class Node:
    def __init__(self, symbol, amount):
        self.left = None
        self.right = None
        self.symbol = symbol
        self.amount = amount
    binary = None

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.symbol, self.amount, self.binary)
        if self.right:
            self.right.print_tree()

    @staticmethod
    def assign_binary(node):
        if not node.binary:
            node.binary = ''
        if node.left:
            node.left.binary = node.binary + '0'
            Node.assign_binary(node.left)
        if node.right:
            node.right.binary = node.binary + '1'
            Node.assign_binary(node.right)
        return 0
