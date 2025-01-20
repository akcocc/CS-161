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

def build_text_buffer(input_codes: list[int]) -> str:
    # As with encoding data, we again initialize a dictionary with each code
    # 0-255 being ASCII characters.
    dictionary: Dict[int, str] = generate_init_dict_rev()

    output_text = ""
    previous_str = ""
    next_code = 255

    # First, it's important to keep track of every string
    # appended to the output, as each each case (whether the dictionary holds a
    # given code) relies on the last outputted string to add new entries to the
    # dictionary.
    #
    # With that, for every code in `input_codes`, we check if it is in the
    # dictionary. If it is, we make a new dictionary entry containing the last
    # outputted string (if it exists) and the first character of our current
    # code's corresponding string pattern, concatenated together. Next, we
    # append our new dictionary entry to the output and set `previous_str` to
    # the outputted string.
    # If the current code is not in the dictionary, however, we make a new
    # dictionary entry containing `previous_str` concatenated with its first
    # character.
    #
    # By doing all of this, we're essnetially re-tracing the steps the encoder
    # took while building *its* dictionary, while using the same base dictionary
    # of ASCII characters, to get back the original text that was encoded.
    for code in input_codes:
        if code in dictionary:
            # Only add a new entry if a previously outputed string exists
            if previous_str != "":
                next_code += 1
                dictionary[next_code] = previous_str + dictionary[code][0]

            output_text += dictionary[code]

            previous_str = dictionary[code]
        else:
            new_str = previous_str + previous_str[0]
            next_code += 1
            dictionary[next_code] = new_str
            output_text += new_str
            previous_str = new_str
    return output_text


# since writing c's u16's resulted in their bytes represented in little-endian
# format, we need to get back our codes by taking every 2 bytes in the input
# buffer and reading them as little-endian. And since the size of our ints
# doesn't really matter at this point, we can just proceed with python's regular
# `int` type.
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

    print(f"Compressed data is {(len(output_buffer)/len(original_contents))*100}% of the original size")
    comp_file = open(f"{file_path}.lzw", "wb")
    comp_file.write(output_buffer)
    comp_file.close()


def decompression(file_path: str):
    comp_file = open(f"{file_path}", "rb")
    input_buffer = comp_file.read()
    comp_file.close()

    original_codes = convert_bytes_to_codes(input_buffer)
    output_text = build_text_buffer(original_codes)

    uncomp_file = open(f"{file_path}.txt", "w")
    uncomp_file.write(output_text)
    uncomp_file.close()

    print(f"Uncompressed file can be found at {file_path}")

def get_path_extension(path: str):
    extension = ""

    # `some_str[::-1] reverses the string
    for c in path[::-1]:
        extension = c + extension
        if c == "." or len(extension) > 4:
            break
    return extension
