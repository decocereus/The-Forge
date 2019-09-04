# I want list of books
# I want people to enter their own info and then be able to rent out a book
fname = open("library_books.txt")
availabe_books = []
for line in fname:
    line = line.strip()
    availabe_books.append(line)

class people:
    def __init__(self, name, age, phone_number):
        self.name = name
        self.age = age
        self.phone_number = phone_number

print("Please register for the library.")

while True:
    members= {}
    try:
        member = people(input("Name: "),int(input("Age: ")),int(input("Mobile Number: ")))
    except:
        print('Please enter valid information')
        continue
    members[member] = members.get(member,0) + 1
    if member in members:
        break
    else:
        continue

class choose_book:
    def __init__(self, book_name, choice):
        self.book_name = book_name
        self.choice = choice

books = [
    choose_book(availabe_books[0],"1"),
    choose_book(availabe_books[1],"2"),
    choose_book(availabe_books[2],"3"),
    choose_book(availabe_books[3],"4"),
    choose_book(availabe_books[4],"5"),
    choose_book(availabe_books[5],"6"),
    choose_book(availabe_books[6],"7"),
    choose_book(availabe_books[7],"8")
]

def choosing_book(books):
    counter = 0
    for book in books:
        counter += 1
        print(counter,end=". ")
        user_book = input(book.book_name)
        print()
        if user_book == book.choice:
            return print("You successfully rented your book")

choosing_book(books)
