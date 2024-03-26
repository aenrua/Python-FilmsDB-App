import sqlite3 as sql # Import the sqlite3 module and assign it an alias

try:
    # Create a variable(object) to hold the path to the folder(file)
    with sql.connect("Projects/Database/filmflix.db") as dbCon: # Use connect function to open folder path, then file
        dbCursor = dbCon.cursor() # Use to execute the SQL statement with the execute method
except sql.OperationalError as e: # Raise SQL error
    print(f"Connection Failed: {e}") # Handling the error