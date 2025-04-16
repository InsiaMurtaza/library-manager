import json
import os

data_file = 'library.txt'

def load_library():
    if os.path.exists(data_file):
        with open(data_file,'r') as file:
            return json.load(file)
    return[]

def save_library(library):
    with open(data_file,'w') as file:
        json.dump(library,file)

def add_book(library):
    title = input('Enter the title of the book: ').lower()
    author = input('Enter the author of the book: ').lower()
    year = input('Enter the year in which the book is published: ')
    genre = input('Enter the genre of the book: ')
    read = input('Have you read the book(yes/no): ').lower() == 'yes'

    new_book = {
        'title': title,
        'author':author,
        'year':year,
        'genre':genre,
        'read': read
    }
    library.append(new_book)
    save_library(library)
    print(f"Book {title} added successfully.")

def remove_book(library):
    title = input("Enter the title of the book you want to remove: ")
    initial_countofbooks = len(library)
    library = [book for book in library if book['title'].lower() != title]
    if len(library) < initial_countofbooks:
        save_library(library)
        print(f"{title} is removed successfully!")
    else: 
        print("Sorry! Cannot found any book of this title...")

def search_book(library):
    title_or_author = input("Select by which key you want to search the book (title or author): ")
    search_by = input(f"Enter the {title_or_author} of the book: ")
    result = [book for book in library if search_by.lower() in book[title_or_author]]
    if result:
        for book in result:
            status = "Read" if book['read'] else "Not Read"
            print(f"""This book is available
                Title: {book['title']}
                Author: {book['author']}
                Year in which published: {book['year']}
                Genre: {book['genre']}
                Read or not: {status}""")
    else:
        print(f"No book found matching {title_or_author} in library!")

def display_all_books(library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Not Read"
            print(f"""Title: {book['title']}
                Author: {book['author']}
                Year in which published: {book['year']}
                Genre: {book['genre']}
                Read or not: {status}""")
    else:
        print("Oops! The Library is empty!!!")

def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])
    percentage_books_read = (read_books/total_books) * 100 if total_books > 0 else 0

    print(f"Total Books: {total_books}")
    print(f"Percentage of Books read: {percentage_books_read:.2f}%")

def main():
    library = load_library()
    while True:
        print(f"""***Welcome to The Library Manager***
              Menu:
              1. Add Book
              2. Remove Book
              3. Search Book
              4. Display All Books
              5. Display Statistics
              6. Exit""")
        
        choice = input("Enter the number of the options from above: ")
        if choice == '1':
            add_book(library)
        elif choice == '2':
            remove_book(library)
        elif choice == '3':
            search_book(library)
        elif choice == '4':
            display_all_books(library)
        elif choice == '5':
            display_statistics(library)
        elif choice == '6':
            print("Thankyou for Visiting Our Library!")
            break
        else:
            print("Invalid number!!! Please enter the number of the options from above....")


if __name__ == '__main__':
    main()
