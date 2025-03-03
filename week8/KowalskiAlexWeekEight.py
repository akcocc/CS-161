import time;
import decimal;
import sys;
from types import FunctionType;

def speaking_screaming():
    """
    Wrapper function for Exercise 1.
    """
    inp = input("Enter a phrase: ");
    upper_first_input = inp.upper()
    while inp != upper_first_input:
        inp = input("Enter the same phrase with all uppercase: ");
    print("OKAY WE GET IT, HI. Jeez...\n");

def vowel_counting():
    """
    Wrapper function for Exercise 2.
    """
    inp = input("Enter a word or phrase: ");
    vowels = 0
    for c in inp:
        match c:
            case "a" | "e" | "i" | "o" | "u":
                vowels += 1;
            case _:
                continue;
    print(f"`{inp}` has {vowels} vowels\n")

def alphabetical_ordering():
    """
    Wrapper function for Exercise 3.
    """
    first_word = input("Enter a word: ");
    second_word = input("Enter another different word: ");

    if first_word < second_word:
        print(f"`{first_word}` comes before `{second_word}`\n");
    else:
        print(f"`{second_word}` comes before `{first_word}`\n");

def is_email_valid(email: str) -> bool:
    """
    Validates that the email provided is a valid email address.

    ----------
    Parameters:
        email: `str`
            the email to check

    -------
    Returns:
        `bool`
            Whether or not the email is valid
    """
    is_valid = email.count("@") == 1

    # early return if the string doesn't have a single "@" to split on.
    if not is_valid:
        return False;

    email_domain = email.split("@")[1];

    return is_valid and "." in email_domain;

def email_vaildation():
    """
    Wrapper function for Exercise 4.
    """
    first_email = first_email = input("Enter a valid email address: ");
    while not is_email_valid(first_email):
        print("That is not a valid email address, please try again...\n")
        first_email = input("Enter a valid email address: ");

    second_email = input("Re-enter your email address: ");
    while second_email != first_email:
        print("Emails do not match, please try again...\n")
        second_email = input("Re-enter your email address: ");

    print("Thank you!\n")

def factorial_recursive(n: int) -> int:
    """
    Recursive implementation of Exercise 5.

    ----------
    Parameters:
        n: `int`
            the current nth calculation

    -------
    Returns:
        `int`
            the final factorial number
    """
    if n == 0:
        return 1;
    return n * factorial_recursive(n-1)

def factorial_iterative(n: int) -> int:
    """
    Recursive implementation of Exercise 5.

    ----------
    Parameters:
        n: `int`
            Which factorial number to calcualte.

    -------
    Returns:
        `int`
            the final factorial number
    """
    current = 1;

    for n in range(2, n+1):
        current *= n;

    return current

MILLISECOND: int = 10**6 # nanoseconds;

def factorial_perf_helper(factorial_func, recursive: bool) -> int:
    """
    Helper function to test each algorithm fairly.

    ----------
    Parameters:
        factorial_func: `FunctionType`
            the function to use during the test.
        recursive: `bool`
            whether or not the inputted function is recursive, enabling recursion depth protections.

    -------
    Returns:
        `int`
            the nth factorial number reached within 10ms
    """

    if factorial_func.__class__ is not FunctionType:
        print("`factorial_func` is not a valid function.");
        exit(1);

    function_name = factorial_func.__name__;

    # the time it took to calculate the last factorial number.
    last_delta = 0;

    last_factorial = 0;
    current_input = 1;

    # We continue calculating factorials until one of the calculations takes
    # more than 10 milliseconds.
    while last_delta < MILLISECOND * 10:
        # we can only go up to the 7995th factorial for recursive functions
        # due to the max recursion depth (which we already had to increase from
        # 995).
        if recursive and current_input == 7995:
            break;
        start = time.perf_counter_ns();
        last_factorial = factorial_func(current_input);
        stop = time.perf_counter_ns();
        last_delta = stop - start;

        # We format the number in scientific notation and print it if the
        # number is more than 1,000,000, otherwise we just print the number in
        # regular decimal format.
        form = "{:.2E}".format(decimal.Decimal(last_factorial))
        if last_factorial > 1_000_000 and current_input % 1000 == 0:
            print(f"`{function_name}`: {form} in {last_delta/MILLISECOND}ms with input `{current_input}`")
        elif last_factorial < 1_000_000:
            print(f"`{function_name}`: {last_factorial} in {last_delta/MILLISECOND}ms with input `{current_input}`")
        current_input += 1;

    # print the last calculated value
    form = "{:.2E}".format(decimal.Decimal(last_factorial))
    print(f"`{function_name}`: {form} in {last_delta/MILLISECOND}ms with input `{current_input}`\n")

    # if the recurse depth limit was hit, inform the user that this happened.
    if recursive and current_input == 4995:
        print("Stopped due to hitting recursion depth limit.\n");
    return current_input;

def factorial_perf():
    """
    Wrapper function for Exercise 5.
    """
    print("Each test will stop after a calculation takes more than 10 milliseconds to complete.")
    print("This can take several minutes to finish...\n")
    recurse = factorial_perf_helper(factorial_recursive, True);
    iter = factorial_perf_helper(factorial_iterative, False);
    if iter > recurse:
        print(f"The iterative implementation won with the {iter}th factorial " +
            f"number versus the recursive implementation with the {recurse}th.");
    elif iter < recurse:
        print(f"The recursive implementation won with the {recurse}th factorial " +
            f"number versus the iterative implementation with the {iter}th.");
    else:
        print(f"The iterative and recursive implementations tied with the " +
            f"{recurse}th factorial number");
    # I've found that the highest number each algorithm can reach are a lot
    # closer than I thought they would be. Sometimes the iterative
    # implementation wins, sometimes the recursive implementation wins; each
    # topping out at about the 7000th and up to 7500th factorial number...
    #
    # Additionally, I could set up another test to run _this_ test at least 100
    # times to see which how often the iterative implementation wins, versus
    # how often the recursive implementation wins. But running such a test would
    # be tricky as each normal run take about 2 minutes to complete on
    # my machine, so such a test would take over 3 hours to finish...

if __name__ == "__main__":
    # Exercise 1
    speaking_screaming();

    # Exercise 2
    vowel_counting();

    # Exercise 3
    alphabetical_ordering();

    # Exercise 4
    email_vaildation();

    # Exercise 5
    # 995 is far from enough...
    sys.setrecursionlimit(8000)
    factorial_perf();
