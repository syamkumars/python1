import json


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


def save_users(users):
    with open("user.json", "w") as file:
        json.dump(users, file, indent=4)