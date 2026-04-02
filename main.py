import datetime

#Methods should be defined before they are called in the program. This is because Python reads the code from top to bottom, and if you try to call a method that hasn't been defined yet, it will result in a NameError. By defining methods at the beginning of the program, you ensure that they are available for use when needed later in the code.
def is_adult(age) -> bool:
    return int(age) >= 18
     
def create_message(name, age):
        birth_year = calculate_birth_year(age)
        adult_status = "an adult" if is_adult(age) else "a minor"
        # Using an f-string to format the message
        return f"Hello {name}! You are {age} years old. You are {adult_status},  Your birth year is: {birth_year}"

def start_ai_journey():
    name = input("What is your name? ")
    age = input("What is your age? ")
    print(create_message(name, age))

def calculate_birth_year(age):
    current_year = datetime.datetime.now().year
    birth_year = current_year - int(age)
    return birth_year


# Main program execution starts here
#Indentation is crucial in Python as it defines the scope of loops, functions, and other code blocks. Proper indentation helps to organize the code and makes it more readable. In this program, the methods are defined with proper indentation, and the main execution starts at the end of the file without any indentation, indicating that it is the main block of code that will be executed when the program runs.
start_ai_journey()
 
