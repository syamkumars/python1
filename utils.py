import datetime


def is_adult(age) -> bool:
    return int(age) >= 18


def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - int(age)
    return birth_year


def get_valid_age():
    while True:
        age = input("What is your age? ")
        if not age.isdigit():
            print("Please enter a number.")
        elif int(age) < 0 or int(age) > 120:
            print("Please enter a valid age.")
        else:
            return age