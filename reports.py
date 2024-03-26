from connect import *

def search_films():
    try:
        while True:
            print(
                "------------------------------------------\n"
                "Reports Menu\n"
                "------------------------------------------"
                )
            reportOptions = {
                "1": "Print details of all films",
                "2": "Print all films of a particular genre",
                "3": "Print all films of a particular year",
                "4": "Print all films of a particular rating",
                "5": "Exit\n"
                "------------------------------------------"
            }
            for key, value in reportOptions.items():
                print(f"{key}. {value}")

            userOption = input(f"Enter a number from the choices above: ")

            if userOption not in reportOptions:
                print(f"{userOption} is not a valid choice!")
                continue

            if userOption == "1":
                dbCursor.execute("SELECT * FROM tblFilms") # Execute the SQL query
                allFilms = dbCursor.fetchall() # Find all records related to the query
                for films in allFilms:
                    print(films)

            elif userOption == "2":
                userGenre = input(f"Enter a genre: ").title()
                dbCursor.execute(f"SELECT * FROM tblFilms WHERE genre = '{userGenre}'")
                allFilms = dbCursor.fetchall()

                if not allFilms: # Check to see if a film with the genre the user inputted exists
                    print(f"No films found for the genre '{userGenre}'")
                else:
                    for films in allFilms:
                        print(films)

            elif userOption == "3":
                while True:
                    userYear = input(f"Enter a year: ")

                    if not userYear.isdigit() or len(userYear) != 4:
                        print("Invalid input. Please enter a valid year")
                        continue

                    dbCursor.execute(f"SELECT * FROM tblFilms WHERE yearReleased = '{userYear}'")
                    allFilms = dbCursor.fetchall()

                    if not allFilms:
                        print(f"No films found for the year '{userYear}'")
                        break
                    else:
                        for films in allFilms:
                            print(films)
                        break

            elif userOption == "4":
                while True:
                    userRating = input(f"Enter a rating: ").upper()

                    if not len(userRating) <= 5:
                        print("Invalid input. Maximum of 5 characters allowed")
                        continue

                    dbCursor.execute(f"SELECT * FROM tblFilms WHERE rating = '{userRating}'")
                    allFilms = dbCursor.fetchall()

                    if not allFilms:
                        print(f"No films found rated '{userRating}'")
                        break
                    else:
                        for films in allFilms:
                            print(films)
                        break

            elif userOption == "5":
                break

    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    search_films()