import random as rand;
import os;
import time

def even_numbers():
    """
    Wrapper function for Exercise 1.
    """
    lower_bound = int(input("Enter lower bound: "));
    upper_bound = int(input("Enter upper bound: "));
    if lower_bound > upper_bound:

        # swapping with python's tuple unpacking feature.
        # all future swapping operations will use this method.
        lower_bound, upper_bound = upper_bound, upper_bound;
        print("Swapped lower and upper bounds as the inputted lower bound " +
              "is more than the inputted upper bound");
    for n in range(lower_bound, upper_bound):
        if (n % 2 == 0):
            print(n);
    print();

def printing_factors():
    """
    Wrapper function for Exercise 2.
    """
    num = int(input("Enter a number: "));
    i = num;
    while i > 0:
        if (num % i == 0):
            print(f"{i} is a factor of {num}");
        i -= 1;
    print();

ALPHABET = ["a", "b", "c", "d", "e",
            "f", "g", "h", "i", "j",
            "k", "l", "m", "n", "o",
            "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"];

def summing_names_nested_loops(name: str) -> int:
    """
    nested loops implementation of Exercise 3.

    Parameters
    ----------
        name: str
            the inputted name

    Returns
    -------
        int
            the sum of the letters in the input name
    """
    sum = 0;
    for c in name:
        for i in range(len(ALPHABET)):
            if c == ALPHABET[i]:
                sum += i;
    return sum;

ASCII_A = ord("a");

def summing_names_ord(name: str) -> int:
    """
    `ord()` implementation of Exercise 3.

    Parameters
    ----------
        name: str
            the inputted name

    Returns
    -------
        int
            the sum of the letters in the input name
    """
    sum = 0
    for c in name:
        sum += ord(c) - ASCII_A;
    return sum;

def summing_names():
    """
    Wrapper function for Exercise 3.
    """
    name = input("What is your name? ");
    sum_nested = summing_names_nested_loops(name);
    sum_ord = summing_names_nested_loops(name);

    print("sum using nested loops implementation:", sum_nested);
    print("sum using ord implementation:", sum_ord, end="\n\n");

def squaring(end_square_num: int, current_square_num: int = 1):
    """
    Recursive function to calculate the next highest square

    Parameters
    ----------
        end_square_num: int
            the highest number to square
        current_square_num: int
            the current number to square, starting with 1.
    """
    square = current_square_num**2;

    print(square);

    if square == end_square_num**2:
        return;

    squaring(end_square_num, current_square_num=current_square_num+1);

def squaring_wrapper():
    """
    Wrapper function for exercise 4.
    """
    num = int(input("Enter a number: "));

    squaring(num);

    print();


def print_sort_state(arr: list[int], first_iter: bool = False):
    """
    prints the state of an array of integers as varying number of stars,
    clearing the last set of stars that were printed.

    Parameters
    ----------
        arr: list[int]
            the list of integers to print the state of
        first_iter: bool
            whether or not to clear the screen depending on if the fisrt 'frame'
            was 'rendered' already.
    """
    if not first_iter:
        # moves cursor up by the length of the array plus 1.
        print(f"\033[{len(arr)+1}A", end="");

        # clears everything from the cursor to the end of the terminal screen.
        print(f"\033[0J", end="");
    else:
        # add some buffer room before printing
        print("\n\n\n\n");

    # prints n stars in a line where n is the current item in the list
    for n in range(len(arr)):
        print("*" * arr[n]);

    # some delay so the animation isn't too fast
    time.sleep(0.01);

def quick_sort(arr: list[int], start: int, end: int, first_iter: bool = False):
    """
    quicksort using Hoare's partition algorithm.

    Parameters
    ----------
        arr: list[int]
            the list of numbers to sort
        start: int
            the current start of an array
        end: int
            the current end of an array
        first_iter: bool
            whether or not its the first recursion, only used for printing
            the sorting animation
    """
    # prints the sorting animation
    print_sort_state(arr, first_iter);

    # base case, once start and end meet or pass, return, finishing the sort
    if start >= end:
        return;

    # picks a pivot and moves numbers more than the pivot to the right, less to
    # the left, then returns a splitting index.
    split = partition(arr, start, end);

    # recurse left
    quick_sort(arr, start, split-1);
    # recurse right
    quick_sort(arr, split, end);

