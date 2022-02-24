class Library:
    def __init__(self, list, name):
        self.booksList = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print("We Had Following Books In Our Library: {self.name}")

        for book in self.booksList:
            print(book)

    def lendBook(self, user, book):
        if book not in self.lendDict.keys():
            self.lendDict.update({book: user})
            print("Lender-Book Database Has Been Updated. You Can Take Book Now")
        else:
            print(f"Book Is already Being Used By {self.lendDict[book]}")

    def addBook(self, book):
        self.booksList.append(book)
        print("Book Is Updated To Book List")

    def returnBook(self, book):
        self.lendDict.pop(book)


if __name__ == '__main__':
    tyro = Library(['Python', 'Java', 'Js', 'C++', 'C-lang', 'Php'], "CODETyro")

    while (True):
        print(f"Welcome To The {tyro.name} library. Enter Your Choice TO Continue")

        print("1. Display Books")
        print("2. Lend A Book")
        print("3. Add A Book")
        print("4. Return A Book")

        user_choice = input()

        if user_choice not in ['1', '2', '3', '4']:
            print("Please Enter A Valid Option....!!")
            continue

        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            tyro.displayBooks()

        elif user_choice == 2:
            book = input("Enter The Name Of The Book You Want To Lend: ")
            user = input("Enter Your Name")
            tyro.lendBook(user, book)


        elif user_choice == 3:
            book = input("Enter The Name Of The Book You Want To Add: ")
            tyro.addBook(book)

        elif user_choice == 4:
            book = input("Enter The Name Of The Book You Want To Return: ")
            tyro.returnBook(book)

        else:
            print("Not A Valid Option..!!")

        print("Press Q To Quit And C To Continue")

        user_choice2 = " "

        while user_choice2 != "C" and user_choice2 != "Q":

            user_choice2 = input()

            if user_choice2 == 'Q':
                exit()

            if user_choice2 == 'C':
                continue
