import csv
import os
import requests

def get_bound(path: str, age: int) -> float:
    file = open(path)
    reader = csv.reader(file)

    # We use a list comprehension here to filter by the year, returning a list
    # of rows containing the year 2024
    rows = [row for _, row  in enumerate(reader) if row[0].isnumeric() and int(row[0]) == 2024]

    # 8th column is the years left for a given age x
    return float(rows[int(age)][7])

def ensure_csv_downloaded(path: str, alt_url: str = ""):
    url = f"https://www.ssa.gov/OACT/HistEst/PerLifeTables/2019/{path[2:]}"
    if alt_url != "":
        url = alt_url

    if not os.path.exists(path):
        print(f"Downloading {path[2:]}")
        resp = requests.get(url)
        m_file = open(path, "wb")
        m_file.write(resp.content)

def greet_user_n_get_age() -> str:
    name = input("What is your name? ")
    print(f"\nHello, {name}!\n")

    return input("How old are you? ")

def fix_age_from_err(age: str) -> int:
    # Operator "+" not supported for types "str" and "Literal[5]"
    # This means that we can't add a string to a number without first casting
    # one to the type of the other
    try:
        print(age + 5)
    except:
        # extra print for spacing
        print("")
        print(int(age) + 5)
        print("success\n")

    return int(age)

def age_offset(age: int):
    age_offset = input("How many years in the future? ")
    print(f"In {age_offset} years, you will be {age + int(age_offset)} years old.\n")

def predict_life_span(age: int):
    wants_death_date = input("Would you like to be given your probable life expectancy? (y/N) ")

    if wants_death_date.strip() != "y":
        print("Well you're getting it anyways! :D")

    m_bound = get_bound(m_file_path, age)
    f_bound = get_bound(f_file_path, age)

    # sort the maximum/minum ages into upper and lower bounds
    lower_bound = m_bound if m_bound <= f_bound else f_bound
    upper_bound = f_bound if f_bound > m_bound else m_bound

    print("\nAccording to the United States Social Security Administraion Projected Period Life tables between the years 2017 and 2095,")
    print(f"you have between {lower_bound} and {upper_bound} years left in your life!\n")

# I mean, *technically* I'm still using the csv you gave us lol
def cleanup_tax_csv_data(path: str) -> list[tuple[int, float, float]]:
    file = open(path)
    reader = csv.reader(file)
    rows = enumerate(reader)
    rows = [row for _, row in rows]

    new_rows: list[tuple[int, float, float]] = []

    for i in range(len(rows)):
        # i == 0 is an empty row, so we skip it
        if i == 0:
            continue

        if i == 1:
            # ith row -> 4th column in row -> first character removed
            # -> leading/trailing whitespace removed -> strip comma -> cast to float
            #
            # other values are hard coded
            new_rows.append((10, 0, float(''.join(rows[i][3][1:].strip().split(",")))))

        # -2 because theres a second extra empty row in the data
        elif i == len(rows) - 2:

            # its easier to hard code this one I think... (-1 == infinity)
            new_rows.append((37, 609350.01, -1))
            break
        else:

            # first value: ith row -> 1st column -> remove last character
            #            -> strip comma -> cast to float
            #
            # second value: ith row -> 2nd column -> split on "$ "
            #               -> take right side -> strip comma -> cast to float

            # third value: ith row -> 4th column in row
            #            -> first character removed leading/trailing whitespace removed
            #            -> strip comma -> cast to float
            new_rows.append((
                int(rows[i][0][:-1]),
                # this is just cursed
                float(''.join(rows[i][1].split("$ ")[1].split(","))),
                float(''.join(rows[i][3][1:].strip().split(",")))
            ))
    return new_rows

def get_income() -> float:
    hours = input("Enter the number of hours worked this week: ")
    hourly_wage = input("Enter your hourly wage: $")

    weekly_income = float(hours) * float(hourly_wage)
    print(f"\nYour gross pay this week is ${weekly_income}")

    gross_annual_income = float(hourly_wage) * float(hours) * 50

    print(f"Your estimated annual gross income will be ${gross_annual_income}")

    return gross_annual_income

def get_taxed_income(gross_income: float):
    tax_data = cleanup_tax_csv_data("./tax_table.csv")

    tax_rate = 0
    for row in tax_data:
        tax_rate = row[0]
        if row[1] <= gross_annual_income <= row[2] and row[2] != -1:
            break

    print(f"Your annual income after taxes at a {tax_rate}% tax rate is ${gross_income * (1 - (float(tax_rate)/100))}")

if __name__ == "__main__":

    m_file_path = "./PerLifeTables_M_Alt2_TR2019.csv"
    f_file_path = "./PerLifeTables_F_Alt2_TR2019.csv"


    # Incase either male/female life tables aren't present in the current working
    # directory, we download them
    ensure_csv_downloaded(m_file_path)
    ensure_csv_downloaded(f_file_path)

    # Tax table
    ensure_csv_downloaded("./tax_table.csv", "https://drive.google.com/uc?export=download&id=1-RHCQBjr1efISXuZ-zte-pGmHKkV9Xqj")
    print("")

    age = greet_user_n_get_age()

    age = fix_age_from_err(age)

    age_offset(age)

    predict_life_span(age)

    gross_annual_income = get_income()

    get_taxed_income(gross_annual_income)
