import datetime
import json


# Methods should be defined before they are called in the program. This is because Python reads the code from top to bottom, and if you try to call a method that hasn't been defined yet, it will result in a NameError. By defining methods at the beginning of the program, you ensure that they are available for use when needed later in the code.
def is_adult(age) -> bool:
    return int(age) >= 18


def create_message(name, age):
    birth_year = calculate_birth_year(age)
    adult_status = "an adult" if is_adult(age) else "a minor"
    # Using an f-string to format the message
    return f"Hello {name}! You are {age} years old. You are {adult_status},  Your birth year is: {birth_year}"


def create_user_summary(user):
    name = user.get("name", "Unknown")
    age = user.get("age", "Unknown")
    city = user.get("city", "Unknown")
    return f"{name} is {age} years old and lives in {city}. Their birth year is {user.get('birth_year', 'Unknown')}."


def save_users(users):
    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)


def load_users():
    try:
        with open("user.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print ("No existing file found")
        return []
    except json.JSONDecodeError:
        print ("Error in file format. Will overwrite fully")
        return []


def get_valid_age():
    while True:
        age = input("What is your age? ")
        if not age.isdigit():
            print("Please enter a number.")
        elif int(age) < 0 or int(age) > 120:
            print("Please enter a valid age.")
        else:
            return age
           

def start_ai_journey():
    users = load_users()
    addUser = input("Do you want to add a user? (yes/no) ")
    if addUser.lower() == "yes" or addUser.lower() == "1" or addUser.lower() == "y":
        for i in range(1):
            name = input("What is your name? ")
            age = get_valid_age()
            city = input("What is your city?")
            user = {
                "name": name,
                "age": age,
                "city": city,
                "birth_year": calculate_birth_year(age),
            }
        users.append(user)

    save_users(users)

    # print(create_message(name, age))
    for user in users:
        print(create_user_summary(user))


def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - int(age)
    return birth_year


# Main program execution starts here
# Indentation is crucial in Python as it defines the scope of loops, functions, and other code blocks. Proper indentation helps to organize the code and makes it more readable. In this program, the methods are defined with proper indentation, and the main execution starts at the end of the file without any indentation, indicating that it is the main block of code that will be executed when the program runs.
start_ai_journey()
