class LibraryItem:
    def __init__(self, title: str, author: str, item_id: str, available: bool = True):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.available = available


class Book(LibraryItem):
    def __init__(self, isbn: str, title: str, author: str, item_id: str, available: bool = True):
        super().__init__(title, author, item_id, available)
        self.isbn = isbn

    def __str__(self):
        return "This is an item in library with type {0} and item title {1} and author {2} and availability {3} and item id {4}".format(
            self.__class__.__name__, self.title, self.author, self.available, self.item_id)


class DVD(LibraryItem):
    def __init__(self, director: str, runtime: int, title: str, author: str, item_id: str, available: bool = True):
        super().__init__(title, author, item_id, available)
        self.director = director
        self.runtime = runtime

    def __str__(self):
        return "This is an item in library with type {0} and item title {1} and author {2} and availability {3} and item id {4}".format(
            self.__class__.__name__, self.title, self.author, self.available, self.item_id)


class Magazine(LibraryItem):
    def __init__(self, title: str, author: str, item_id: str, issue_number: int, publication_date: str,
                 available: bool = True):
        super().__init__(title, author, item_id, available)
        self.issue_number = issue_number

    def __str__(self):
        return "This is an item in library with type {0} and item title {1} and author {2} and availability {3} and item id {4}".format(
            self.__class__.__name__, self.title, self.author, self.available, self.item_id)


class Library():
    total_items = 0
    items = []

    def add_item(self, item: LibraryItem):
        self.items.append(item)
        self.total_items = self.total_items + 1

    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                self.total_items = -1
                break

    def checkout_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.available = False

    def return_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                item.available = True

    def display_available_items(self):
        for item in self.items:
            if item.available == True:
                print(
                    "list of available items is showing -> item title: {0} , item id {1}, item availability {2}".format(
                        item.title, item.item_id, item.available))

    def display_items_by_type(self, item_type):
        for item in self.items:
            if isinstance(item, item_type):
                print("list of all items with type of {0} is showing , item title : {1} ".format(type(item).__name__,
                                                                                                 item.title))


dvd1 = DVD(title="dvd1", item_id="1", available=True, author='dvdauthor1', director="dvddirector1", runtime="druntime1")
dvd2 = DVD(title="dvd2", item_id="2", available=True, author='dvdauthor2', director="dvddirector2", runtime="druntime2")
book1 = Book(title="book1", author="author1", item_id="3", available=True, isbn="book1isbn")
book2 = Book(title="book2", author="author2", item_id="4", available=True, isbn="book2isbn")
magazine1 = Magazine(title="magazine1", author="authormagazaine1", item_id="5", available=True, issue_number=5,
                     publication_date="publicationdatemag1")
magazine2 = Magazine(title="Magazine2", author="authormagazine2", item_id="6", available=True, issue_number=6,
                     publication_date="publicationdatemag2")
lib = Library()
lib.add_item(dvd1)
lib.add_item(dvd2)
lib.add_item(book1)
lib.add_item(book2)
lib.add_item(magazine1)
lib.add_item(magazine2)
lib.checkout_item(magazine1.item_id)
lib.checkout_item(book2.item_id)
lib.checkout_item(dvd1.item_id)
lib.display_available_items()
lib.remove_item(dvd2.item_id)
lib.return_item(magazine1.item_id)
lib.display_available_items()
lib.display_items_by_type(DVD)
lib.display_items_by_type(Magazine)
lib.display_items_by_type(Library)
