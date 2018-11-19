from node import Node


def create_frequency_list(string):
    frequency_dict = {}
    for i in string:
        if i in frequency_dict:
            frequency_dict[i] += 1
        else:
            frequency_dict[i] = 1

    # creates a sorted list of tuples consisting of symbols and number of their occurences
    sorted_keys = sorted(frequency_dict, key=frequency_dict.get)
    frequency_list = []
    for key in sorted_keys:
        frequency_list.append((key, frequency_dict[key]))
    return frequency_list


def generate_huffman_binary_tree(freq_list):
    while len(freq_list) > 1:
        a, b = freq_list[0], freq_list[1]
        temp_symbol = a.symbol + b.symbol
        temp_amount = a.amount + b.amount
        temp = Node(temp_symbol, temp_amount)
        temp.left, temp.right = a, b
        # removes a and b from freq_list:
        freq_list = freq_list[2:]
        if len(freq_list) > 0:
            inserted = False
            for i, node in enumerate(freq_list):
                if temp.amount <= node.amount:
                    freq_list.insert(i, temp)
                    inserted = True
                    break
            if not inserted:
                freq_list.append(temp)
    return temp


def main():
    test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi."
    frequency_list = create_frequency_list(test_string)

    for i in range(len(frequency_list)):
        to_node = frequency_list[i]
        frequency_list[i] = Node(to_node[0], to_node[1])

    tree = generate_huffman_binary_tree(frequency_list)
    print(tree.symbol, tree.amount)
    Node.assign_binary(tree)
    tree.print_tree()


if __name__ == "__main__":
    main()
