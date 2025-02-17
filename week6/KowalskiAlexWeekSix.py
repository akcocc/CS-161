def blastoff_input() -> tuple[int, int]:
    """
    Gets the input for future blastoff functions

    Returns
    -------
        int > 0
    """
    num = int(input("Enter a number > 0: "));
    while num <= 0:
        print(f"{num} is not > 0. Please try again");
        num = int(input("Enter a number > 0: "));
    return (num, 1)

def blastoff_input_w_step() -> tuple[int, int]:
    """
    Gets the input for future blastoff functions

    Returns
    -------
        int > 0
    """
    num = int(input("Enter a number > 0: "));
    while num <= 0:
        print(f"{num} is not > 0. Please try again");
        num = int(input("Enter a number > 0: "));

    step = int(input("Enter a number > 0 to decrease by: "));
    while step <= 0:
        print(f"{step} is not > 0. Please try again");
        num = int(input("Enter a number > 0 to decrease by: "));
    return (num, step)


def blastoff(num: int, decrease_step: int):
    """
    Wrapper function for Exercise 1.

    Parameters
    ----------
        num: int
            starting number
        decrease_step: int
            amount to decrease by on every iteration of the loop
    """
    while num > 0:
        print(num);
        num -= decrease_step;
    print("Blastoff!\n");


def blastoff_even_odd(num: int, decrease_step: int):
    """
    Wrapper function for Exercise 2 & 3.

    Parameters
    ----------
        num: int
            starting number
        decrease_step: int
            amount to decrease by on every iteration of the loop
    """
    while num > 0:
        print(f"{num}; ", end="");
        if num % 2 == 0:
            print("even");
        else:
            print("odd");
        num -= decrease_step;

    print("Blastoff!\n");

def longer_words(word_limit: bool):
    """
    Wrapper function for Exercise 4.

    Parameters
    ----------
        word_limit: bool
            states whether the user should be limited by the amount of words
            they're able to input
    """
    current_len = 5;
    word_count = 0;
    while current_len >= 5:
        word = input("Enter a word: ");
        current_len = len(word);
        print(f"{word} has {current_len} letters")
        word_count += 1;
        if word_count == 5 and word_limit:
            break;

    if word_count == 5 and word_limit:
        print("Too many words\n")
    else:
        print("Goodbye\n")

def hundreds_counting():
    """
    Wrapper function for Exercise 5.
    """
    num = 0;
    while num <= 100:
        print(f"Decimal: {num} Binary: {bin(num)} Hex: {hex(num)}");
        num += 1;
    print()

def heat_death_iteration(num_stars: int):
    """
    Iteration implementation of Exercise 6.
    """
    while num_stars > 0:
        print("*" * num_stars);
        num_stars -= 1;

def heat_death_recursion(num_stars: int):
    """
    Recursion implementation of Exercise 6.
    """
    print("*" * num_stars);
    if num_stars > 0:
        heat_death_recursion(num_stars - 1);

def heat_death():
    """
    Wrapper function for Exercise 6.
    """
    num_stars = input("How many stars do you see in the sky at night? ");
    num_stars = int(num_stars);
    if num_stars <= 0:
        print("I see... Light pollution can be like that I guess.");
    heat_death_iteration(num_stars);
    print()
    heat_death_recursion(num_stars);

    print("Eventually there will be no stars...\n");

def sum_digits_func(input: str) -> int:
    if len(input) > 0:
        return int(input[0]) + sum_digits_func(input[1:])
    else:
        # no more digits to sum
        return 0

def sum_digits():
    """
    Wrapper function for Extra Credit 1.
    """
    num = input("Enter a number > 0: ");
    while not num.isdecimal() or int(num) <= 0:
        print(f"{num} is not > 0 or isn't a number");
        num = input("Enter a number > 0: ");

    print(f"The sum of the digits of {num} is {sum_digits_func(num)}\n")

def palindrome_check(word: str) -> bool:
    # We check if the first and last characters are the same
    if len(word) > 0 and word[0] == word[len(word)-1]:
        # Then we pass in the same word with the first and last characters removed
        # into our recurseive function.
        return palindrome_check(word[1:len(word)-1])

    # If the above condition is false, that means that the first and last
    # characters of whatever word we're checking are not the same or the
    # length of the word is 0. By this point, if the length of our word is more
    # than 1 that means it isn't a palindrome, otherwise we can safely say that
    # it is, assmuming that the length of the word we started with was more
    # than 1.
    return len(word) <= 1

def recursive_palindrome():
    """
    Wrapper function for Extra Credit 2.
    """
    word = input("Enter any word: ");
    while len(word) == 0:
        word = input("Please enter a word: ")

    if palindrome_check(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")


if __name__ == "__main__":
    # Exercise 1
    num, step = blastoff_input()
    blastoff(num, step);

    # Exercise 2
    num, step = blastoff_input()
    blastoff_even_odd(num, step);

    # Exercise 3
    num, step = blastoff_input_w_step()
    blastoff_even_odd(num, step);

    # Exercise 4.1
    longer_words(False);

    # Exercise 4.2
    longer_words(True);

    # Exercise 5
    hundreds_counting();

    # Exercise 6
    heat_death()

    # Extra Credit 1
    sum_digits();

    # Extra Credit 2
    recursive_palindrome();
