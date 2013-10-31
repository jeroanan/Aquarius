CREATE TABLE IF NOT EXISTS Format (
    Code TEXT PRIMARY KEY,
    Description TEXT,
    MimeType TEXT
);

CREATE TABLE IF NOT EXISTS Author (
    Id INTEGER PRIMARY KEY ASC,
    AuthorName,
    AuthorUri TEXT
);

CREATE TABLE IF NOT EXISTS Book (  
    Id INTEGER PRIMARY KEY ASC,
    Title TEXT,
    Author INT,
    FOREIGN KEY(Author) REFERENCES Author(Id)
);

CREATE TABLE IF NOT EXISTS BookAuthor (
    Book INTEGER,
    Author INTEGER,
    FOREIGN KEY(Book) REFERENCES Book(Id),
    FOREIGN KEY(Author) REFERENCES Author(Id)
);

CREATE TABLE IF NOT EXISTS BookFormat (
    Book INTEGER,
    Format TEXT,
    FOREIGN KEY(Book) REFERENCES Book(Id),
    FOREIGN KEY(Format) REFERENCES Format(Code)
);
