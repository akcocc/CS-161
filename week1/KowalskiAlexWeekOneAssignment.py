import datetime as dt

def pet_printing():
    pet_type = "dog"
    pet_name = "Rosie"

    print(f"I have a {pet_type} and their name is {pet_name}.")

def person_printing():
    users_name = input("Enter your first name: ")
    users_age = ""
    while users_age is not int or users_age <= 0:
        users_age = input("Enter your current age: ")
        try:
            users_age = int(users_age)
        # There doesn't exist person with negative age last time I checked...
            if int(users_age) <= 0:
                print(f"`{users_age}` is not a valid age")
                continue
            break
        except:
            print(f"`{users_age}` is not a valid age")
    users_annual_savings = ""
    while users_annual_savings is not int:
        users_annual_savings = input("Enter your yearly savings: $ ")
        try:
            users_annual_savings = int(users_annual_savings)
            break
        except:
            print(f"`{users_annual_savings}` is not a valid number")

    print(f"Hello {users_name}! You are currently {users_age} years old.")
    print(f"In 10 years, you will be {users_age + 10} years old.")
    print(f"If you save ${users_annual_savings} each year, in 5 years you will have saved ${users_annual_savings * 5}")
    print(f"Your average monthly savings is ${int(users_annual_savings) / 12}")

def time_printing():
    current_datetime = dt.datetime.now()
    print(current_datetime)

    # To get the the first time we first use our current datetime to get the month
    # and set the date to be the first of this month. This will set the time to be 00:00 of the first of this month.
    # Next we can add any number of days to our new datetime that guarantees a datetime with the month as next month.
    # Finally we can get the first day of this month by setting the day of that new datetime to 1.
    next_month = (current_datetime.replace(day=1, hour=0) + dt.timedelta(days=32)).replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    time_until_next_month = int(next_month.timestamp() - current_datetime.timestamp())

    print(time_until_next_month)


if __name__ == "__main__":
    # pet_printing()
    # person_printing()
    time_printing()
