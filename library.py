class Library:
    def __init__(self, name, author, is_available=True):
        self.name = name
        self.author = author
        self.is_available = is_available

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"{self.name} by {self.author} is issued.")
        else:
            print(f"Sorry, {self.name} is not available right now.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"{self.name} has been returned.")
        else:
            print(f"{self.name} was already in the library.")

    def show_status(self):
        if self.is_available:
            print(f"{self.name} by {self.author} -> Available")
        else:
            print(f"{self.name} by {self.author} -> Issued")


if __name__ == "__main__":

    books = [
        Library("1984", "George Orwell"),
        Library("To Kill a Mockingbird", "Harper Lee"),
        Library("The Great Gatsby", "F. Scott Fitzgerald")
    ]

    while True:
        print("\n--- Library Menu ---")
        print("1. Show all books")
        print("2. Issue a book")
        print("3. Return a book")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nBook List:")
            for b in books:
                b.show_status()

        elif choice == "2":
            name = input("Enter book name: ")
            found = False

            for b in books:
                if b.name.lower() == name.lower():
                    b.check_out()
                    found = True
                    break

            if not found:
                print("Book not found.")

        elif choice == "3":
            name = input("Enter book name: ")
            found = False

            for b in books:
                if b.name.lower() == name.lower():
                    b.return_book()
                    found = True
                    break

            if not found:
                print("Book not found.")

        elif choice == "4":
            print("Thank you! Exiting...")
            break

        else:
            print("Wrong choice, try again.")