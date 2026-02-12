from datetime import datetime
class LibraryBook:
    fine = 10

    def __init__(self,book_title, author):
        self.book_title = book_title
        self.author = author

    def issue_book(self,name,issue_date):
        self.name = name
        self.issue_date = issue_date
        print("Book issued to ",self.name)

    def return_book(self,amt_paid):
        print("Book returned by ",self.name)
        if self.fine_amount > 0:
            if amt_paid == self.fine_amount:
                print("Fine paid")
            elif amt_paid > self.fine_amount:
                print("Return amount",amt_paid - self.fine_amount)
            else:
                print("Fine unpaid")

    def calculate_fine(self, return_date, issue_date):
        self.return_date = return_date
        self.issue_date = issue_date
        days_late = (self.return_date.date() - self.issue_date.date()).days
        if days_late > 0:
            self.fine_amount = days_late * LibraryBook.fine
            print("Fine amount: ",self.fine_amount)
        else:
            print("No fine")
        
    @classmethod
    def update_fine_amount(cls,new_fine):
        if new_fine >= 0:
            cls.fine = new_fine
            print("Updated fine amount: ",cls.fine)
        else:
            print("Fine amount is invalid")

l1 = LibraryBook("The Great Gatsby","F.Scott Fitzgerald")
l1.issue_book("Harshitha",datetime(2026,1,1))
l1.calculate_fine(datetime(2026,1,10), datetime(2026,1,1))
l1.return_book(100)
LibraryBook.update_fine_amount(15)