def partition(arr: list[int], start: int, end: int) -> int:
    """
    Hoare's partition algorithm.

    Parameters
    ----------
        arr: list[int]
            the list of numbers to sort
        start: int
            the current start of an array
        end: int
            the current end of an array

    Returns
    -------
        int
            the index that will subdivide the array into two more partitions
    """
    pivot = arr[start];

    left = start;
    right = end;
    while True:
        # find first number more than pivot from the left
        while (arr[left] < pivot):
            left += 1;

        # find first number less than pivot from the right
        while (arr[right] > pivot):
            right -= 1;

        # if left and right cross, break and return left to split array
        if (left > right):
            break;

        # swap
        arr[left], arr[right] = arr[right], arr[left];

        # increment left and right to continue
        left += 1;
        right -= 1;

    return left;

def sort_into_teepee(arr: list[int], lines: int):
    """
    sort by odd numbers ascending, then even numbers descending

    Parameters
    ----------
        arr: list[int]
            the array to resort
        lines: int
            the number of available terminal lines on the screen
    """
    # swap odd numbers with their next even numbered neighbors
    i = 0
    while i < len(arr)-1:
        arr[i], arr[i+1] = arr[i+1], arr[i];
        print_sort_state(arr);
        i += 2;

    # separate even and odd numbers
    i = 0
    while i < len(arr):
        for j in range(len(arr)-1):
            if (arr[j] % 2 == 1):
                arr[j], arr[j+1] = arr[j+1], arr[j];

        print_sort_state(arr);
        i += 1;

    # find first odd number
    i = 0;
    while (arr[i] % 2 != 1):
        i += 1;

    # if line number is odd, we need to add one
    if (lines % 2 == 1):
        i += 1;

    # reverse odd numbers
    j = len(arr)-1;
    while i < j:
        arr[i], arr[j] = arr[j], arr[i];
        print_sort_state(arr);
        i += 1;
        j -=1;

    # reverse entire array so odd numbers ascend and even numbers decend
    i = 0
    j = len(arr)-1;
    while i < j:
        arr[i], arr[j] = arr[j], arr[i];
        print_sort_state(arr);
        i += 1;
        j -=1;

def teepee_sorting():
    """
    Wrapper function for Exercise 5.
    (Got a bit carried away...)
    """
    terminal_dimensions = os.get_terminal_size();
    lines = terminal_dimensions.lines;
    cols = terminal_dimensions.columns;
    arr = [];

    # We use the the smallest dimension of the terminal screen to determine the
    # size of the array.
    if lines >= cols:
        arr = [n for n in range(1, cols-5)];
    else:
        arr = [n for n in range(1, lines-5)];
    rand.shuffle(arr);
    unsorted = list(arr);
    # sort arr
    quick_sort(arr, 0, len(arr)-1, True);

    sort_into_teepee(arr, lines);

    print("Unsorted Array: ", unsorted);
    print("TeePee Array: ", arr, end="\n\n");

def next_highest_number():
    """
    Wrapper function for Exercise 6.
    """
    num = input("Enter a number: ");

    # make sure the input can be cast to an integer

    old_num = int(num);
    num = list(num);

    for i in reversed(range(1, len(num))):
        if int(num[i-1]) < int(num[i]):
            num[i], num[i-1] = num[i-1], num[i];
            break;
    num = "".join(num);

    if old_num >= int(num):
        print("A higher number with the same digits does not exist.");
    else:
        print("Next highest number with same digits:", num);

if __name__ == "__main__":
    # Exercise 1
    even_numbers();

    # Exercise 2
    printing_factors();

    # Exercise 3
    summing_names();

    # Exercise 4
    squaring_wrapper()

    # wait 1 second before showing next exercise, so it can be viewed properly.
    time.sleep(1);

    # Exercise 5
    teepee_sorting();

    # Exercise 6
    next_highest_number();
