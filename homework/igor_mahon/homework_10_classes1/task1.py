# Библиотека
# Первый класс
# Создайте класс book с атрибутами:
# материал страниц
# наличие текста
# название книги
# автор
# кол-во страниц
# ISBN
# флаг зарезервирована ли книга или нет (True/False).
# Какие-то из атрибутов будут общими для всех книг (материал, наличие текста), какие-то индивидуальными.
# Создайте несколько (штук 5) экземпляров разных книг.
# После создания пометьте одну книгу как зарезервированную.
# Распечатайте детали о каждой книге в таком виде:
# Если книга зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500, материал: бумага, зарезервирована
# если не зарезервирована:
# Название: Идиот, Автор: Достоевский, страниц: 500,  материал: бумага


class Book:
    def __init__(self, name, author, number_pages, reserved, isbn):
        self.name = name
        self.author = author
        self.pages = number_pages
        self.isbn = isbn
        self.reserved = reserved

    material = 'бумага'
    text_on_pages = 'Да'

    def is_booked(self):
        if self.reserved:
            return ', зарезервирована'
        else:
            return ''


book1 = Book('Горе от ума том1', 'Грибоедов', 100, False, 5435435345345)
book2 = Book('Горе от ума том2', 'Грибоедов', 100, True, 4234324234232)
book3 = Book('Идиот том1', 'Достоевский', 500, False, 4563346456465)
book4 = Book('Идиот том2', 'Достоевский', 500, False, 3123123123123)
book5 = Book('Идиот том3', 'Достоевский', 500, False, 3645645345343)


for book in [book1, book2, book3, book4, book5]:
    print("Название: ", book.name, ", Автор: ", book.author, ", страниц: ", book.pages,
          ", материал: ", book.material, book.is_booked(), sep='')


# Второй класс
# Создайте дочерний класс для первого. Это будет класс для школьных учебников. В нем будут дополнительные атрибуты:
#
# предмет (типа математика, история, география),
# класс (школьный класс, для которого этот учебник)(осторожно с названием переменной. class - зарезервированное слово),
# наличие заданий (bool)
# Создайте несколько экземпляров учебников.
# После создания пометьте один учебник как зарезервированный.
# Распечатайте детали о каждом учебнике в таком виде: Если учебник зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9, зарезервирована
# если не зарезервирован:
#
# Название: Алгебра, Автор: Иванов, страниц: 200, предмет: Математика, класс: 9


class SchoolBooks(Book):
    def __init__(self, name, author, number_pages, reserved, isbn, subject, grade, homework):
        super().__init__(name, author, number_pages, reserved, isbn)
        self.subject = subject
        self.grade = grade
        self.homework = homework


school_book1 = SchoolBooks('Алгебра ч1', 'Петров', 20, True, 4324243234234, 'Математика', 11, False)
school_book2 = SchoolBooks('Алгебра ч2', 'Петров', 30, False, 2342342543543, 'Математика', 11, True)
school_book3 = SchoolBooks('Геометрия', 'Иванов', 40, False, 2423442453645, 'Математика', 10, True)
school_book4 = SchoolBooks('Термодинамика', 'Морозов', 100, False, 5654645646464, 'Физика', 10, False)

for book in [school_book1, school_book2, school_book3, school_book4]:
    print("Название: ", book.name, ", Автор: ", book.author, ", страниц: ", book.pages,
          ", предмет: ", book.subject, ", класс: ", book.grade, book.is_booked(), sep='')
