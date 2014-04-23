# Decrypt a given message that uses a single character as key.

import base64, string

def challenge3():
    ciphertext = raw_input("Please provide the encrypted string: ")

    list_lowercase = list(string.ascii_lowercase)
    list_uppercase = list(string.ascii_uppercase)

    alphabet = list_lowercase + list_uppercase

    for x in alphabet:
        print "Using key: {0}".format(x)


        plaintext = hex(int(ciphertext, 16) ^ int(len(ciphertext)/2 * hex(ord(x))[2:], 16))[2:-1]
        decoded_result = base64.b16decode(plaintext, True)

        print "Plaintext (hex): {0}".format(plaintext)
        print "Plaintext (ascii): {0}".format(decoded_result)


challenge3()

