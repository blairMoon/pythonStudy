class Library:

    def __init__(self, name):
        self.name = name 
        self.book_list = [] 

    def add(self, book):
        self.book_list.append(book)

    def remove(self, book):
        try:
            self.book_list.remove(book)
        except:
            print("제거할 책이 없습니다.")

    def info(self):
        for book in self.book_list:
            print(book) 
        
class Book:

    def __init__(self, title, location):
        self.title = title
        self.location = location 
    
    def __str__(self):
        return self.title

    def is_borrowed(self):
        self.title = input()
        if self.title in self.book_list:
            return "Library"
        else:
            return "User"    


book1 = Book("A", "1st floor")
book2 = Book("B", "2nd floor")

hyu_library = Library("hanyang")

hyu_library.add(book1)
hyu_library.info()

hyu_library.add(book2)
hyu_library.info()

hyu_library.remove("A")
hyu_library.info()
        
