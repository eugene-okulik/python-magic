from homework.irina_elfimova.homework_10.hmw_10_1 import Book_Store


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
