if __name__ == "__main__":
    x = 57
    print(x, bin(x), hex(x))
    x = 57.756

    # x must be an integer
    # try catch here is a good use case since we are expecting an error to
    # happen and we want to be able to continue execution as normal anyways
    try:
        print(x, bin(x), hex(x))
    except Exception as err:
        print(f"parameters must be integers for binary and hex forms; Error message: {err}")

    y = 0b01111111
    z = 0x80
    print("Alternitve representation assignment:", y, z)

    print("Sum between representations:", y + z)
