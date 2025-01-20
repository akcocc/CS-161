from os.path import exists
from sys import argv

import KowalskiAlexLZW as lzw

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

    try:
        file_path = argv[1]
        if exists(file_path):
            # Very jank
            if lzw.get_path_extension(file_path) == ".lzw":
                print("\nDecompressing file...\n")
                lzw.decompression(file_path)
            else:
                lzw.compression(file_path)
    except:
        exit(0)

