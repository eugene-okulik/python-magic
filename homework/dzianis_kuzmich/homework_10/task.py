# First Class
class Book:
    def __init__(self, title, author, num_pages, ISBN, material='бумага', text=True):
        self.material = material
        self.text = text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = False

    def reserve(self):
        self.reserved = True

    def print_details(self):
        details = f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, материал: {self.material}"
        print(details)


# Second Class
class SchoolBook(Book):
    def __init__(self, title, author, num_pages, ISBN, subject, grade_level, exercises, material='paper', text=True):
        self.material = material
        self.text = text
        self.title = title
        self.author = author
        self.num_pages = num_pages
        self.ISBN = ISBN
        self.reserved = False

        # Additional attributes
        self.subject = subject
        self.grade_level = grade_level
        self.exercises = exercises

    def print_details(self):
        details = f"Название: {self.title}, Автор: {self.author}, страниц: {self.num_pages}, предмет: {self.subject}," \
                  f" класс: {self.grade_level}"
        if self.reserved:
            details += ", зарезервирована"
        print(details)


# Create instances of books
book1 = Book("Идиот", "Достоевский", 500, "123-456")
book2 = Book("Война и мир", "Толстой", 1000, "789-012")
book3 = Book("1984", "Оруэлл", 300, "345-678")

# Mark one book as reserved
book2.reserve()

# Print book details
book1.print_details()
book2.print_details()
book3.print_details()

# Create instances of school books
school_book1 = SchoolBook("Алгебра", "Иванов", 200, "910-111", "Математика", 9, True)
school_book2 = SchoolBook("История", "Петров", 150, "112-113", "История", 10, True)

# Mark one school book as reserved
school_book2.reserve()

# Print school book details
school_book1.print_details()
school_book2.print_details()
