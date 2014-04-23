import base64

def challenge1():
    operation_id = int(raw_input("Please give 1 for base64 to hex or 2 for hex to base64 encoding: "))
    if operation_id == 1:
        str_result = base64_2_hex()
    elif operation_id == 2:
        str_result = hex_2_base64()
    else:
        print "Operation not available."
    print "The resulting string is {0}".format(str_result)

def hex_2_base64():
    str_decode = raw_input("Please give hex string to base64 encode: ")
    tmp_data = base64.b16decode(str_decode, True)
    print "The base16 decoded data: {0}".format(tmp_data)
    str_result = base64.b64encode(tmp_data)
    return str_result

def base64_2_hex():
    str_decode = raw_input("Please give base64 string to hex encode: ")
    tmp_data = base64.b64decode(str_decode)
    print "The base64 decoded data: {0}".format(tmp_data)
    str_result = base64.b16encode(tmp_data)
    return str_result

challenge1()

