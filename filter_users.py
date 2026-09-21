import json


def load_users():
    """Loads user data from the JSON file and returns it."""
    with open("users.json", "r") as file:
        return json.load(file)


def filter_users_by_name(name, users):
    """Filters users by the specified name and returns the matching users."""
    return [user for user in users if user["name"].lower() == name.lower()]


def filter_by_age(age, users):
    """Filters users by the specified age and returns the matching users."""
    return [user for user in users if user["age"] == age]


def print_users(filtered_users):
    """Prints the filtered users to the screen."""
    for user in filtered_users:
        print(user)


def main():
    """Starts and controls the program flow."""
    filter_option = input("What would you like to filter by? "
                          "(Currently, only 'name' and 'age' is supported): ").strip().lower()

    users_data = load_users()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filtered_users = filter_users_by_name(name_to_search, users_data)
        print_users(filtered_users)

    elif filter_option == "age":
        try:
            age_to_search = int(input("Enter an age to filter users: ").strip())
            filtered_users = filter_by_age(age_to_search, users_data)
            print_users(filtered_users)
        except ValueError:
            print("Invalid age.")

    else:
        print("Filtering by that option is not yet supported.")


if __name__ == "__main__":
    main()
