class Book:

    book_count=0  # 1 iteration:0  2 iteration: 1

    def __init__(self,title,author,copies):
        self.title=title
        self.author=author 
        self._copies=copies


        Book.book_count+=1
        self.no_of_books = Book.book_count


    @property
    def copies(self):       # self.copies=copies(setter)  self.copies(getter)
        return self._copies
    
    @copies.setter
    def copies(self,value):
        if value<0:
            raise ValueError("Negative copies cannot exist")
        self._copies=value
    
    def __str__(self): # print
        return(f"Book: {self.no_of_books}|Title: {self.title}  Author: {self.author} and Copies: {self.copies}")


class Library:

    def __init__(self):
        self.books=[]

    def add_book(self,title,author,copies):
        for book in self.books:
            if book.title==title:
                book.copies+=copies
                print("Book Already Exists, so adding the copies")
                return
            
        book=Book(title,author,copies)
        self.books.append(book)

    def view_books(self):
        if not self.books:
            print("No books Available")
            return
        for book in self.books:
            print(book)
        return

    def issue_book(self,title):
        for book in self.books:
            if book.title==title:
                book.copies-=1
                print("Book issued")
                return
            
            if book.copies==0:
                print("No copies Available")
                return
            
            if book.title!=title:
                print("No such book exists")
                return

    def return_book(self,title):
        for book in self.books:
            if book.title==title:
                book.copies+=1
                print("Book returned successfully")
                return

            if book.title!=title:
                 print("No such book exists")
                 return

    def remove_book(self,title):
        for book in self.books:
            if book.title==title:
                self.books.remove(book)
                return

    def save_data(self):
        if self.books==[]:
                print("No books added, so no data to save")
                return
        
        with open("data.txt","a") as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.copies} \n")
                
        print("Data Saved successfully")
        return
    
    def load_data(self):
        with open("data.txt","r") as file:
            content=file.read()
            if content=="":
                print("File is empty so no data to load")
                return
            
            elif content!="":
                total_books=[]
                total_books=content.split(",")
                print(f"The loaded content is: \n title: {total_books[0]} , author: {total_books[1]} and copies: {total_books[2]}")
                return


L=Library()
# L.save_data()

while True:
    print("Welcome to Library Management system")
    print("Choose any one option from below: ")
    print("1- Add book")
    print("2- View books")
    print("3- Issue book")
    print("4- Return book")
    print("5- Remove book")
    print("6- Save data")
    print("7- Load data")
    print("Type 'exit' to exit the program")

    choice=input("").strip().lower()
    if choice=="1":
        L.add_book(input("Title: "),input("Author: "),input("Copies: "))
    
    elif choice=="2":
        L.view_books()

    elif choice=="3":
        L.issue_book(input("Title: "))

    elif choice=="4":
        L.return_book(input("Title: "))
    
    elif choice=="5":
        L.remove_book(input("Title: "))

    elif choice=="6":
        L.save_data()

    elif choice=="7":
        L.load_data()

    elif choice=="exit":
        break

    else:
        print("Invalid choice")







# l=Library()
# l.add_book("Chemistry","rutherford",4)
# l.add_book("physics","newton",5)
# l.add_book("English","abc",4)
# print("Added a book")
# l.view_books()
# l.issue_book("abc")
# print("Again viewing books: ")
# l.view_books()
# l.return_book("abc")
# print("Again viewing books: ")
# l.view_books()
# l.save_data()


# l.issue_book("abc")
# l.add_book("abc","efg",4)
        