import random


class Book_Store:
    def __init__(self, name, author, page_number, ISNB):
        self.name = name
        self.author = author
        self.pages = page_number
        self.ISNB = ISNB

    material = 'paper'
    text_on_pages = True
    #    ISNB = random.Random[122143256982425435, 12215325698425435]
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
