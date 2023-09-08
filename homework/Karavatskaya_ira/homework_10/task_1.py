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
    material = 'бумага'
    text = True

    def __init__(self, title, author, num_pages, material, reserved, isbn):
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.material = material
        self.reserved = reserved
        self.isbn = isbn

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages},"
                f" материал: {self.material}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, "
                f"страниц: {self.num_pages}, материал: {self.material}"
            )


book1 = Book("Мастер и Маргарита", "Булгаков", 400, "бумага", False, '54335667')
book2 = Book("Война и мир", "Толстой", 1000, "бумага", True, '43456788')
book3 = Book("Уолтер Айзексон", "Стив Джобс", 600, "бумага", False, '456835555')
book4 = Book("451 градус по Фаренгейту", "Рэй Брэдбери", 300, "бумага", False, '555544322')
book5 = Book("Идиот", "Федор Достоевский", 500, "бумага", False, '67654766')

book2.reserved = True

print("Детали о каждой книге:")
book1.details()
book2.details()
book3.details()
book4.details()
book5.details()


class Textbook(Book):
    def __init__(self, title, author, num_pages, material, reserved, isbn, subject, grade, exercises):
        super().__init__(title, author, num_pages, material, reserved, isbn)
        self.subject = subject
        self.grade = grade
        self.exercises = exercises

    def details(self):
        if self.reserved:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"материал: {self.material}, предмет: {self.subject}, класс: {self.grade}, зарезервирована"
            )
        else:
            print(
                f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, "
                f"материал: {self.material}, предмет: {self.subject}, класс: {self.grade}"
            )


textbook1 = Textbook("Алгебра", "Иванов", 200, "бумага", False, '345678', "Математика", 9, True)
textbook2 = Textbook("История", "Петров", 150, "бумага", True, '4324566', "История", 10, True)
textbook3 = Textbook("География", "Сидоров", 180, "бумага", False, '5432123', "География", 8, True)
textbook4 = Textbook("Физика", "Смирнов", 250, "бумага", False, '6543344', "Физика", 11, True)
textbook5 = Textbook("Биология", "Козлов", 220, "бумага", False, '6543232', "Химия", 10, True)

textbook2.reserved = True

print("Детали о каждом учебнике:")
textbook1.details()
textbook2.details()
textbook3.details()
textbook4.details()
textbook5.details()
