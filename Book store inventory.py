import csv
import os

def load_books(filename='books.csv'):
    """Load books from CSV file"""
    if not os.path.exists(filename):
        return []
    
    books = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)  
        for row in reader:
            if row:  
                books.append(row)
    return books

def save_books(books, filename='books.csv'):
    """Save books to CSV file"""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'ISBN', 'Genre', 'Price', 'Quantity'])
        writer.writerows(books)

def add_book(books):
    """Add a new book"""
    print("\n--- Add New Book ---")
    
    # Input validations
    title = input("Enter book title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return books
    
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN: ").strip()
    
    #  duplicate ISBN
    if any(book[2] == isbn for book in books):
        print("A book with this ISBN already exists!")
        return books
    
    genre = input("Enter genre: ").strip()
    
    # Price 
    while True:
        try:
            price = float(input("Enter price: "))
            if price <= 0:
                print("Price must be a positive number!")
                continue
            break
        except ValueError:
            print("Invalid price. Please enter a number.")
    
    # Quantity 
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity < 0:
                print("Quantity cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
    
    # Add book
    new_book = [title, author, isbn, genre, str(price), str(quantity)]
    books.append(new_book)
    print("Book added successfully!")
    return books

def view_books(books):
    """View all books"""
    if not books:
        print("No books in the inventory.")
        return
    
    print("\n--- Book Inventory ---")
    print("{:<30} {:<20} {:<15} {:<15} {:<10} {:<10}".format(
        "Title", "Author", "ISBN", "Genre", "Price", "Quantity"
    ))
    print("-" * 110)
    
    for book in books:
        print("{:<30} {:<20} {:<15} {:<15} ${:<9} {:<10}".format(
            book[0], book[1], book[2], book[3], book[4], book[5]
        ))

def remove_book(books):
    """Remove a book by ISBN"""
    isbn = input("Enter ISBN of the book to remove: ").strip()
    
    for book in books[:]:  
        if book[2] == isbn:
            books.remove(book)
            print("Book removed successfully!")
            return books
    
    print("No book found with this ISBN.")
    return books

def main():
    """Main menu and program flow"""
    # Load  books
    books = load_books()
    
    while True:
        print("\n--- Book Store Management System ---")
        print("1. Add Book")
        print("2. View Books")
        print("3. Remove Book")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            books = add_book(books)
            save_books(books)
        elif choice == '2':
            view_books(books)
        elif choice == '3':
            books = remove_book(books)
            save_books(books)
        elif choice == '4':
            save_books(books)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()