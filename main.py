database = {}
taken = {}
while True:
    command = input("What would you want to do? (Write help for command list) ")
    if command == "help" or command == "-h":
        print(" \t [add book] \t | [-a] | \t [adds a new book to the system] \n \
        [find book] \t | [-f] | \t  [this command finds a book at the system] \n \
        [list an author’s books] \t | [-la] | \t [finds the books of an author which are in the system] \n \
        [take book] \t | [-t] | \t [give a book to someone] \n \
        [return book] \t | [-r] | \t [returns a book which have taken by someone] \n \
        [list books] \t | [-l] | \t [lists every book in the system] \n \
        [list taken books] \t | [-lt] | \t [lists every taken book in the system] \n \
        [list books before/after year] \t | [-ly] | \t [lists every book in the system with given dates] \n \
        [help] \t | [-h] | \t [prints all commands and their descriptions] \n \
        [quit] \t | [-q] | \t [quits program]")

    if command == "add book" or command == "-a":
        bookName = input("Please enter the book's name: ")
        bookNum = input(str("Please enter the book's number: "))
        bookCat = input("Please enter the book's category: ")
        bookPlac = input("Please enter the book's placement: ")
        bookAuth = input("Please enter the book's author: ")
        bookDate = input("Please enter the book's publishment year: ")
        bookTaken = "Book isn't taken."
        if bookName != "" and bookNum != "" and bookCat != "" and bookPlac != "" and bookAuth != "" and bookDate != "":
            if bookDate.isnumeric():
                a = []
                a.append(bookTaken)
                a.append(bookName)
                a.append(bookNum)
                a.append(bookCat)
                a.append(bookPlac)
                a.append(bookAuth)
                a.append(bookDate)
                database[bookName] = a
                print("[" + bookName + "] has added to the system.")
            else:
                print("Can not add book to the system. Improper parameter(s).")
        else:
            print("Can not add book to the system. Missing parameter(s).")

    if command == "find book" or command == "-f":
        findName = input("Please enter the book's name: ")
        findNum = input("Please enter the book's number: ")
        if findName == "" or findNum == "":
            print("Can not find book. Missing parameter(s).")
        else:
            if findName in database.keys() and (database[findName])[1] == findNum:
                for x in range(0,6):
                    print("[" + str((database[findName])[x]) + "]", end="")
                print("")
            else:
                print("Can not find book. Missing parameter(s).")

    if command == "list an author's books" or command == "-la":
        listAuth = input("Please enter the author's name: ")
        if listAuth == "":
            print("Can not list book(s). Missing parameter(s).")
        else:
            for i in database.keys():
                if listAuth in database[i]:
                    print("[" + (database[i])[1] + "] " + "[" + (database[i])[2] + "]")

    if command == "take book" or command == "-t":
        takeName = input("Please enter the name of the book that you want to take: ")
        takeNum = input("Please enter the number of the book that you want to take: ")
        personId = input("PLease enter your id: ")
        if takeName != "" and takeNum != "" and personId != "":
            if takeName in database.keys():
                if database[takeName][0] == "Book isn't taken.":
                    database[takeName][0] = "Book is taken."
                    u = []
                    u.append(takeName)
                    u.append(takeNum)
                    u.append(personId)
                    taken[takeName] = u
                    print("[" + takeName + "] has given with no problem.")
                else:
                    print("Can not give book. Someone has already taken it.")
            else:
                print("Can not give book. There is no book like this in this system.")
        else:
            print("Can not give book. Missing parameter(s).")

    if command == "return book" or command == "-r":
        retName = input("Please enter the name of the book that you want to return: ")
        retNum = input("Please enter the number of the book that you want to return: ")
        if retName != "" and retNum != "":
            if retName in database.keys():
                if (database[retName])[0] == "Book isn't taken.":
                    print("Can not return book. It has not been taken by anyone.")
                else:
                    database[retName][0] = "Book isn't taken."
                    del taken[retName]
                    print("[" + retName + "] has been returned.")

            else:
                print("Can not return book. There is no book like this in this system.")
        else:
            print("Can not return book(s). Missing parameter(s).")

    if command == "list books" or command == "-l":
        for collab in database.values():
            print("[" + collab[1] + "] [" + collab[2] + "]")

    if command == "list taken books" or command == "-lt":
        for take in taken.values():
            print("[" + take[0] + "] [" + take[1] + "] [" + take[2] + "]")

    if command == "list books before/after year" or command == "-ly":
        year = input("Please enter the year that you want to question: ")
        befaf = input("Do you want to question before that year or after that year (type before or after): ")
        if year == "" or befaf == "":
            print("Can not list book(s). Missing parameter(s).")
        elif year.isnumeric():
            check = []
            for q in database.values():
                if befaf == "before":
                    if int(year) >= int(q[-1]):
                        check.append(q)
                if befaf == "after":
                    if int(year) < int(q[-1]):
                        check.append(q)
            for i in check:
                print("[" + str(i[1]) + "] [" + str(i[2]) + "]")
        else:
            print("Can not list book(s). Improper input.")

    if command not in ["add book", "-a", "find book", "-f", "list an author’s books", "-la", "take book", "-t", "return book", "-r", "list book", "-l", "list taken books", "-lt", "quit", "-q", "help", "-h"]:
        print("You have entered a command that does not exist. Write ‘help’ to get to know commands.")

    if command == "quit" or command == "-q":
        print("See you later :)")
        break