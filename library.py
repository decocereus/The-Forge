fname = open("library_books.txt")
available_books = []
for line in fname:
    line = line.strip()
    available_books.append(line)

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

def add_and_choose_books():
    books = []
    for b in available_books:
        books.append(b)

    for book in books:
        print(book)
        print('Do you want this book ? yes or no')
        answer = input('')
        answer.lower()
        if answer[0] == 'y':

            return print('You rented',book,'successfully')

        else:   continue

add_and_choose_books()
