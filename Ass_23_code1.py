class BookStore:
    NoOfBooks = 0

    def __init__(self):
        self.BookName = input("Enter Name of the Book : ")
        self.AuthorName = input(f"Enter name of Author : ")

        if(self.BookName == None or self.AuthorName == None):
            print("Enter BookName and Authorname First")
        else:
            BookStore.NoOfBooks += 1

    def Display(self):
        print(f"{self.BookName} by {self.AuthorName}. No of Books : {self.NoOfBooks}")

obj1 = BookStore()

obj1.Display()

obj2 = BookStore()

obj2.Display()