import requests;
import psutil;

# Spent a little extra time making things more presentable. :)

def pool_admission(age: int) -> int:
    """
    Calculates the admission fee per person for a given `age`.
    Parameters
    ----------
        age: int
            The age of the person.

    Returns
    -------
        int >= 0
            The admission fee for that person in USD.
        int == -1
            An invalid age was inputted.
    """

    # Kinda tricky with the range semantics, so I just interpreted the ranges
    # in the instructions as best as I could (i.e under 2, over 60, between 2
    # and 11, etc.).
    if age < 2:
        return 0;
    elif 2 <= age < 11:
        return 3;
    elif 11 <= age <= 60:
        return 6;
    elif age > 60:
        return 4;

    return -1;

def state_elif(state: str, state_casefold: str):
    """
    `elif` implementation of Exercise 2.

    Parameters
    ----------
        state: str
            Orignal inputted state or province.
        state_casefold: str
            Lowercased version of inputted state or province.
    """
    # elif
    print("IF: ", end = "");
    if (state_casefold == "montana"):
        print("Helena");
    elif (state_casefold == "colorado"):
        print("Denver");
    elif (state_casefold == "ontario"):
        print("Toronto");
    elif (state_casefold == "normandy"):
        print("Rouen");
    elif (state_casefold == "rio grande do norte"):
        print("Natal");
    else:
        print(f"Unknown State/Region/Province: {state}");

def state_dict(state: str, state_casefold: str):
    """
    `dict` implementation of Exercise 2.

    Parameters
    ----------
        state: str
            Orignal inputted state or province.
        state_casefold: str
            Lowercased version of inputted state or province.
    """
    # dict
    print("DICT: ", end = "");
    state_dict = {
        "montana": "Helena",
        "colorado": "Denver",
        "ontario": "Toronto",
        "normandy": "Rouen",
        "rio grande do norte": "Natal",
    };
    print(state_dict.get(state_casefold, f"Unknown State/Region/Province: {state}"));

def state_match(state: str, state_casefold: str):
    """
    `match` implementation of Exercise 2.

    Parameters
    ----------
        state: str
            Orignal inputted state or province.
        state_casefold: str
            Lowercased version of inputted state or province.
    """
    # match
    print("MATCH: ", end = "")
    match state_casefold:
        case "montana":
            print("Helena");
        case "colorado":
            print("Denver");
        case "ontario":
            print("Toronto");
        case "normandy":
            print("Rouen");
        case "rio grande do norte":
            print("Natal");
        case _:
            print(f"Unknown State/Region/Province: {state}");

def number_divisible():
    """
    Wrapper function for Exercise 1.
    """
    number = input("Enter a number: ");
    number = int(number);

    # `%` = modulo/remainder
    # If the remainder from deviding number by 5 is 0, then it is divisible
    # by 5.
    if (number % 5 == 0):
        print(f"{number} is divisible by 5\n");
    else:
        print(f"{number} is not divisible by 5 with a remainder of {number % 5}\n");

def capital_of_state():
    """
    Wrapper function for Exercises 2 & 3.
    """
    state = input("Enter a state, region, or province: ");

    state_casefold = state.casefold();

    # All state names are lowercased to allow for case insensitive user input.
    state_elif(state, state_casefold);
    state_dict(state, state_casefold);
    state_match(state, state_casefold);

def pool_fees():
    """
    Wrapper function for Exercise 4.
    """
    age = input("\nInput your age for pool admission: ");
    age = int(age);

    admission_fee = pool_admission(age);

    if admission_fee == -1:
        print(f"Invalid age: {age}");
    else:
        print(f"Admission fee is ${admission_fee}");

def request_counting():
    """
    Wrapper function for Exercise 5.
    """
    response = requests.get("http://coccbobcat.com");
    occurences = response.text.count("160");

    print(f"\nThe substring '160' appears in http://coccbobcat.com HTML source {occurences} times.");

def process_counting():
    """
    Wrapper function for Exercise 6.
    """
    # PID stands for Process ID.
    # `pids` is a list of all PIDs of currently running processes.
    pids = psutil.pids();

    print(f"\nThere are {len(pids)} running processes");

if __name__ == "__main__":
    # Exercise 1
    number_divisible()

    # Exercise 2 & 3
    capital_of_state()

    # Exercise 4
    pool_fees()

    # Exercise 5
    request_counting()

    # Exercise 6
    process_counting()
