from node import Node


def read_file(file):
    with open(file, 'r', encoding="utf-8-sig") as input_file:
        data = input_file.read()
    return data


def write_to_file(file, to_write):
    with open(file, 'w', encoding='utf-8-sig') as output_file:
        output_file.write(to_write)


def binary_to_file(input_text, output_file, bin_dictionary):
    with open(output_file, 'w', encoding="utf-8-sig") as output_file:
        for i in input_text:
            output_file.write(bin_dictionary[i])


def binary_to_char(binary, char_dictionary):
    big_t = ''
    sad = False
    while binary:
        temp = ''
        for i in binary:
            temp += i
            # print(big_t)
            if temp in char_dictionary:
                big_t += char_dictionary[temp]
                binary = binary[len(temp)-1:]
                temp = ''
                # print(len(binary))
            elif len(binary) - len(temp) == 0:
                print('gg')
                sad = True
                break
        if sad:
            break
    return big_t


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
        if freq_list:
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
    input_file = "Mr_T.txt"
    output_file = "Binary_T.txt"
    input_string = read_file(input_file)
    frequency_list = create_frequency_list(input_string)

    for i in range(len(frequency_list)):
        to_node = frequency_list[i]
        frequency_list[i] = Node(to_node[0], to_node[1])

    tree = generate_huffman_binary_tree(frequency_list)
    tree.assign_binary()
    bin_dictionary = tree.node_to_bin_dict({})
    print(bin_dictionary)

    binary_to_file(input_string, output_file, bin_dictionary)

    # reverse the coding:
    to_char_file = output_file
    to_char = read_file(to_char_file)
    char_output_file = "Mr_T_or_is_it.txt"
    char_dictionary = tree.node_to_char_dict({})
    new_t = binary_to_char(to_char, char_dictionary)
    write_to_file(char_output_file, new_t)


if __name__ == "__main__":
    main()
