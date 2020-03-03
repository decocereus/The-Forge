
lastname = []
hoursWorked = []
hourlyWage = []

fname = open("yoo.pdf")
rawData = []
for line in fname:
    line = line.strip()
    rawData.append(line)

def store_data_in_table():
    for i in raw:
        lastname.append(i)
        hoursWorked.append(i)
        hourlyWage.append(i)

def printData():
    print(lastname)
    print(hoursWorked)
    print(hourlyWage)

def specificUser(userName = input("Enter the username: ")):
    if userName in lastname:
        printData()



store_data_in_table()
printData()
specificUser()
