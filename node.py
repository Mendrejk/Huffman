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

    def assign_binary(self):
        if not self.binary:
            self.binary = ''
        if self.left:
            self.left.binary = self.binary + '0'
            self.left.assign_binary()
        if self.right:
            self.right.binary = self.binary + '1'
            self.right.assign_binary()
        return 0

    def node_to_bin_dict(self, dictionary):
        if self.left:
            self.left.node_to_bin_dict(dictionary)
            # if len(self.left.symbol) == 1:
            #    dictionary[self.left.symbol] = self.left.binary
        if len(self.symbol) == 1:
            dictionary[self.symbol] = self.binary
        if self.right:
            if len(self.right.symbol) == 1:
                dictionary[self.right.symbol] = self.right.binary
        return dictionary
