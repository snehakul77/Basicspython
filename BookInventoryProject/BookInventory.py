#WAP You’re managing a bookstore, and you want to keep track of books and their details such as:
#Book title, author, Price and Quantity

#Display all the books in stock with their details.
#Calculate the total value of the inventory.
#Find the most expensive book and the least expensive book in the store.
#Sort books by price.

books_inventory = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "price": 18.99, "quantity": 10},
    {"title": "1984", "author": "George Orwell", "price": 15.99, "quantity": 8},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "price": 12.99, "quantity": 15},
    {"title": "Moby Dick", "author": "Herman Melville", "price": 22.50, "quantity": 5},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "price": 9.99, "quantity": 20}
]

def calculate_inventory(books):
    total = 0
    for book in books_inventory:
        total += book["price"] * book["quantity"]
    return total

def findmax_leastexpensive(books):
    most_exp = max(books, key=lambda book: book["price"])
    leastexpensive = min(books, key=lambda book: book["price"])
    return most_exp, leastexpensive

def displaybookdetails(books):
    print(f"Title: {books['title']}")
    print(f"Author: {books['author']}")
    print(f"Price: {books['price']:.2f}")
    print(f"Quantity: {books['quantity']}")
    print("----"*30)

def sortbooks(books):
    return sorted(books, key=lambda book: book["price"])

print("Books Inventory")

for book in books_inventory:
    displaybookdetails(book)

inventoryvalue = calculate_inventory(books_inventory)
print(f"Total Inventory: {inventoryvalue:.2f}")

mostexpensive , leastexpensive = findmax_leastexpensive(books_inventory)
print(f"Most Expensive: {mostexpensive["price"]:.2f}")
print(f"LeastExpensive: {leastexpensive["price"]:.2f}")
print("----"*30)
print("Sorted book lists")
sortbooks = sortbooks(books_inventory)
for book in sortbooks:
    print(f"{book['title']} -> {book['price']:.2f}")

