import logging

logging.basicConfig(
    filename='Employee.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w',
    force=True)

class Employee:
    hra_percentage = 15

    def __init__(self,emp_id,name,salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
        self.leaves = 0
        self.deduction = 0

    def calculate_salary(self):
        hra = (self.salary * Employee.hra_percentage) / 100
        net_salary = (self.salary + hra) - self.deduction
        return net_salary
    
    def apply_leave_deduction(self,leave_days):
        self.leave_days = leave_days
        per_day_salary = self.salary / 30
        self.deduction = per_day_salary * leave_days
        logging.info("%s days leave applied so Deduction is %s",leave_days,self.deduction)

    def display_payslip(self):
        hra = (self.salary * Employee.hra_percentage) / 100
        net_salary = self.calculate_salary()

        logging.info("Employee ID: %s",self.emp_id)
        logging.info("Name: %s",self.name)
        logging.info("Salary: %s",self.salary)
        logging.info("HRA (%s): %s",Employee.hra_percentage,hra)
        logging.info("Leave Deduction: %s",self.deduction)
        logging.info("Net Salary: %s",net_salary)

    @classmethod
    def update_hra_percentage(cls,new_hra):
        if new_hra >= 0:
            cls.hra_percentage = new_hra
            logging.info("HRA percentage updated to %s",new_hra)
        else:
            logging.error("Invalid HRA percentage")

e1 = Employee(321,"Harshitha",150000)
e1.apply_leave_deduction(2)
e1.display_payslip()
Employee.update_hra_percentage(25)
e1.display_payslip()