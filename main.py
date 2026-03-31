import datetime

#Methods should be defined before they are called in the program. This is because Python reads the code from top to bottom, and if you try to call a method that hasn't been defined yet, it will result in a NameError. By defining methods at the beginning of the program, you ensure that they are available for use when needed later in the code.
def greet_user(name, age):
    # Using an f-string to format the message
    print(f"Hello {name}! You are {age} years old.")


def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - int(age)
    return birth_year

# Main program execution starts here
name = input("What is your name? ")
age = input("What is your age? ")


message = greet_user(name, age)

print("Your birth year is: " + str(calculate_birth_year(age)))
