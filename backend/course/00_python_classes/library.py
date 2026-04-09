class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title={self.title!r}, isbn={self.isbn!r})"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed = []

    def borrow(self, book):
        self.borrowed.append(book)

    def return_book(self, isbn):
        for i, book in enumerate(self.borrowed):
            if book.isbn == isbn:
                return self.borrowed.pop(i)
        return None


class Library:
    def __init__(self):
        self.catalog = []
        self.members = []

    def add_book(self, book):
        self.catalog.append(book)

    def register(self, member):
        self.members.append(member)

    def lend(self, isbn, member_id):
        book = self._find_book(isbn)
        member = self._find_member(member_id)
        if book and member:
            self.catalog.remove(book)
            member.borrow(book)
            return True
        return False

    def accept_return(self, isbn, member_id):
        member = self._find_member(member_id)
        if not member:
            return False
        book = member.return_book(isbn)
        if book:
            self.catalog.append(book)
            return True
        return False

    def _find_book(self, isbn):
        for book in self.catalog:
            if book.isbn == isbn:
                return book
        return None

    def _find_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None


if __name__ == "__main__":
    lib = Library()
    lib.add_book(Book("Clean Code", "Robert C. Martin", "9780132350884"))
    lib.add_book(Book("Python Tricks", "Dan Bader", "9781775093305"))

    alice = Member("Alice", "M001")
    lib.register(alice)

    print("Lend:", lib.lend("9780132350884", "M001"))
    print("Borrowed:", alice.borrowed)
    print("Return:", lib.accept_return("9780132350884", "M001"))
    print("Catalog:", lib.catalog)
