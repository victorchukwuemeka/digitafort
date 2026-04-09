# Practical: Build a Simple Library System

## Goal
Practice class design, encapsulation, and composition by modeling a small library.

## Requirements
Implement the following classes:

### 1. `Book`
- Attributes: `title`, `author`, `isbn`
- `__repr__` should show title and isbn

### 2. `Member`
- Attributes: `name`, `member_id`
- Tracks borrowed books (list of `Book` objects)
- Method: `borrow(book)` adds a book
- Method: `return_book(isbn)` removes a book by isbn

### 3. `Library`
- Holds a catalog (list of `Book`)
- Holds members (list of `Member`)
- Method: `add_book(book)`
- Method: `register(member)`
- Method: `lend(isbn, member_id)`
    - Finds the book and member
    - Removes the book from catalog
    - Adds the book to member
- Method: `accept_return(isbn, member_id)`
    - Removes the book from member
    - Adds the book back to catalog

## Stretch Goals
1. Use `@property` to prevent setting empty titles.
2. Add a `@classmethod` to `Book` that builds from a dict.
3. Add a `@dataclass` version of `Book` and compare with manual class.

## Suggested File
Create a file named `library.py` and implement the classes. Then run a few manual tests at the bottom of the file.
