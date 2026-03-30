# Day 4 - Mini Project: Library Management System
# Combines classes, inheritance, and magic methods!

class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.borrowed = 0

    def available_copies(self):
        return self.copies - self.borrowed

    def checkout(self):
        if self.available_copies() > 0:
            self.borrowed += 1
            return True
        return False

    def return_book(self):
        if self.borrowed > 0:
            self.borrowed -= 1

    def __str__(self):
        return f"{self.title} by {self.author} ({self.available_copies()} available)"


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.checkout():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        return f"Member: {self.name} (ID: {self.member_id})"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"  Added: {book.title}")

    def register_member(self, member):
        self.members.append(member)
        print(f"  Registered: {member.name}")

    def list_books(self):
        print(f"\n=== {self.name} - Books ===")
        if not self.books:
            print("  No books in library")
            return
        for i, book in enumerate(self.books, 1):
            status = f"{book.available_copies()}/{book.copies} available"
            print(f"  {i}. {book.title} by {book.author} [{status}]")

    def list_members(self):
        print(f"\n=== Members ===")
        if not self.members:
            print("  No members registered")
            return
        for member in self.members:
            borrowed = len(member.borrowed_books)
            print(f"  {member.member_id}: {member.name} ({borrowed} books borrowed)")

    def find_book(self, title):
        for book in self.books:
            if title.lower() in book.title.lower():
                return book
        return None

    def find_member(self, name):
        for member in self.members:
            if name.lower() in member.name.lower():
                return member
        return None


# ============================================================
# Main Program
# ============================================================
library = Library("City Library")

# Seed some data
library.add_book(Book("Python Crash Course", "Eric Matthes", "123", 3))
library.add_book(Book("Django for APIs", "William Vincent", "456", 2))
library.add_book(Book("Clean Code", "Robert Martin", "789", 1))

alice = Member("Alice Johnson", "M001")
bob = Member("Bob Smith", "M002")
library.register_member(alice)
library.register_member(bob)

print()

# Menu loop
while True:
    print("\n--- Library Menu ---")
    print("1. List books")
    print("2. List members")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Add a book")
    print("6. Register member")
    print("7. Exit")

    choice = input("\nEnter choice (1-7): ")

    if choice == "1":
        library.list_books()

    elif choice == "2":
        library.list_members()

    elif choice == "3":
        member_name = input("Member name: ")
        member = library.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found")
            continue

        library.list_books()
        book_title = input("Book title: ")
        book = library.find_book(book_title)

        if not book:
            print(f"Book '{book_title}' not found")
        elif member.borrow_book(book):
            print(f"  {member.name} borrowed '{book.title}'")
        else:
            print(f"  No copies available for '{book.title}'")

    elif choice == "4":
        member_name = input("Member name: ")
        member = library.find_member(member_name)
        if not member:
            print(f"Member '{member_name}' not found")
            continue

        if not member.borrowed_books:
            print(f"  {member.name} has no borrowed books")
            continue

        print(f"  {member.name}'s books:")
        for i, book in enumerate(member.borrowed_books, 1):
            print(f"    {i}. {book.title}")

        book_title = input("Book title to return: ")
        book = library.find_book(book_title)

        if book and member.return_book(book):
            print(f"  {member.name} returned '{book.title}'")
        else:
            print("  Could not return that book")

    elif choice == "5":
        title = input("Title: ")
        author = input("Author: ")
        isbn = input("ISBN: ")
        copies = int(input("Copies: "))
        library.add_book(Book(title, author, isbn, copies))

    elif choice == "6":
        name = input("Name: ")
        member_id = input("Member ID: ")
        library.register_member(Member(name, member_id))

    elif choice == "7":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")

# BONUS: Add overdue tracking with dates
# BONUS: Add a search by author feature
# BONUS: Export/import library data to a file
