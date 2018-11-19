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


def generate_huffman_binary_tree(list):
    if len(list) > 1:
        a, b = list[0], list[1]
        temp_symbol = a.symbol + b.symbol
        temp_amount = a.count + b.count
        temp = Node(temp_symbol, temp_amount)
        # removes a and b from list:
        a = a[2:]
        if len(list) > 0:
            for i, node in list:
                if temp.amount < node.amount:
                    list.insert(temp, i)
                    break


def main():
    test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi."
    frequency_list = create_frequency_list(test_string)
    print(frequency_list)

    for i in range(len(frequency_list)):
        to_node = frequency_list[i]
        frequency_list[i] = Node(to_node[0], to_node[1])


if __name__ == "__main__":
    main()
