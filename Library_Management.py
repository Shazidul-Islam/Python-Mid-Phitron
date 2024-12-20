class Library:
    book_catalog = []

    def add_book(self, book):
        Library.book_catalog.append(book)
        print(f"Book '{book._book_title}' added to the library.")

class Book:
    def __init__(self, b_id, book_title, b_author, is_available=True):
        self._b_id = b_id
        self._book_title = book_title
        self._b_author = b_author
        self._is_available = is_available

    def borrow_book(self):
        if self._is_available:
            self._is_available = False
            print(f"Successfully borrowed the book '{self._book_title}'.")
        else:
            print(f"Book '{self._book_title}' is already borrowed.")

    def return_book(self):
        if not self._is_available:
            self._is_available = True
            print(f"'{self._book_title}' returned successfully.")
        else:
            print(f"'{self._book_title}' is not borrowed.")

    def view_book_info(self):
        availability_status = "Available" if self._is_available else "Not Available"
        print(f"Book ID: {self._b_id}, Title: {self._book_title}, Author: {self._b_author}, Status: {availability_status}")

library = Library()
book1 = Book(201, "Introduction to Python", "Guido van Rossum")
book2 = Book(202, "Artificial Intelligence Basics", "John McCarthy")
book3 = Book(203, "Data Structures and Algorithms", "Donald Knuth")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

def menu():
    while True:
        print("\nMenu:")
        print("1. View All Books")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. Exit")
        
        try:
            n = int(input("Enter your choice: "))
            
            if n == 1:
                if Library.book_catalog:
                    print("Displaying all books in the library:")
                    for book in Library.book_catalog:
                        book.view_book_info()
                else:
                    print("The library currently has no books available.")
            
            elif n == 2:
                b_id = int(input("Enter the Book ID to borrow: "))
                found = False
                for book in Library.book_catalog:
                    if book._b_id == b_id:
                        book.borrow_book()
                        found = True
                        break
                if not found:
                    print("The entered Book ID does not exist in the library.")
            
            elif n == 3:
                b_id = int(input("Enter the Book ID to return: "))
                found = False
                for book in Library.book_catalog:
                    if book._b_id == b_id:
                        book.return_book()
                        found = True
                        break
                if not found:
                    print("The entered Book ID does not exist in the library.")
            
            elif n == 4:
                print("Thank you for using the library system. Goodbye!")
                break
            
            else:
                print("Invalid selection. Please choose a valid option from the menu.")
        
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

menu()
