class Patient:
    fee=1500

    def __init__(self,name,age,phone):
        self.name = name
        self.age = age
        self.phone = phone

    def admit_patient(self,disease):
        self.disease = disease
        print("Patient admitted with disease: ",self.disease)

    def discharge_patient(self,amount_paid):
        print("Amount paid by patient: ",amount_paid)
        if amount_paid<=0:
            print("Invalid amount")
        elif self.total_bill - amount_paid > 0:
            print("Amount due: ",self.total_bill - amount_paid)
        elif self.total_bill - amount_paid < 0:
            print("Return amount: ",amount_paid - self.total_bill)
        else:
            print("Bill paid")

    def calculate_bill(self,no_of_days,per_day_charge):
        self.no_of_days = no_of_days
        self.per_day_charge = per_day_charge
        self.total_bill = (self.no_of_days*self.per_day_charge)+Patient.fee
        print("Total bill for discharge: ",self.total_bill)

    @classmethod
    def update_consultation_fee(cls,new_fee):
        if new_fee >= 0:
            cls.fee = new_fee
            print("Updated consultation fee: ",cls.fee)
        else:
            print("Consultation fee is invalid")

p1 = Patient("A",22,"6528652747")
p1.admit_patient("Fever")  
p1.calculate_bill(5,400)
p1.discharge_patient(3000)
Patient.update_consultation_fee(2500)
print("Updated fee: ",Patient.fee)