class Publisher:

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Publisher {self.name}")


class Book(Publisher):

    def __init__(self, name, title, author, price):
        super().__init__(name)
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        super().display()

        print(f"Book title: {self.title}")
        print(f"author {self.author}")
        print(f"price {self.price}")


b1 = Book("Safa Publishers", "Wings of fire", "kalam", 500)
b1.display()
