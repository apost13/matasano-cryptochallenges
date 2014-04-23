import base64, sys

def challenge2():
    buffer1 = raw_input("Please provide the first element for XOR operation: ")
    buffer2 = raw_input("Please provide the second element for XOR operation: ")

    buffer1_size = len(buffer1)
    buffer2_size = len(buffer2)

    if buffer1_size != buffer2_size:
        print "Buffers should have the same size! Quitting..."
        sys.exit(0)

    xor_result = hex(int(buffer1, 16) ^ int(buffer2, 16))[2:-1]

    print "The result of XOR operation is: {0}".format(xor_result)

challenge2()
