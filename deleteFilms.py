from connect import *

def delete_film():
    try:
        # filmID is primary key field
        filmID = int(input("Enter the FilmID of the record to be deleted: "))
        dbCursor.execute(f"SELECT * FROM tblFilms WHERE filmID = {filmID}")

        # The fetchone method is a unique (one) record
        row = dbCursor.fetchone()

        if row == None:
            print(f"Delete is not possible as no record with the FilmID {filmID} exists!")
        else:
            dbCursor.execute("DELETE FROM tblFilms WHERE filmID = ?", (filmID,))
            dbCon.commit()
            print(f"Record with FilmID {filmID} has been deleted from the films table")

    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    delete_film()