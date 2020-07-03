
def one_binary_function(key, string):
    string_ord = []
    binary_ord = []
    cipher_list = []
    final_list = []

    for c in string:
        string_ord.append(ord(c))

    for i in string_ord:
        binary_ord.append(bin(i))

    binary_key = bin(key)
    counter = 0

    for b in binary_ord:
        x = int(binary_ord[counter], 2)
        y = int(binary_key, 2)
        cipher_list.append(x ^ y)
        counter += 1

    for i in cipher_list:
        character = chr(i)
        final_list.append(character)

    return "".join(final_list)
