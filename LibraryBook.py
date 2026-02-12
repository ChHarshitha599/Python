from datetime import datetime

class LibraryBook:
    fine = 10
    max_days = 10
    max_books = 5

    def __init__(self, no_of_books):
        self.no_of_books = no_of_books
        self.fine_amount = 0

    def issue_book(self, name, issue_date):
        self.name = name
        self.issue_date = issue_date
        if self.no_of_books < LibraryBook.max_books:
            self.no_of_books += 1
            print("Book issued to", self.name)
        else:
            print("Maximum books limit reached")

    def return_book(self, amt_paid):
        if self.no_of_books <= 0:
            print("No books to return")
        else:
            print("Book returned by", self.name)
            self.no_of_books -= 1
            if self.fine_amount > 0:
                if amt_paid == self.fine_amount:
                    print("Fine paid")
                elif amt_paid > self.fine_amount:
                    print("Return amount", amt_paid - self.fine_amount)
                else:
                    print("Fine unpaid")
            else:
                print("No fine to pay")

    def calculate_fine(self, return_date):
        days_late = (return_date.date() - self.issue_date.date()).days

        if days_late > LibraryBook.max_days:
            extra_days = days_late - LibraryBook.max_days
            self.fine_amount = extra_days * LibraryBook.fine
            print("Fine amount:", self.fine_amount)
        else:
            self.fine_amount = 0
            print("No fine")

    @classmethod
    def update_fine_amount(cls, new_fine):
        if new_fine >= 0:
            cls.fine = new_fine
            print("Updated fine amount:", cls.fine)
        else:
            print("Fine amount is invalid")

l1 = LibraryBook(6)
l1.issue_book("Harshitha", datetime(2026,1,1))
l1.calculate_fine(datetime(2026,1,15))
l1.return_book(50)
LibraryBook.update_fine_amount(15)
