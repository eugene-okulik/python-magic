class Book:
    material_pages = 'бумага'
    presence_of_text = True

    def __init__(self, title, author, number_pages, isbn, reserved=False):
        self.title = title
        self.author = author
        self.number_pages = number_pages
        self.isbn = isbn
        self.reserved = reserved
        self.print_book = self.reserved_print

    def reserved_print(book):
        if book.reserved:
            return (f'Название: {book.title}, Автор: {book.author},'
                    f' страниц: {book.number_pages}, материал: {book.material_pages}, зарезервирована')
        else:
            return (f'Название: {book.title}, Автор: {book.author},'
                    f' страниц: {book.number_pages}, материал: {book.material_pages}')


book1 = Book(title="Цель", author="Элияху Голдратт", number_pages=486, isbn="985-483-216-3")
book2 = Book(title="Красная таблетка", author="Андрей Курпатов", number_pages=352, isbn="978-5-906940-62-9")
book3 = Book(title="1984", author="Джордж Оруэлл", number_pages=352, isbn="978-5-389-19109-9")
book4 = Book(title="Атлант расправил плечи", author="Айн Рэнд", number_pages=1394, isbn="5-9614-0362-9")
book5 = Book(title="Женщины", author="Чарльз Буковски", number_pages=432, isbn="978-5-699-37887-6")

book5.reserved = True

print(book1.print_book())
print(book2.print_book())
print(book3.print_book())
print(book4.print_book())
print(book5.print_book())


class Textbook(Book):

    def __init__(self, subject, level, exercises, title, author, number_pages, isbn):
        super().__init__(title, author, number_pages, isbn)
        self.subject = subject
        self.level = level
        self.exercises = exercises
        self.print_textbook = self.reserved_print_textbook

    def reserved_print_textbook(textbook):
        if textbook.reserved:
            return (f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.number_pages},'
                    f' предмет: {textbook.material_pages}, класс: {textbook.level}, зарезервирована')

        else:
            return (f'Название: {textbook.title}, Автор: {textbook.author}, страниц: {textbook.number_pages},'
                    f' предмет: {textbook.material_pages}, класс: {textbook.level}')


textbook_1 = Textbook(
    'Математика', 1, True, 'Математика. 1 класс. Учебник',
    'Волкова', 128, '9785091024593'
)
textbook_2 = Textbook(
    'Русский язык', 2, True, 'Русский язык. 2 класс. Учебник',
    'Смирнова', 234, '9785231024593'
)
textbook_3 = Textbook(
    'Биология', 3, True, 'Биология. 3 класс. Учебник',
    'Амарян', 178, '9785091024223'
)
textbook_4 = Textbook(
    'Физика', 4, True, 'Физика. 4 класс. Учебник',
    'Славик', 230, '9785091024593'
)
textbook_5 = Textbook(
    'Информатика', 5, True, 'Информатика. 5 класс. Учебник',
    'Маск', 430, '9085091024593'
)

textbook_3.reserved = True

print(textbook_1.print_textbook())
print(textbook_2.print_textbook())
print(textbook_3.print_textbook())
print(textbook_4.print_textbook())
print(textbook_5.print_textbook())
