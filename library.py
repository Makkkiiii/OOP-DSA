class Book:
    default_rental_price_per_day = 5.0

    def __init__(self, title, author, copies_available, custom_rental_price=None):
        self.title = title
        self.author = author
        self.copies_available = copies_available
        self.custom_rental_price = custom_rental_price

    @classmethod
    def update_default_rental_price(cls, new_price):
        cls.default_rental_price_per_day = new_price

    def get_rental_price(self):
        return self.custom_rental_price or Book.default_rental_price_per_day

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies Available: {self.copies_available}")
        print(f"Rental Price per Day: ${self.get_rental_price():.2f}")


book1 = Book("The Linux History", "L. Troy", 3)
book2 = Book("Kali", "Linux", 5, custom_rental_price=7.0)
book1.display_details()
book2.display_details()
Book.update_default_rental_price(6.0)
book1.display_details()
book2.display_details()