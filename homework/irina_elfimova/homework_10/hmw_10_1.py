import random


class Book_Store:
    def __init__(self, name, author, page_number, ISNB):
        self.name = name
        self.author = author
        self.pages = page_number
        self.ISNB = ISNB

    material = 'paper'
    text_on_pages = True
    reserved = False

    def is_reserved(self):
        if self.reserved:
            return ', reserved'
        else:
            return ''


book_1 = Book_Store('"1984"', 'George Orwell', 400, 312143256982425435)
book_2 = Book_Store('"The Great Gatsby"', 'F. Scott Fitzgerald', 250, 452143256982632535)
book_3 = Book_Store('"Harry Potter and the Sorcerers Stone"', 'J.K. Rowling', 600, 68216985982632535)
book_4 = Book_Store('"The Little Prince"', 'Antoine de Saint-Exupéry', 200, 652143256982429981)
book_5 = Book_Store('"Fahrenheit 451"', 'Ray Bradbury', 150, 37689585982632535)
book_5.reserved = True

for book in [book_1, book_2, book_3, book_4, book_5]:
    print("Title:", book.name, ',', "Author:", book.author, ',', "pages:", book.pages, ',',
          "material:", book.material, ',', "ISNB:", book.ISNB, ',', book.is_reserved())


class TextBooks(Book_Store):

    def __init__(
            self, name, author, page_number, ISNB, subject, grade
    ):
        super().__init__(name, author, page_number, ISNB)
        self.subject = subject
        self.grade = grade
        homework = True


book_6 = TextBooks('"Mental Math"', 'J.Smith', 100, 122143256982425435, 'Math', 'Second')
book_7 = TextBooks('"Spanish as a second language"', 'D.Carter', 60, 122143256982425435, 'Spanish', 'Third')
book_7.reserved = True
book_8 = TextBooks('"Big Science"', 'K.B.Baker', 150, 122143256982425435, 'Science', 'Seventh')
book_9 = TextBooks('"How to draw"', 'L.V.Garner', 45, 122143256982425435, 'Arts', 'First')
book_10 = TextBooks('"Upper Math"', 'M.Taylor', 250, 122143256982425435, 'Math', 'Tenth')

for textbook in [book_6, book_7, book_8, book_9, book_10]:
    print("Title:", textbook.name, ',', "Author:", textbook.author, ',', "Pages:", textbook.pages, ',',
          "Subject:", textbook.subject, "Grade:", textbook.grade, textbook.is_reserved())
