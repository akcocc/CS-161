import datetime as dt

# `unit_str` is a optional parameter with a default value of number
# This allows us to change what unit to use when an input is not a valid number
def get_num_input(prompt_str: str, unit_str: str = "number") -> int:
    inp = ""
    while inp is not int:
        inp = input(prompt_str)
        try:
            inp = int(inp)
            break
        except:
            print(f"`{inp}` is not a valid {unit_str}")
    return inp


def pet_printing():
    pet_type = "dog"
    pet_name = "Rosie"

    print(f"I have a {pet_type} and their name is {pet_name}.\n")


def person_printing() -> str:
    users_name = input("Enter your first name: ")
    users_age = 0
    while users_age <= 0:
        users_age = get_num_input("Enter your current age: ", "age")
        # There doesn't exist a person with negative age last time I checked...
        if int(users_age) > 0:
            break
        print(f"`{users_age}` is not a valid age")

    users_annual_savings = get_num_input("Enter your yearly savings: $", "amount")

    print(f"Hello {users_name}! You are currently {users_age} years old.")
    print(f"In 10 years, you will be {users_age + 10} years old.")
    print(f"If you save ${users_annual_savings} each year, in 5 years you will have saved ${users_annual_savings * 5}")
    print(f"Your average monthly savings is ${int(users_annual_savings) / 12}\n")
    return users_name


def time_printing():
    current_datetime = dt.datetime.now()
    print(f"The current date and time is {current_datetime}")

    # To get the the first day of the next month we first use our current datetime to get the current month
    # and set the date to be the 1st of this month (I also set the hour to 0 for a bit of extra percision just in case).
    # Next we can add any number of days to our new datetime that guarantees a datetime within the next month.
    # Finally we can get the first day of next month by setting the day of that new datetime to 1 and the time to 00:00:00.
    next_month = (current_datetime.replace(day=1, hour=0) + dt.timedelta(days=32)).replace(day=1, hour=0, minute=0, second=0)
    # Theres cleaner ways to do this with other libraries such as dateutil, but im not sure if its part of the standard library so I've avoided using it.

    # finall we can get the amount of seconds left in the month by taking the delta between each timestamp's unix-epoch timestamp in seconds.
    time_until_next_month = int(next_month.timestamp() - current_datetime.timestamp())

    print(f"There are only {time_until_next_month} seconds left in this month. Let's go, time's ticking...\n")


# I like this function name
def egg_printing():
    num_eggs = get_num_input("Enter the number of eggs: ")

    print(f"This makes {num_eggs // 12} dozen eggs with {num_eggs % 12} left over\n")


if __name__ == "__main__":
    pet_printing()
    users_name = person_printing()
    time_printing()
    egg_printing()

    print(f"We'll talk again soon, {users_name}...")
