import addFilms, deleteFilms, updateFilms, readFilms
from reports import search_films # To avoid circular dependency

def read_file(file_path): # file_path is a parameter/variable
    try:
        with open(file_path) as readFile:
            rf = readFile.read()
            return rf
    except FileNotFoundError as nf:
        print(f"File not found because: {nf}")

def films_menu():
    option = 0 # Initialise/assign the option variable with an integer value 0
    optionsList = ["1","2","3","4","5","6"] # Create a list of string values/elements/items
    menuChoices = read_file("Projects/Database/menuOptions.txt") # Call the read file function and assign it to a variable

    while option not in optionsList: # Repeat the menu options until the option to exit the menu is entered
        print(menuChoices) # Print the menuChoices by calling the variable that holds the read_file

        option = input("Choose a number from the above: ") # Re-assign the value of the option variable so it can be re-used e.g. 1 = "1", 2 = "2"

        # Check if the input entered in the option variable above is not outside of or within range of 1,2,3,4,5,6
        if option not in optionsList:
            print(f"{option} is not a valid choice!")

    return option

mainProgram = True # Toggle to False to exit the while loop below
while mainProgram: # Same as while True
    mainMenu = films_menu() # Call the films_menu() function and assign it to a variable
    # Match case is the equivalent of switch statements in JS
    match mainMenu:
        case "1": # Call the addFilms file imported on line 1 and the function inside of it called add_film()
            addFilms.insert_film()
        case "2":
            deleteFilms.delete_film()
        case "3":
            updateFilms.update_film()
        case "4":
            readFilms.read_films()
        case "5":
            search_films()
        case _:
            mainProgram = False # Set the mainProgram to False to exit the menu
input("Press enter to exit...")