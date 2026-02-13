import logging

logging.basicConfig(
    filename='logging.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s')

class Order:
    tax_percentage = 3

    def __init__(self,order_id,item_name,price,quantity):
        self.order_id = order_id
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
        self.is_cancelled = False

    def place_order(self):
        logging.info("Order %s placed successfully for %s %s",self.order_id,self.quantity,self.item_name)

    def cancel_order(self):
        self.is_cancelled = True
        logging.info("Order %s has been cancelled",self.order_id)

    def calculate_total_price(self):
        if self.is_cancelled:
            logging.warning("Order %s is cancelled",self.order_id)
            return 0
        total = (self.price * self.quantity) + ((self.price * self.quantity) * Order.tax_percentage) / 100
        return total

    @classmethod
    def update_tax_percentage(cls,new_tax_percentage):
        if new_tax_percentage >= 0:
            cls.tax_percentage = new_tax_percentage
        else:
            logging.error("Tax percentage is invalid")

order1 = Order(123,"Laptop",50000,2)
order1.place_order()
logging.info("Total Price: %s",order1.calculate_total_price())
Order.update_tax_percentage(5)
logging.info("Total Price after updation: %s",order1.calculate_total_price())
order1.cancel_order()
