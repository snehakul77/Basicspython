books = [
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "genre": "Fantasy", "pages": 310},
    {"title": "1984", "author": "George Orwell", "genre": "Dystopian", "pages": 328},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "genre": "Classic", "pages": 281},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genre": "Classic", "pages": 180},
    {"title": "Brave New World", "author": "Aldous Huxley", "genre": "Dystopian", "pages": 268},
    {"title": "Harry Potter", "author": "J.K. Rowling", "genre": "Fantasy", "pages": 309}
]
#-------------------------
##Filter and print books that have less than 300 pages.
sort_books = sorted(books, key=lambda book:book["pages"] )
print("----Sorting booking by number of pages----")
for book in sort_books:
    if book["pages"] < 300:
        print(f"{book['title']} {book['author']} {book['pages']}")
#---------------------------
#Group the books by genre
#book_genre = {}
#for book in books:
#    genre = book["genre"]
#    title = book["title"]
#    if genre not in book_genre:
#        book_genre[genre] = []
#    book_genre[genre].append(title)
#    #print(book_genre)

#for genre in book_genre:
#    print(genre, book_genre[genre])
#--------------------------
#Find the book with the most pages.

#max_book =max(books, key=lambda book:book["pages"])
#print(max_book["title"])

#---------------------------
# List all authors alphabetically (no duplicates).
#sort_author = sorted(books, key=lambda book:book["author"])
#for book in sort_author:
#    print(book["author"])

#----------------------------





