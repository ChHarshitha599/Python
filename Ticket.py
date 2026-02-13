import logging

logging.basicConfig(
    filename='Ticket.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    force=True)

class Ticket:
    base_fare = 3

    def __init__(self,ticket_no,passenger_name,destination,distance):
        self.ticket_no = ticket_no
        self.passenger_name = passenger_name
        self.destination = destination
        self.distance = distance
        self.is_booked = False
        self.is_cancelled = False

    def book_ticket(self):
        if self.is_booked:
            logging.info("Ticket already booked.")
            return
        self.is_booked = True
        logging.info("Ticket booked successfully.Ticket No: %s, Passenger Name: %s, Destination: %s",self.ticket_no,self.passenger_name,self.destination)

    def cancel_ticket(self):
        if not self.is_booked:
            logging.info("Ticket not booked yet.")
            return
        self.is_cancelled = True
        logging.info("Ticket %s cancelled successfully.",self.ticket_no)

    def calculate_fare(self):
        fare = self.distance * Ticket.base_fare
        if self.is_cancelled:
            return fare - (fare * 0.30)
        return fare
    
    @classmethod
    def update_base_fare(cls,new_fare):
        if new_fare > 0:
            cls.base_fare = new_fare
            logging.info("Base fare updated to %s per km.",new_fare)
        else:
            logging.info("Invalid base fare.")
            
t1 = Ticket(123,"Harshitha","Hyderabad",130)
t1.book_ticket()
logging.info("Fare: %s", t1.calculate_fare())
t1.cancel_ticket()
logging.info("Refund after cancellation: %s",t1.calculate_fare())
Ticket.update_base_fare(3)
logging.info("Fare after base fare update: %s",t1.calculate_fare())
