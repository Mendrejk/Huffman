class Node:
    def __init__(self, symbol, amount):
        self.left = None
        self.right = None
        self.symbol = symbol
        self.amount = amount

    # def insert(self, symbol):
    #     if self.symbol:
    #         if symbol < self.symbol:
    #             if self.left is None:
    #                 self.left = Node(symbol)
    #             else:
    #                 self.left.insert(symbol)
    #         elif symbol > self.symbol:
    #             if self.right is None:
    #                 self.right = Node(symbol)
    #             else:
    #                 self.right.insert(symbol)
    #     else:
    #         self.symbol = symbol

    # def insert_tree(self, tree):
    #     # assuming symbol is
    #     if tree.symbol < self.symbol:
    #         if self.left is None:
    #             self.left = tree
    #         else:
    #             self.left.insert_tree(tree)
    #     elif tree.symbol > self.symbol:
    #         if self.right is None:
    #             self.right = tree
    #         else:
    #             self.right.insert_tree(tree)

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.symbol, self.amount)
        if self.right:
            self.right.print_tree()
