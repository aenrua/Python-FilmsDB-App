-- SQLite
PRAGMA foreign_keys=off;

BEGIN TRANSACTION;

ALTER TABLE tblFilms RENAME TO _tblFilms_old;

CREATE TABLE tblFilms(
    filmID integer NOT NULL,
    title text,
    yearReleased integer,
    rating text,
    duration integer,
    genre text,
    primary key (filmID)
    );

INSERT INTO tblFilms (filmID, title, yearReleased, rating, duration, genre)
    SELECT filmID, title, yearReleased, rating, duration, genre
    FROM _tblFilms_old;

COMMIT;

PRAGMA foreign_keys=on;