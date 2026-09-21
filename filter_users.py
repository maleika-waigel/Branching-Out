import json


def load_users():
    """Lädt Benutzerdaten aus der JSON-Datei und gibt sie zurück."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name, users):
    """Filtert Benutzer nach dem eingegebenen Namen und gibt sie aus."""
    filtered_users = [user for user in users if user["name"].lower() == name.lower()]

    for user in filtered_users:
        print(user)


def filter_by_age(age, users):
    """Filtert Benutzer nach dem eingegebenen Alter und gibt sie aus."""
    filtered_users = [user for user in users if user["age"] == age]

    for user in filtered_users:
        print(user)


if __name__ == "__main__":
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name' and 'age' is supported): ").strip().lower()

    users_data = load_users()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search, users_data)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filter_by_age(age_to_search, users_data)
        except ValueError:
            print("Invalid age.")

    else:
        print("Filtering by that option is not yet supported.")
