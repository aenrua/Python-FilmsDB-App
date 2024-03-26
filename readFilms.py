from connect import *

def read_films():
    try:
        allFilms = dbCursor.execute("SELECT * FROM tblFilms").fetchall()
        if allFilms:
            print("FilmID |              Title              | Release Year |   Rating   | Duration (mins) | Genre")
            print("*" * 101)

            for aFilm in allFilms:
                print(f"  {aFilm[0]:2}   | {aFilm[1]:31} |     {aFilm[2]:4}     |     {aFilm[3]:5}  |       {aFilm[4]:3}       | {aFilm[5]:15}")
        else:
            print("No film found in the films table")
    
    except sql.OperationalError as e:
        print(f"Failed because : {e}")
    except sql.ProgrammingError as pe:
        print(f"Failed because of Programming Error: {pe}")
    except sql.Error as er:
        print(f"Failed because Error: {er}")
if __name__ == "__main__":
    read_films()