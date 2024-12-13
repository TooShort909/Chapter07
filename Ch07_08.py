def name_search():
    # Read the list of popular names from the file
    with open('popular_names.txt', 'r') as file:
        popular_names = [line.strip() for line in file.readlines()]

    # Ask the user for a name to search
    name_to_search = input("Enter a name to check if it is popular: ").strip()

    if name_to_search in popular_names:
        print(f"The name {name_to_search} is popular.")
    else:
        print(f"The name {name_to_search} is not in the list of popular names.")

name_search()