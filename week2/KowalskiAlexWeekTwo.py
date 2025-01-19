from os.path import exists
from sys import argv
from typing import Dict

# importing c's unsigned 16bit int type to have constant sized integers.
# This is just for convenience when reading and writing to and from lzw compressed
# data.
from ctypes import c_uint16

def printing_reps(x: int):
    print(x, bin(x), hex(x))

def float_error(x: float):
    # x must be an integer
    # try catch here is a good use case since we are expecting an error to
    # happen and we want to be able to continue execution as normal anyways
    try:
        print(x, bin(x), hex(x))
    except Exception as err:
        print(f"parameters must be integers for binary and hex forms; Error message: {err}")

def adding_reps():
    y = 0b01111111
    z = 0x80
    print("Alternitve representation assignment:", y, z)
    print("Sum between representations:", y + z)

def data_compression(file_path: str):
    file = open(file_path)
    original_contents = file.read()
    file.close()

    dictionary: Dict[str, c_uint16] = {}
    cursor = 0

    code_buffer: list[c_uint16] = []
    first_char = original_contents[cursor]
    last_code = c_uint16()
    while cursor < len(original_contents):
        cursor += 1
        next_char = original_contents[cursor]
        if dictionary.__contains__(first_char + next_char):
            first_char += next_char
        else:
            first_char = next_char
            last_code = assign_code(first_char, len(dictionary))
            dictionary[first_char] = last_code
            code_buffer.append(last_code)
    code_buffer.append(last_code)

    dict_buffer: list[c_uint16] = []

    # Dictionary strings are represented as the size of the string as a u16
    # followed by the string itself
    for dict_str, _ in dictionary:
        dict_buffer.append(c_uint16(len(dict_str)))
        dict_buffer.append(c_uint16(len(dict_str)))

    dict_size = c_uint16(len(dictionary))

    comp_file = open(f"{file_path}.lzw", "ab")

    comp_file.write(dict_size)
    comp_file.close()

def assign_code(new_str: str, dict_len: int) -> c_uint16:
    if len(new_str) > 1:
        # All strs with more than one char are offset by 255
        # 0-255 are reserved for ascii chars
        return c_uint16(255 + dict_len + 1)

    # All strs with a single char use their ascii code in the
    # dictionary
    return c_uint16(ord(new_str))

def theor_compr_rate():
    original_size = 240

    dictionary_size = 25
    compressed_size = 148

    percent_of_compression = (compressed_size + dictionary_size)/original_size

    print("Original Size:", original_size)
    print("Dictionary Size:", dictionary_size)
    print("Compressed Size:", compressed_size)

    print(f"Theoretical compression rate given the above parameters: {percent_of_compression * 10}%")


if __name__ == "__main__":
    args = argv

    x = 57
    printing_reps(x)

    x = 57.756
    float_error(x)

    x = 57

    adding_reps()
    theor_compr_rate()

    file_path = argv[1]

    if file_path != "" and exists(file_path):
        data_compression(file_path)
