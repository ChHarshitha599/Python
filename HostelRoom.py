import logging

logging.basicConfig(
    filename='HostelRoom.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    force=True)

class HostelRoom:
    room_rent = 5000

    def __init__(self,room_number,room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.student_name = None

    def allocate_room(self,student_name):
        if self.student_name is None:
            self.student_name = student_name
            logging.info("Room %s allocated to %s.",self.room_number,student_name)
        else:
            logging.warning("Room %s already occupied by %s.",self.room_number,self.student_name)

    def vacate_room(self):
        if self.student_name is not None:
            logging.info("%s has vacated Room %s.",self.student_name,self.room_number)
            self.student_name = None
        else:
            logging.warning("Room %s is already vacant.",self.room_number)

    def calculate_monthly_fee(self):
        if self.student_name is None:
            logging.info("Room is vacant")
            return 0
        if self.room_type == "Double":
            return HostelRoom.room_rent-1000
        else:
            return HostelRoom.room_rent

    @classmethod
    def update_room_rent(cls,new_rent):
        if new_rent > 0:
            cls.room_rent = new_rent
            logging.info("Room rent updated to %s",new_rent)
        else:
            logging.warning("Invalid rent amount")

h1 = HostelRoom(121,"Single")
h1.allocate_room("Harshitha")
logging.info("Fee: %s",h1.calculate_monthly_fee())
h1.update_room_rent(6000)
h1.vacate_room()
