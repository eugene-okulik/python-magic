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
    def __init__(self, material, has_text, title, author, num_pages, isbn, is_reserved=False):
        self.material = material
        self.has_text = has_text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.isbn = isbn
        self.is_reserved = is_reserved

    def reserve(self):
        self.is_reserved = True

    def unreserve(self):
        self.is_reserved = False

    def print_details(self):
        if self.is_reserved:
            reserved_str = ', зарезервирована'
        else:
            reserved_str = ''

        print(
            f"Название: {self.title}, Автор: {self.author}, "
            f"страниц: {self.num_pages}, материал: {self.material}{reserved_str}"
        )


# создаем экземпляры книг
book1 = Book('бумага', True, 'Мастер и Маргарита', 'Михаил Булгаков', 400, '1234567890')
book2 = Book('бумага', True, 'Война и мир', 'Лев Толстой', 1000, '2345678901')
book3 = Book('электронная', True, 'Стив Джобс', 'Уолтер Айзексон', 600, '3456789012')
book4 = Book('бумага', False, '451 градус по Фаренгейту', 'Рэй Брэдбери', 300, '4567890123')
book5 = Book('бумага', True, 'Идиот', 'Федор Достоевский', 500, '5678901234')

# помечаем одну книгу как зарезервированную
book1.reserve()

# печатаем детали каждой книги
book1.print_details()
book2.print_details()
book3.print_details()
book4.print_details()
book5.print_details()


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

class Textbook(Book):
    def __init__(
            self, material, text, title, author, pages, isbn, reserved=False, subject="",
            grade="", exercises=False
    ):
        super().__init__(material, text, title, author, pages, isbn, reserved)
        self.subject = subject
        self.grade = grade
        self.exercises = exercises

    def print_details(self):
        if self.is_reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"материал: {self.material}, предмет: {self.subject}, класс: {self.grade}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, материал: {self.material}, "
                f"предмет: {self.subject}, класс: {self.grade}"
            )


# Создаем экземпляры учебников
textbook1 = Textbook("бумага", True, "Алгебра", "Иванов", 200, "1111", True, "Математика", "9")
textbook2 = Textbook("бумага", True, "История", "Петров", 150, "2222", False, "История", "8")
textbook3 = Textbook("бумага", True, "География", "Сидоров", 180, "3333", False, "География", "7")
textbook4 = Textbook("электронный", True, "Физика", "Смирнов", 250, "4444", False, "Физика", "10")
textbook5 = Textbook("бумага", True, "Биология", "Козлов", 220, "5555", False, "Биология", "11")

# Выводим детали о каждом учебнике
textbook1.print_details()
textbook2.print_details()
textbook3.print_details()
textbook4.print_details()
textbook5.print_details()
