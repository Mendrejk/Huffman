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


def main():
    test_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin nibh augue, suscipit a, scelerisque sed, lacinia in, mi."
    frequency_list = create_frequency_list(test_string)
    print(frequency_list)

    root1 = Node(3)
    root1.insert(6)
    root2 = Node(5)
    root2.insert(4)
    root1.insert_tree(root2)
    root1.print_tree()


if __name__ == "__main__":
    main()
