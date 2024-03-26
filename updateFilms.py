from connect import *

def update_film():
    try:
        print(
            "---------------------------------------------------\n"
            "Amend Menu\n"
            "---------------------------------------------------"
            )
        filmID = int(input("Enter the FilmID of the record to be amended: ")) # Get filmID from the user
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")
        row = dbCursor.fetchone()

        if row == None: # None is a singleton object that checks if a value is present
            print(f"No record with the 'FilmID' {filmID} exists!")
        else:
            while True: # Loops the process until the user chooses the exit
                updateOptions = { # Create a dictionary with the options (for display only)
                    "1": "Title",
                    "2": "Release Year",
                    "3": "Rating",
                    "4": "Duration",
                    "5": "Genre",
                    "6": "Exit\n"
                    "---------------------------------------------------"
                }
                columnMapping = { # Create a dictionary with the option names linked to the db column names
                    "1": "title",
                    "2": "yearReleased",
                    "3": "rating",
                    "4": "duration",
                    "5": "genre"
                }
                while True:
                    for key, value in updateOptions.items():
                        print(f"{key}. {value}") # Display the updateOptions dictionary

                    userOption = input(f"Enter the number of the field you want to amend: ")

                    while userOption not in updateOptions: # Loop if the user entered an option that is not displayed
                        print(f"{userOption} is not a valid choice!")
                        userOption = input(f"Enter the number of the field you want to amend: ")

                    if userOption == "6":
                        return

                    option = updateOptions[userOption] # Select the option from the updateOptions dictionary based on the user input

                    if userOption in columnMapping: # Check to see if the user input option has a corresponding db column name
                        columnName = columnMapping[userOption] # Select the column name from the columnMapping dictionary based on the user input

                    fieldValue = input(f"Enter the new value for '{option}': ") # Ask the user to enter a new value for the option selected
                    if columnName == "title":
                        break
                    elif columnName == "yearReleased":
                        if fieldValue.isdigit() and len(fieldValue) == 4:
                            break
                        else:
                            print("Invalid input. Please enter a valid year")
                            continue
                    elif columnName == "rating":
                        fieldValue = fieldValue.upper()
                        if len(fieldValue) <= 5:
                            break
                        else:
                            print("Invalid input. Maximum of 5 characters allowed")
                            continue
                    elif columnName == "duration":
                        if fieldValue.isdigit():
                            break
                        else:
                            print("Invalid input. Please enter a number")
                            continue
                    elif columnName == "genre":
                        fieldValue = fieldValue.title()
                        break

                dbCursor.execute(f"UPDATE tblFilms SET {columnName} = ? WHERE filmID = ? ", (fieldValue, filmID)) # Update the database with the new field value
                dbCon.commit()
                print(f"'{option}' for record with FilmID {filmID} updated")
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    update_film()