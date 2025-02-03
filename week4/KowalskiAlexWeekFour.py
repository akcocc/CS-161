import openpyxl

def todo():
    """
    Used when a new func is not implemented and shouldn't be used in actual code

    Parameters
    ----------
        None

    Returns
    -------
        None

    """
    print("Function not implemented")
    exit(1)

def average(n1: int | float, n2: int | float, n3: int | float) -> float:
    """
   gets the average between 3 numbers

   Parameters
   ----------
      n1 & n2 & n3: float | int
          defines the numbers to average

   Returns
   -------
      float
          the result of averaging the above parameters
   """
    return (n1 + n2 + n3)/3

print(average(7, 5, 9))
print(average(6, 6, 7))

## the commented code below will not run and will error if the above code
# were replaced. This is because python is an interpreted language and reads
# files top to bottom, so when the interpreter tries to run the function in the
# print statement, it wouldn't have seen the function's declaration yet and can't
# execute the function. (This is also why `if __name__ == "__main__"` has to be
# at the bottom of the file)


# print(average(7, 5, 9))
# print(average(6, 6, 7))

# def average(n1: int | float, n2: int | float, n3: int | float) -> float:
#    """
#    gets the average between 3 numbers
#
#    Parameters
#    ----------
#       n1 & n2 & n3: float | int
#           defines the numbers to average
#
#    Returns
#    -------
#       float
#           the result of averaging the above parameters
#    """
#     return (n1 + n2 + n3)/3


# Errors because function parameters are local to the function itself and can
# only be accessed from inside the function. Parameters can be thought as input
# placeholders to where they will be used in the function
# print(n1)

def dog_to_human_years(dog_years: int) -> int:
    """
    the conversion between dog years and human years can be represented by this
    formula: dog's age in human years = 24 + (dog's age - 2) x 4

    Parameters
    ----------
        dog_years: int
            the age of the dog

    Returns
    -------
        int
            the age of the dog in human years
    """
    return (24 + (dog_years - 2)) * 4

def get_car_value(purchase_price: float, age_of_car: int, type_of_car: str):
    """
    calculates the current value of a car based on the type of the car and the
    age of the car.

    Parameters
    ----------
        purchase_price : float
            defines the price of the car when first bought
        age_of_car : int
            defines the number of years after the car was first bought
        type_of_car : str
            defines the type of car to get its appreciation/depreciation rate

    Returns
        None
            prints out the value of the type of car after n years
    -------
    """

    # `str.casefold()` converts all strings to lower case
    type_of_car_lower = type_of_car.casefold()

    current_value: float;

    match type_of_car_lower:
        case "german":
            current_value = purchase_price * (1 - (0.05 * age_of_car))
        case "japanese":
            current_value = purchase_price * (1 - (0.07 * age_of_car))
        case "italian":
            current_value = purchase_price * (1 + (0.05 * age_of_car))
        case _:
            print("Unknown car type:", type_of_car_lower)
            return

    if type_of_car_lower[0] == "i":
        print(f"The value of an {type_of_car_lower} after {age_of_car} years will be ${current_value}")
    else:
        print(f"The value of a {type_of_car_lower} after {age_of_car} years will be ${current_value}")

    def dog_questions():
        """
        asks the user the name and age of their dog and prints out their dog's
        age in human years

        Parameters
        ----------
            None

        Returns
        -------
            None
        """
        name = input("What is your dog's name? ")

        dog_years = input(f"How old is {name}? ")

        dog_years = int(dog_years)

        human_years = dog_to_human_years(dog_years)
        print(f"Your {name} is {human_years} years old.")


def ice_cream_price():
    """
    asks the user the number of scoops of ice cream they want, calculates
    the price by this formula: `Price = number of scoops x $1.15 + $2.25`,
    then prints out the price of an ice cream scoops with the inputted
    number of scoops

    Parameters
    ----------
        None

    Returns
    -------
        None
    """
    num_scoops = input("How many scoops of ice cream would you like? ")
    num_scoops = int(num_scoops)

    cone_price = (num_scoops * 1.15) + 2.25

    print(f"A {num_scoops}-scoop cone will cost ${cone_price}")

if __name__ == "__main__":
    dog_years = 5
    print(f"{dog_years} dog years is equivalent to {dog_to_human_years(dog_years)} human years")

    dog_years = 11
    print(f"{dog_years} dog years is equivalent to {dog_to_human_years(dog_years)} human years")

    get_car_value(30000, 5, "GERMAN")
    get_car_value(30000, 5, "Japanese")
    get_car_value(30000, 5, "iTALIAN")
    get_car_value(30000, 5, "polish")

    ice_cream_price()

    openpyxl.load_workbook()

