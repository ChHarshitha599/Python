import logging

logging.basicConfig(
    filename='Movie.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    force=True)

class MovieTicket:
    
    ticket_price = 350
    
    def __init__(self,movie_name,time,seat_number):
        self.movie_name = movie_name
        self.time = time
        self.seat_number = seat_number
        self.is_booked = False
    
    def book_seat(self):
        if not self.is_booked:
            self.is_booked = True
            logging.info("Seat %s booked successfully for '%s'",self.seat_number,self.movie_name)
        else:
            logging.warning("Seat %s is already booked",self.seat_number)
    
    def cancel_booking(self):
        if self.is_booked:
            self.is_booked = False
            logging.info("Booking for seat %s has been cancelled",self.seat_number)
        else:
            logging.warning("Seat %s is not booked",self.seat_number)
    def calculate_ticket_price(self):
        tax = 0.10 * MovieTicket.ticket_price
        total = MovieTicket.ticket_price + tax
        return total
    
    @classmethod
    def update_ticket_price(cls, new_price):
        if new_price > 0:
            cls.ticket_price = new_price
            logging.info("Ticket price updated to %s",cls.ticket_price)
        else:
            logging.warning("Invalid ticket price")

t1 = MovieTicket("Harshitha","7 PM","B10")
t1.book_seat()
print("Total Price:",t1.calculate_ticket_price())
t1 .cancel_booking()
MovieTicket.update_ticket_price(250)
print("New Total Price:", t1.calculate_ticket_price())