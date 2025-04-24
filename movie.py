class Movie:
  
    ticket_price = 10.0 

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def display_info(self):
        print(f"Movie: {self.title}, Duration: {self.duration} minutes")

    @classmethod
    def update_ticket_price(cls, new_price):
        cls.ticket_price = new_price
        print(f"Updated price: ${cls.ticket_price:.2f}")

    @staticmethod
    def calculate_total_price(num_tickets):
        return num_tickets * Movie.ticket_price

if __name__ == "__main__":
    
    movie1 = Movie("Inception", 148)
    movie2 = Movie("The Matrix", 136)

    
    movie1.display_info()
    movie2.display_info()

    print(f"Initial ticket price: ${Movie.ticket_price:.2f}")

    Movie.update_ticket_price(12.5)

    num_tickets = 3
    total_price = Movie.calculate_total_price(num_tickets)
    print(f"Total price for {num_tickets} tickets: ${total_price:.2f}")