if __name__ == "__main__":
    name = input("What is your name? ")
    print(f"Hello, {name}!")

    age = input("How old are you? ")

    # Operator "+" not supported for types "str" and "Literal[5]"
    # This means that we can't add a string to a number without first casting
    # one to the type of the other
    try:
        print(age + 5)
    except:
        print(int(age) + 5)

    age_offset = input("How many years in the future? ")

    # This would be a good place to use f-strings
    print("In " + age_offset + " years, you will be " + str(int(age) + int(age_offset)) + " years old.")
