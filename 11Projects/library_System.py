# Program to make Library Management System using Python.

class LibraryItem:
    def __init__(self, title, year):
        self.__title = title   
        self.__year = year     

    # ?Getter for title
    def get_title(self):
        return self.__title

    # Setter for title
    def set_title(self, title):
        self.__title = title

    # ?Getter for year
    def get_year(self):
        return self.__year

    # ?Setter for year
    def set_year(self, year):
        self.__year = year

    def get_info(self):
        return f"Title: {self.__title}, Year: {self.__year}"

class Book(LibraryItem):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.__author = author   

    # ?Getter for author
    def get_author(self):
        return self.__author

    # ?Setter for author
    def set_author(self, author):
        self.__author = author

    # ?Overriding the get_info method
    def get_info(self):
        return f"Title: {self.get_title()}, Year: {self.get_year()}, Author: {self.__author}"

class Magazine(LibraryItem):
    def __init__(self, title, year, issue):
        super().__init__(title, year)
        self.__issue = issue   

    # ?Getter for issue
    def get_issue(self):
        return self.__issue

    # ?Setter for issue
    def set_issue(self, issue):
        self.__issue = issue

    # ?Overriding the get_info method
    def get_info(self):
        return f"Title: {self.get_title()}, Year: {self.get_year()}, Issue: {self.__issue}"

# ?Creating instances of Book and Magazine
book = Book("1984", 1949, "George Orwell")
magazine = Magazine("Time", 2023, "July")

# ?Accessing information through polymorphic method
items = [book, magazine]

for item in items:
    print(item.get_info())

