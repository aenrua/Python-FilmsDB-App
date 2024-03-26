from connect import *

# Create a subroutine to add films to the films table
def insert_film():
    try:
        # Create variables for each field to store the respective data from the input function
        fTitle = input("Enter film title: ")
        while True:
            fYear = input("Enter release year: ")
            if fYear.isdigit() and len(fYear) == 4:
                break
            else:
                print("Invalid input. Please enter a valid year")
        while True:
            fRating = input("Enter rating: ")
            if len(fRating) <= 5: # Maximum of 5 characters
                fRating = fRating.upper()
                break
            else:
                print("Invalid input. Maximum of 5 characters allowed")
        while True:
            fDuration = input("Enter duration (in minutes): ")
            if fDuration.isdigit():
                break
            else:
                print("Invalid input. Please enter a number")
        fGenre = input("Enter genre: ").title()
        
        dbCursor.execute("INSERT INTO tblFilms VALUES(NULL,?,?,?,?,?)", (fTitle, fYear, fRating, fDuration, fGenre))

        dbCon.commit()
        print(f"'{fTitle}' added to the films table")

    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    insert_film()