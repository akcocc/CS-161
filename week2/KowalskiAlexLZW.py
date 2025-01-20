# importing c's unsigned 16bit int type to have constant sized integers.
# This is just for convenience when reading and writing lzw compressed
# data.
from ctypes import c_uint16

from typing import Dict


def generate_init_dict() -> Dict[str, c_uint16]:
    dictionary: Dict[str, c_uint16] = {}
    for i in range(256):
        dictionary[chr(i)] = c_uint16(i)
    return dictionary

# a reversed version of the other dict generator for use in decoding as we will
# be indexing the dictionary by code, not by string, while decoding.
def generate_init_dict_rev() -> Dict[int, str]:
    dictionary: Dict[int, str] = {}
    for i in range(256):
        dictionary[i] = chr(i)
    return dictionary

def build_code_buffer(original_contents: str) -> list[c_uint16]:

    # We first start by initializing our dictionary with all possible single
    # character strings, or in other words, all possible ASCII values.
    dictionary: Dict[str, c_uint16] = generate_init_dict()

    code_buffer: list[c_uint16] = []

    sequence = ""

    # We offset all new dictionary entries by 255 as the first 255 entries of
    # the dictionary are reserved for the ASCII symbols mentioned earlier.
    code = 255

    # Then, while we aren't at the end of the input string, we take the next char
    # and check if the combination of `sequence` and `char` are in the dictionary.
    # If they aren't, we add the combinatin to the dictionary, then append the
    # code for the next longest string that was in the dictionary to our output
    # buffer, `code_buffer`.
    #
    # Once there is no more characters left in the input string to process, we
    # append the code for the remaining sequence to our output buffer, knowing
    # that it will be in the dictionary.

    for char in original_contents:
        sequence += char
        if sequence not in dictionary:

            code += 1
            dictionary[sequence] = c_uint16(code)

            # `sequence[:-1]` can be understood as our current `sequence`,
            # without it's last character, which we know is in the dictionary.
            code_buffer.append(dictionary[sequence[:-1]])

            # `sequence` is then set to the character we omitted in the last step
            # to be used to build the next string sequence
            sequence = char

    code_buffer.append(dictionary[sequence])
    return code_buffer

def build_text_buffer(input_codes: list[int]):
    # As with encoding data, we again initialize a dictionary with each code
    # 0-255 being ASCII characters.
    dictionary: Dict[int, str] = generate_init_dict_rev()

    output_text = ""
    previous_str = ""
    next_code = 255

    # While decompressing data, it's important to keep track of every string
    # appended to the output, as each
    for code in input_codes:
        if code in dictionary:
            output_text += dictionary[code]

            # Only add a new entry if a previously outputed string exists
            if previous_str != "":
                next_code += 1
                dictionary[next_code] = previous_str + dictionary[code][0]
            previous_str = dictionary[code]
        else:
            new_str = previous_str + previous_str[0]
            next_code += 1
            dictionary[next_code] = new_str
            output_text += new_str
            previous_str = new_str
    print(output_text)


def convert_bytes_to_codes(original_bytes: bytes) -> list[int]:
    cursor = 0
    output_codes: list[int] = []
    while cursor < len(original_bytes):
        output_codes.append(int.from_bytes(original_bytes[cursor:cursor+2], byteorder='little', signed=False))
        cursor += 2
    # print(output_codes)
    return output_codes

def compression(file_path: str):

    # we assume the input file to be a text file containing only valid ASCII
    # sorry, we can't compress emojis :( (I've overcomplicated things in this
    # assignment enough already...)
    file = open(file_path, "r")
    original_contents = file.read()
    file.close()

    code_buffer = build_code_buffer(original_contents)

    output_buffer = bytearray()
    for code in code_buffer:
        output_buffer.extend(bytearray(code))

    comp_file = open(f"{file_path}.lzw", "wb")
    comp_file.write(output_buffer)
    comp_file.close()


def decompression(file_path: str):
    comp_file = open(f"{file_path}.lzw", "rb")
    input_buffer = comp_file.read()
    original_codes = convert_bytes_to_codes(input_buffer)
    build_text_buffer(original_codes)
    comp_file.close()
