class Book:
    material = 'paper'
    text = True

    def __init__(self, book_name, author, pages, isbn):
        self.book_name = book_name
        self.author = author
        self.pages = pages
        self.isbn = isbn
        self.reserved = False


book1 = Book('Scar Tissues', 'Kidis', 500, 101)
book2 = Book('Acid for the children', 'Balsary', 400, 102)
book3 = Book('Electrify my life', 'Balamy', 500, 103)
book4 = Book('Viva Coldplay!', 'Roach', 300, 104)
book5 = Book('Electroshock', 'Garnier', 200, 105)

book1.reserved = True

books = [book1, book2, book3, book4, book5]

for book in books:
    if book.reserved:
        print(f'Name:{book.book_name}, Author:{book.author}, pages:{book.pages}, material:{book.material}, is reserved')
    else:
        print(f'Name:{book.book_name}, Author:{book.author}, pages:{book.pages}, material:{book.material}')


class SchoolBook(Book):

    def __init__(self, book_name, author, pages, isbn, subject, clas, homework):
        super().__init__(book_name, author, pages, isbn)
        self.subject = subject
        self.clas = clas
        self.homework = homework
        self.reserved = False


sbook1 = SchoolBook('Algebra', 'Ivanov', 500, 105, 'Maths', 10, True)
sbook2 = SchoolBook('Geometry', 'Petrov', 400, 106, 'Maths', 9, False)

sbook1.reserved = True

sbooks = [sbook1, sbook2]

for sbook in sbooks:
    if sbook.reserved:
        print(
            f'Name:{sbook.book_name}, Author:{sbook.author}, pages:{sbook.pages}, '
            f'subject:{sbook.subject}, clas:{sbook.clas} is reserved'
        )
    else:
        print(
            f'Name:{sbook.book_name}, Author:{sbook.author}, pages:{sbook.pages}, '
            f'material:{sbook.material}, clas:{sbook.clas}'
        )
