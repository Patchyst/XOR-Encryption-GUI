def one_binary_function(key, string):
    # padding the String
    string_ord = []
    binary_ord = []
    for c in string:
        string_ord.append(ord(c))
    for i in string_ord:
        binary_ord.append(bin(i))
    # The message is now padded under the binary_ord
    # Next we will pad the key under as binary number
    binary_key = bin(key)
    # The key is now stored under the binary_key var
    # Next run the padded key and message variable throught he XOR stream Cipher
    cipher_list = []
    counter = 0
    for b in binary_ord:
        # X is the binary ordinal numbers being turned into an integer with a base of 2 effectively making them into binary numbers
        x = int(binary_ord[counter], 2)
        # Y same operaation as x
        y = int(binary_key, 2)
        # running XOR on the X and Y VAR
        cipher_list.append(x ^ y)
        counter += 1
    # Converting Cipher to readable characters using chr()
    final_list = []
    cipher_string = ""
    for i in cipher_list:
        character = chr(i)
        final_list.append(character)

    cipher_string.join(final_list)
    print(cipher_string)
    print(final_list)


one_binary_function(5, "Hello World")